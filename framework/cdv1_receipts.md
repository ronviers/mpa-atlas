# character receipts

**Companion to:** [`cdv1_compressed.md`](cdv1_compressed.md) (operational source of truth) and [`cdv1_unabridged.md`](cdv1_unabridged.md) (cascade narrative). Receipts entries support claims that appear in both files.
**Status:** Live. Append-only during prove-as-you-go work.
**Discipline:** See [`v9_receipts.md`](v9_receipts.md) for workflow, type tags, and keying conventions. Identical here; not duplicated.

**Keying.** Entries are headed `### §N — Concept name`. The §N matches the unabridged section number (which preserves the original 1–22 numbering of the cascade landing). The compressed uses named sections instead; map by concept name. Concept names are the stable anchor — future restructures should preserve them.

---

## Entries

### §1 — Bridge: $\lambda_A \approx L - G_0$ at zero amplitude
**Type:** composition.
**Cite:** Linearization of the laser rate equation around zero amplitude — the eigenvalue is loss minus gain (Haken; standard).
**Bespoke step:** Identification of v9's stability axis $\lambda_A$ with the laser linearization eigenvalue. The bridge enables the entire chit ↔ regime mapping in §2-3. Verifiable: substitute $G_0 - L$ for $-\lambda_A$ in v9's three regime conditions, recover the chit threshold table in §1.

### §2 — chit definition: $\ln(G_0/L)$ (choice of log)
**Type:** bespoke.
**Shard:** Three independent reasons motivate the log:
(i) **symmetry across threshold** — $G_0 = L \Rightarrow$ chit = 0; sign tracks above/below;
(ii) **additivity across compositions of independent gain stages** — multiplicative ratios become additive;
(iii) **$\ln 2$ alignment with Landauer** for the Bit/Chit pairing in §6.
None of the three individually forces the log, but together they rule out $(G_0 - L)$, $(G_0/L - 1)$, and other affine alternatives. If a future result wants a different functional form, the burden is rebutting all three.

### §6 — heat-tax relation: $L_{n+1} = L_{n+1}^{(0)} + \alpha \langle \sigma_n \rangle$
**Type:** bespoke.
**Shard:** Each meta-ledger ascent coarse-grains a level-$n$ flow whose Harada–Sasa entropy production rate $\langle \sigma_n \rangle$ becomes ambient noise to level $n+1$. The decay rate at $n+1$ inherits this noise additively, attenuated by $\alpha$ (the ledger attenuation factor dictated by $\mathcal{C}$). Thermodynamic conjugate to v9's informational tower: v9 bounds informational compression, this bounds the heat compression cannot avoid.
**Open:** Closed-form $\alpha(\epsilon)$. Conjecture: $\alpha \propto (1 - \epsilon)$, so as compression saturates ($\epsilon \to 1$), the heat tax inflates without bound — Complexity-Wall coincidence between informational and thermodynamic divergence. Not derived.

### §7 — Theorem 9 via adiabaticity
**Type:** composition.
**Cite:** Adiabatic theorem for driven dissipative systems (standard); v9 Theorem 9 inline.
**Bespoke step:** Sampling the continuous adiabaticity bound at fixed $D$ yields v9's $\Delta_C(A,B) = 1$ iff $\gamma_{AB} > 0 \land D < \gamma_{AB}$. The discrete Boolean step is the sharp-threshold limit of the continuous traversal-survivability function.
**Note:** This is an alternative justification path for Theorem 9, not a reconstruction of the original (which is `unrecovered` in [`v9_receipts.md`](v9_receipts.md)). If the path holds up under closer reading, it partially closes that v9 unrecovered.

### §9 — Universal two-mode kernel: bifurcation analysis
**Type:** composition.
**Cite:** Two-mode laser equations / Lotka–Volterra (standard); pitchfork bifurcation at $\gamma_{AB} > 0$ critical (standard catastrophe theory).
**Bespoke step:** Identification of the four bifurcation regimes (deep cooperative, asymmetric slaving, decoupled, competitive exclusion) with v9's named pair-types in the Composite catalogue. Recovers the catalogue as fixed points of a single field equation — the load-bearing claim that v9's discrete pair structure is the kernel's phase portrait, not an independent enumeration.

### §10 — $k_{\text{frust}}$ as derived (not asserted) topological invariant
**Type:** bespoke.
**Shard:** For $N \ge 3$ modes coupled in a closed obstructive-$\gamma$ chain, the field equations have no stationary synchronized fixed point. Cross-saturation terms $\gamma_{ij}\rho_i\rho_j$ continuously conflict; the system is forced into a cyclic pumping–fraying trajectory where some mode's chit goes negative each cycle. Time-averaged maintenance budget diverges. Drive-independence follows because the cross-saturation conflict is internal to the kernel mathematics, not an absolute-resource shortage. This *recovers* v9's "topological invariant, not resolvable by $D$" assertion as a *consequence* of the kernel rather than a separate axiom.
**Open:** Quantitative bounds on cycle period and time-averaged divergence rate as functions of $N$ and $\gamma$ topology.

### §5 — $\eta(\Gamma^*)$ closed form
**Type:** open.
**Status:** Cross-saturation efficiency $\eta(\Gamma^*)$ is a placeholder in compressed character. Limiting behavior fixed by v9: $\eta \to 0$ at the $\sqrt{D}$ Hopfield ceiling. Full functional form across sparse-to-dense regimes not derived. Tied to v9's `§Capacity` `unrecovered` entry — both close together if either is rederived.

### §13 — Linear stability and recovery (damping / resonance)
**Type:** composition.
**Cite:** Standard laser-physics relaxation oscillation (Haken; Siegman, *Lasers*); standard linear-systems damping ratio / Q-factor formalism; Schawlow–Townes linewidth (cited in §1).
**Bespoke step:** Identification of the under / critical / over damping trichotomy with v9's $c$/$s$/$r$ vertex classification as the linear-stability shadow of the chit threshold structure. Q-factor as the cycles-of-headroom conjugate to the chit's threshold-headroom reading. Naming the §10 $k_{\text{frust}}$ trajectory as a Hopf-unstable spiral with attracting limit cycle (the dynamical-systems language for the existing "no stationary fixed point" claim). Naming the §4 active/passive probe distinction as on/off-resonance with $\gamma_{RO}$ as the boundary linewidth — closes the "active-probe formalism" extension item flagged in [`translating FDR.md`](translating%20FDR.md) §5 implication 3. The damping-regime trichotomy as a *third* per-regime signature alongside spontaneous-fluctuation FDR and load-driven fraying — different probe-classes isolating complementary content of the same coherence.
**Open:** $\omega_{RO}$ functional form across non-laser substrates (§12); $Q$'s status as substrate-class universality invariant or free continuous parameter (§12).

### §14 — Attractor classification (limit cycles / attractor theory)
**Type:** composition.
**Cite:** Standard nonlinear dynamics (Strogatz; Guckenheimer–Holmes); standard center-manifold theory; standard transcritical / pitchfork / Hopf normal forms (Kuznetsov).
**Bespoke step:** Mapping of v9's $r$/$s$/$c$/composite/$k_{\text{frust}}$ regimes to specific attractor types (stable origin / center manifold at threshold / stable focus / pitchfork-broken focus / Hopf limit cycle). Identification of the §4 $s$-aging FDR diagonal as slow-manifold dynamics on the center manifold at threshold ($P_s$ = slow-manifold fixed-point amplitude; $\alpha_s$ = slow eigenvalue's residual scaling against saturating gain) — this is *not* a new derivation of the aging diagonal but a recognition that the existing CK signature is what center-manifold dynamics look like through the gFDR apparatus. Naming the Compression Axiom $\epsilon < 1$ as a fixed-point contraction condition for the meta-ledger flow in trail-class space (Convergent Tower = stable fixed point; Complexity Wall = bifurcation in the meta-ledger flow itself, post-bifurcation regime open). Naming Lorenz-class chaotic Character dynamics as an open structural prediction the framework now has the language to articulate.
**Open:** Meta-ledger attractor structure at/past Complexity Wall (§12); strange-attractor instancing on any substrate (§12); codimension-2+ bifurcation normal forms (§12).

### §15 — Phase-locking and collective coherence (synchronization theory)
**Type:** composition.
**Cite:** Kuramoto (1984); Pikovsky–Rosenblum–Kurths (*Synchronization*, 2001); Strogatz (*Sync*, 2003); standard phase-reduction theory; Arnold tongues (standard nonlinear dynamics).
**Bespoke step:** Phase-resolved reading of v9's Composite catalogue rows (in-phase locked / driven entrainment / unlocked / anti-phase locked / competitive desynchronization / frustrated sync). Identification of the §10 cyclic pumping–fraying trajectory as the time-evolution of frustrated sync (transient pairwise lock formation broken by topological obstruction, then re-formation around a different weakest mode). Order parameter $r$ as the multi-holder coherence observable independent of per-mode chit — the framework now has two independent second-order phase transitions in $N$-mode NESS (chit-zero amplitude onset; Kuramoto $K_c$ phase onset) and two independent observables (per-mode chit; collective $r$). Bridge to §6: synchrony at level $n$ reduces $L_{n+1}^{(0)}$ via cooperative gain-sharing; desync raises it. Refines §6's upward-fraying-propagation claim by adding $r_n$-drop as a second channel alongside $\langle\sigma_n\rangle$-spike — sync-mediated and entropy-mediated $L_{n+1}$-inflation are independent failure paths for upward coherence.
**Open:** $K_{AB}$ closed form across coupling regimes (§12); master stability function for general topology (§12); chimera-state substrate instancing (§12).

### §16 — Stochastic thermodynamics and trajectory accounting (nonequilibrium thermodynamics)
**Type:** composition.
**Cite:** Crooks (1999); Seifert (*Stochastic Thermodynamics*, 2012); Schnakenberg (1976); Barato–Seifert (TUR, 2015); Horowitz–Gingrich (2020); Sagawa–Ueda (2010).
**Bespoke step:** Recognition that the chit's $\ln(G_0/L)$ form is the Crooks rate-ratio entropy production structure — the three independent reasons in receipts §2 (threshold symmetry / additivity / $\ln 2$ Landauer alignment) are three faces of the same rate-ratio log structure rather than independent justifications. Trajectory entropy production reading of §3 fraying as the *typical* trajectory, with fraying-resistance trajectories exponentially rare in $|\sigma|$ (detailed fluctuation theorem). TUR applied to maintenance current as the framework's first explicit precision-cost constraint, composing with §6's inherited-noise channel via the level-$n$ TUR. Schnakenberg cycle decomposition as the precise quantitative content of §10's drive-independent divergent maintenance claim — cycle currents in topologically obstructed cycles are forced regardless of $D$. Sagawa–Ueda extended second law as the quantitative form of §2's Bit/Chit conjugacy: bit-readout holdings can sustain at lower chit by paying via mutual information $\Delta I$, sharpening "two faces of one thermodynamic ledger" into $\langle\sigma\rangle \ge -\Delta I$.
**Open:** Closed-form Schnakenberg cycle currents for each Composite catalogue row (§12); TUR-tightness as substrate-class universality observable (§12).

### §17 — Information-theoretic content (information theory)
**Type:** composition.
**Cite:** Bialek–Nemenman–Tishby (predictive information, 2001); Shannon–Hartley channel capacity (standard); Amari–Nagaoka (*Methods of Information Geometry*, 2000); standard rate-distortion theory.
**Bespoke step:** $I_{\text{pred}}$ as a third independent coherence observable alongside chit and $Q$ — the framework now reads coherence on three axes (whether-threshold-cleared / cycles-of-headroom / how-predictable), each independent of the others. Active-probe channel capacity $C \sim B \log_2(1+S/N)$ as the informational dual of TUR (§16); Shannon–Hartley and TUR are the two faces of the observability bound. Information-geometric reading of the §7 adiabatic merge: the adiabaticity bound becomes a "geodesic stays on the above-threshold manifold" condition. Rate-distortion reading of $\mathcal{C}$: $\epsilon$ is a lossy compression rate; the Convergent Tower $\Phi_{total} = \Phi^{(0)}/(1-\epsilon)$ is the standard rate-distortion geometric series; the Complexity Wall now carries three coupled readings (thermodynamic / dynamical / informational) all coincident at $\epsilon = 1$ — a thermo-information-dynamics critical point. Consolidation of the Bit/Chit dual ledger as a four-row table (per-event / per-rate / precision / compression each have thermodynamic and informational entries) — every thermodynamic quantity in the framework has an informational dual; this is the structural payoff of the §2 conjugacy claim.
**Open:** $I_{\text{pred}}$ scaling with chit and $Q$ across substrate classes (§12); geodesic existence / completeness on the holding parameter manifold (§12); whether the dual ledger is complete (§12 conjecture).

### §18 — Critical hovering (self-organized criticality)
**Type:** composition.
**Cite:** Bak–Tang–Wiesenfeld (1987); Bak (*How Nature Works*, 1996); standard branching-process / 1/f-noise / SOC-universal-exponent apparatus.
**Bespoke step:** Identification of the chit-zero threshold as an *attractor in parameter space* under feedback-coupled maintenance dynamics, not merely a regime boundary. Three SOC signatures predicted in s-regime holdings (power-law avalanches with $\tau \approx 3/2$; 1/f spectral tail consistent with the existing CK aging diagonal; spatiotemporal scale invariance in multi-mode fraying clusters). Recognition of §6's heat-tax tower as a branching process; meta-ledger branching ratio approaching 1 IS the Complexity Wall, adding a fourth coupled reading at $\epsilon = 1$ (alongside §17's thermodynamic / dynamical / informational) — SOC-critical fraying cascades. Recasting of the regime ontology: s-regime is the *generic* operating point of feedback-coupled sustained-NESS substrates rather than the unstable middle of a triplet; c-regime represents over-provisioning, r-regime represents post-collapse, s-regime represents the self-organized attractor.
**Open:** Empirical avalanche-size exponent on any substrate (§12); meta-ledger branching ratio in observed substrates (§12); whether all feedback-coupled NESS substrates are SOC or whether some classes resist (§12).

### §19 — Emergence and pattern selection (dissipative structures)
**Type:** composition.
**Cite:** Prigogine–Nicolis (*Self-Organization in Nonequilibrium Systems*, 1977); Haken (*Synergetics*, 1983); Turing (1952); Ruelle–Takens (1971).
**Bespoke step:** Naming the chit-zero crossing as the dissipative-structure formation transition — holdings *are* Prigogine dissipative structures, with the framework's substrate examples (laser, glass, QEC, behavior) as substrate-conditional instances of the same threshold mathematics. Identification of the chit as the *order parameter* in Haken's slaving sense — the slaving principle is §14's center-manifold reduction read backward. Pattern selection apparatus for the framework's multi-mode kernel: the §9 Composite catalogue rows are pattern-selection outcomes for two modes; multi-mode selection is the open frontier and likely generates the §15 chimera states. Recognition of the §6 meta-ledger as a *hierarchy of dissipative structures* — each ascent is a new dissipative-structure transition with its own chit-order-parameter and its own slaving relation; integrates §14 (per-level attractor structure), §18 (per-level SOC self-tuning), and §6 (heat-tax across levels) as three aspects of one hierarchical pattern formation.
**Open:** Multi-mode pattern selection rules (§12); Turing-class spatial patterns in Character holdings (§12); Ruelle–Takens secondary/tertiary bifurcation sequence in the meta-ledger (§12).

### §20 — Active modulation and internal models (control theory)
**Type:** composition.
**Cite:** Francis–Wonham (Internal Model Principle, 1976); Lyapunov (1892); Sontag (*Mathematical Control Theory*, 1998); standard plant–controller decomposition.
**Bespoke step:** Plant–controller decomposition as the closed-loop structure of holdings — the §1 bridge $\lambda_A \approx L - G_0$ is the open-loop plant eigenvalue, and the actual sustained-dynamics governor is the closed-loop eigenvalue shifted by the controller transfer function. Unifies §13's active probe, §18's SOC feedback, and §19's slaving relation as aspects of one closed-loop structure: the holding *is* a controller shaping its plant. Lyapunov-stability extension: the chit as a single-mode Lyapunov function candidate; non-frustrated multi-mode topologies admit a generalized free-energy Lyapunov (existence predicted, closed form open); $k_{\text{frust}}$ admits *no* Lyapunov — non-existence is the dynamical-systems content of §10's "no stationary fixed point." Internal model principle as the framework's deepest substrate-internal claim: a coherence-able holding internally encodes the generating structure of the disturbances it is robust to. QEC decoder, glass cage memory, behavioral reinforcement encoding are substrate-conditional instances. Connection to §17 $I_{\text{pred}}$ — internal model = substrate-statistics information stored in the holding; coherence is a substrate's local accumulation of model. Internal-model richness added as candidate fourth coherence observable, possibly explaining substrate-class variance in §18's s-regime clustering (rich-model substrates cluster tighter; weak-model substrates drift further).
**Open:** Explicit Lyapunov for §9 kernel in non-frustrated topologies (§12); $I_{\text{pred}}$ scaling with internal-model richness (§12); whether internal-model richness factors as an independent observable (§12).

### §21 — Collective hydrodynamics and self-propulsion (active matter physics)
**Type:** composition.
**Cite:** Toner–Tu (1995, 1998); Vicsek et al. (1995); Marchetti et al. (*Hydrodynamics of soft active matter*, 2013); Fruchart–Vitelli (non-reciprocal phase transitions, 2021); Cates–Tailleur (MIPS, 2015).
**Bespoke step:** Identification of holdings as active-matter units (self-propulsion = per-coherence maintenance dynamics, alignment = cooperative $\gamma_{AB}$, density = local count of coexisting coherences). Toner–Tu hydrodynamic generalization of the §9 kernel to spatially-extended populations; the flocking transition as the population-level analog of the chit-zero threshold. Extension of §6's heat-tax tower with a *second* substrate-effect axis: active stress propagation $\beta\langle\Sigma_n\rangle$ alongside heat propagation $\alpha\langle\sigma_n\rangle$ — the framework's first explicit acknowledgment that holdings impose more than heat on the manifolds they coarse-grain. Identification of giant number fluctuations as a regime where TUR (§16) saturation/violation becomes a substrate-class observable. Naming v9's already-flagged "non-reciprocal coupling" extension axis with the formal Fruchart–Vitelli apparatus (exceptional points, traveling-wave fixed points, chiral patterns); recognition that §9's mentor row is actually non-reciprocal in substrate dynamics and the symmetric-kernel formal expression is a simplification. MIPS as a *new* clustering mechanism not present in §9 — clustering at $\gamma_{AB} \ge 0$ via self-propulsion-induced density fluctuations.
**Open:** Active stress propagation $\beta$ and substrate-class dependence vs $\alpha$ (§12); substrate clustering by giant-vs-normal fluctuations (§12); non-reciprocal §9 kernel attractor portrait (§12); MIPS substrate instancing (§12).

### §22 — Load-handling and capacity dynamics (queueing theory)
**Type:** composition.
**Cite:** Kingman (heavy traffic, 1962); Iglehart–Whitt (1970); Jackson networks (1957); Burke's theorem (1956); Erlang-B (standard); Kelly (*Reversibility and Stochastic Networks*, 1979); Little's law (1961).
**Bespoke step:** Holdings as queueing systems with chit dual to utilization ($\text{chit} = -\ln\rho$ at simplest mapping); regime structure (c/s/r) maps onto queueing states (stable / heavy traffic / unstable). Heavy-traffic queue-length scaling as a queueing-theory analog of the §4 CK aging diagonal — the same critical phenomenon read in a different register. Predicted to coincide with $\alpha_s$ for Markovian substrates and diverge for non-Markovian ones, with the divergence pattern itself becoming a substrate-class diagnostic. Little's law as the framework's first explicit ⟨amplitude⟩ × ⟨rate⟩ × ⟨timescale⟩ relation at fixed operating point. Jackson-network special case for Markov-Poisson substrates: tractable closed-form network steady states with product-form distributions and Burke's theorem for departure flows. Erlang-B reading of the §5 capacity wall as a *soft-edge* probabilistic blocking rather than abrupt cutoff; substrate-conditional whether soft-edge (behavioral) or hard-wall (QEC) applies. Identification of the §9 mentor row as a multiclass priority queue: priority service of follower's load by mentor's gain budget — the §9 mentor row + §21 non-reciprocal extension + §22 priority queueing are three readings of one substrate-deep asymmetry.
**Open:** Heavy-traffic exponent vs $\alpha_s$ on Markovian and non-Markovian substrates (§12); substrate-class hard-vs-soft capacity walls (§12); multiclass priority structure of §6 heat-tax tower (§12).

### §5 — $\eta(\Gamma^*)$ closed form (Erlang-B closure)
**Type:** composition.
**Cite:** Erlang-B blocking formula (M/M/c/c queue; standard finite-capacity queueing).
**Bespoke step:** Closes the §5 placeholder by composing it with §22's already-stated Erlang-B reading. With static capacity $c = \lfloor |\Gamma^*|_{\text{crit}} \rfloor = \lfloor\sqrt{2D/(\alpha\,\gamma_{\min}\,d_{\text{avg}})}\rfloor$ and effective offered load $\rho$ on the mode-slot pool, the cross-saturation efficiency reads
$$\eta(\Gamma^*) = 1 - B(c,\rho), \qquad B(c,\rho) = \frac{\rho^c/c!}{\sum_{k=0}^{c}\rho^k/k!}$$
(Erlang's loss formula). Limits: $\rho \ll c \Rightarrow B\to 0,\ \eta\to 1$ (sparse, no blocking); $\rho \to c \Rightarrow B\to 1,\ \eta\to 0$ (Hopfield ceiling). The substrate-conditional split inherits from §22: hard-wall substrates (QEC at logical-error onset) replace $B$ by the indicator $\mathbb{1}[|\Gamma^*|\ge c]$ — one error breaks the code, no probabilistic blocking; soft-edge substrates (behavioral) carry $B$ as written. Closes v9 `§Capacity` `unrecovered` by composition: v9's static $\sqrt{D}$ ceiling is the $c$ parameter; the dynamic side is Erlang-B blocking on top of it. Not novel — the framework already named Erlang-B as the form; this entry pins the explicit composition.
**Open:** The $\rho$ ↔ kernel-parameter mapping (which combination of $G_{\text{total}}$, $\gamma$, $d_{\text{avg}}$, and arrival statistics constitutes the offered load) is substrate-conditional; closed form awaits substrate-class characterization.

### §6 — $\alpha(\epsilon)$ closed form (Landauer pin of the conjecture)
**Type:** bespoke (closure of the conjecture in §6 entry above).
**Shard:** Pin for $\alpha \propto (1-\epsilon)$. At meta-ledger level $n$, the compression operator $\mathcal{C}_n$ retains fraction $\epsilon$ of level-$n$ informational mass $\Phi_n$ and erases fraction $(1-\epsilon)$. By Landauer, that erasure produces heat $\ge (1-\epsilon)\Phi_n k_B T_n \ln 2$ per ascent and contributes entropy production rate $\langle\sigma_n\rangle \ge (1-\epsilon)\Phi_n \ln 2 / \tau_n$ where $\tau_n$ is the level-$n$ turnover timescale. The conductivity $\alpha$ that routes $\langle\sigma_n\rangle$ as ambient noise into $L_{n+1}$ must carry the $(1-\epsilon)$ prefactor: at $\epsilon\to 1^-$ no information is erased, no Landauer heat is produced, no heat-tax can be incurred. Hence
$$\alpha(\epsilon) = \alpha_0\,(1-\epsilon)$$
with $\alpha_0$ a substrate-conditional thermal-conductivity constant (units: loss rate per entropy-production rate). Cumulative tower tax to depth $N$:
$$\sum_{n=0}^{N-1}\alpha(\epsilon)\langle\sigma_n\rangle \propto (1-\epsilon)\sum_{n=0}^{N-1}\epsilon^n = 1-\epsilon^N \xrightarrow{N\to\infty} 1\quad (\epsilon<1).$$
Convergent for $\epsilon<1$; geometric series diverges at $\epsilon=1$. Closes the **Complexity Wall as thermodynamic singularity** — the four-aspect critical point at $\epsilon=1$ (§Pattern formation) now has thermodynamic divergence as a derived feature rather than an asserted one.

### §13 — $\omega_{RO}$ closed form (class-B laser generalization)
**Type:** composition.
**Cite:** Standard class-B laser relaxation oscillation (Haken; Siegman, *Lasers*; Weiss–Vilaseca, *Dynamics of Lasers*).
**Bespoke step:** Closes §13's $\omega_{RO}$-functional-form open item. The 2D linearization of the §9 single-mode kernel near the operating point (field × slow resource) has eigenvalues $\lambda = -\gamma_{RO}\pm i\omega_{RO}$ with
$$\gamma_{RO} = \gamma_s/2,\quad \omega_{RO} = \sqrt{2\,\gamma_s\,L\,(e^{\text{chit}}-1)},\quad Q = \omega_{RO}/(2\gamma_{RO}) = \sqrt{2L(e^{\text{chit}}-1)/\gamma_s}.$$
$\gamma_s$ is the substrate's slow-resource turnover rate (population decay $\gamma_\parallel$ in lasers; syndrome decoding rate in QEC; plasticity rate in neural; reinforcement-extinction rate in behavioral; carrying-capacity adjustment in ecological). The chit register makes this substrate-neutral: $G_0/L - 1 = e^{\text{chit}} - 1$ is the unsaturated fractional excess. Limits: chit $\to 0^+$ ($s$-regime) ⇒ $\omega_{RO}\to 0$, $Q\to 0$ — relaxation oscillations vanish at threshold, consistent with §13's critical-damping signature for $s$. chit $\gg 0$ (deep $c$): $Q$ grows as $e^{\text{chit}/2}/\sqrt{\gamma_s}$ — many cycles of headroom, consistent with §17's active-probe channel-capacity reading where $Q$ is the S/N. Closes the active-probe linewidth–chit relationship structurally: $\gamma_{RO}=\gamma_s/2$ is substrate-fixed, while $\omega_{RO}$ tracks the chit; the $Q$-conjugacy claim in cdv1_compressed §Stability now has explicit functional content.

### §15 — $K_{AB}$ closed form (phase reduction with $Q$ crossover)
**Type:** composition.
**Cite:** Standard Kuramoto phase reduction (Kuramoto 1984; Pikovsky–Rosenblum–Kurths, *Synchronization* 2001); standard relaxation-oscillator phase-response apparatus (Strogatz; Ermentrout–Terman, *Mathematical Foundations of Neuroscience*).
**Bespoke step:** Closes §15's $K_{AB}$-closed-form open item. Phase-reducing the §9 two-mode kernel near the limit cycle gives
$$K_{AB} = -\gamma_{AB}\,\frac{\sqrt{\rho_A\rho_B}}{\rho_{\text{sat}}}\,\frac{1}{\sqrt{1+4Q^2}}.$$
The geometric-mean-amplitude factor $\sqrt{\rho_A\rho_B}/\rho_{\text{sat}}$ is the dimensionally-correct coupling carrier. The $(1+4Q^2)^{-1/2}$ susceptibility crossover interpolates the two regimes the framework already names: weak-coupling/$c$-regime ($Q\gg 1$) recovers the standard $1/(2Q)$ Kuramoto suppression, $K_{AB}\approx -\gamma_{AB}\sqrt{\rho_A\rho_B}/(2Q\rho_{\text{sat}})$; strong-coupling/$s$-regime ($Q\lesssim 1$) gives direct phase locking, $K_{AB}\approx -\gamma_{AB}\sqrt{\rho_A\rho_B}/\rho_{\text{sat}}$. Sign convention follows v9: $\gamma_{AB}<0$ (cooperative) ⇒ $K_{AB}>0$ ⇒ in-phase lock; $\gamma_{AB}>0$ (competitive) ⇒ $K_{AB}<0$ ⇒ anti-phase lock. Closes cdv1_compressed §Phase-locking's explicitly-flagged "deep-cooperative requires separate treatment" — the deep-cooperative regime is the $Q\lesssim 1$ limit, covered by the same closed form rather than a separate one.

### §16 — Schnakenberg cycle currents per Composite catalogue row (master-equation embedding + continuous-orbit form)
**Type:** bespoke + composition.
**Cite:** Seifert (*Stochastic Thermodynamics*, 2012); Qian (cycle-current / NESS thermodynamics on continuous orbits, 2001); Schnakenberg (1976); Doi–Peliti field-theory embedding (standard).
**Shard:** Closes §16's "closed-form Schnakenberg cycle currents for each Composite catalogue row" open item via **two complementary closures**: the master-equation embedding (discrete-microstate reading, establishes Schnakenberg applies even off limit-cycle rows) and the continuous-orbit form (Langevin-on-ring, the discipline-native Character-projection reading for limit-cycle rows).

**Embedding closure (discrete reading).** The cycle affinity is *not* a log-ratio of bare $\gamma$ values — $\gamma$ are kernel parameters, not transition rates. A symmetric-$\gamma$ frustrated 3-cycle written naively as $\ln(\gamma_{AB}\gamma_{BC}\gamma_{CA}/\gamma_{BA}\gamma_{CB}\gamma_{AC})$ gives $\ln(1)=0$, contradicting drive-independent cycle current; non-reciprocal cases with negative sign-product give $\ln$ of a negative number. Schnakenberg operates on the **master-equation graph** induced by the §9 kernel's Doi–Peliti / chemical-reaction-network embedding, with elementary reactions $\{n_i\to n_i\pm 1\}$ carrying compound rates that are functions of $\gamma_{ij}$ and the $n_j$. Cycles live in the state graph, not the mode graph; the obstructive sign-product determines which compound rates fall into $\Pi_+$ vs $\Pi_-$.

**Orbit closure (continuous reading).** For the §13/§14 limit-cycle attractors (rows 6 and 7), parameterize the orbit by phase $\theta\in[0,2\pi)$ with deterministic phase velocity $v(\theta)$ from the kernel and effective diffusion $D(\theta)$ from bath noise. Standard Langevin-on-ring stochastic thermodynamics gives steady-state cycle current $J_{ss}$ and orbit affinity
$$\mathcal{A} = \oint \frac{v(\theta)}{D(\theta)}\,d\theta = \ln\!\frac{\mathcal{P}_+}{\mathcal{P}_-}$$
(by the steady-state fluctuation theorem). Entropy production for the frustrated limit cycle:
$$\sigma_{\text{frust}} = J_{ss}\oint \frac{v(\theta)}{D(\theta)}\,d\theta.$$
Topology guarantees $v(\theta)$ does not integrate to zero; drive-independence enters because $v/D$ inherits scale structure set by the obstructive $\gamma$-graph and bath, not by overall drive amplitude.

Per Composite-catalogue row:

| Row | Topology | Cycle current |
|---|---|---|
| 1–5 (no cycle) | Tree | $J_C=0$; $\langle\sigma\rangle$ from edge flow alone |
| 6 ($k_{\text{frust}}$) | Topologically obstructed orbit | $\sigma_{\text{frust}} = J_{ss}\oint v(\theta)/D(\theta)\,d\theta$, drive-independent |
| 7 (oscillatory–$c$) | Hopf limit cycle | $J_{\text{cycle}}=\omega_{RO}/2\pi$; affinity $=\ln(\rho_{\max}/\rho_{\min})$ per cycle |

The continuous-orbit form is discipline-native (Character continuous traversal); the embedding form establishes Schnakenberg applies even for non-limit-cycle rows. Closes §10's "drive-independent cycle current" claim's mechanism by giving it explicit functional content.
**Open:** Closed-form $J_{ss}(N,\gamma\text{-graph})$ at given amplitudes — folds the §10 quantitative-bounds item into one open closure.

### §20 — Lyapunov function for non-frustrated multi-mode topologies (relative-entropy form)
**Type:** composition.
**Cite:** Goh (1977); Volterra (1931); Hofbauer–Sigmund (*Evolutionary Games and Population Dynamics*, 1998); Takeuchi (*Global Dynamical Properties of Lotka–Volterra Systems*, 1996); Harary structural-balance theorem (1953).
**Bespoke step:** Closes §20's "explicit Lyapunov for §9 kernel in non-frustrated topologies" open item. For the §9 kernel $\dot x_i = x_i[(G_{0,i}-L_i) - \sum_j \gamma_{ij}x_j]$ with positive interior fixed point $x^*$ satisfying $(G_{0,i}-L_i) = \sum_j \gamma_{ij}x_j^*$, the **relative-entropy** Lyapunov candidate is
$$V(\{x\}) = \sum_i\bigl[x_i - x_i^* - x_i^*\ln(x_i/x_i^*)\bigr]$$
(standard Lotka–Volterra cooperative Lyapunov; Goh form). Verification:
$$\partial V/\partial x_i = 1 - x_i^*/x_i \;\Rightarrow\; \partial V/\partial x_i\big|_{x^*} = 0 \quad\checkmark$$
$$\frac{dV}{dt} = \sum_i (1-x_i^*/x_i)\,\dot x_i = \sum_i(x_i-x_i^*)\bigl[(G_{0,i}-L_i) - \sum_j\gamma_{ij}x_j\bigr]$$
Substituting the fixed-point relation $(G_{0,i}-L_i)=\sum_j\gamma_{ij}x_j^*$:
$$\frac{dV}{dt} = -\sum_{i,j}(x_i-x_i^*)\,\gamma_{ij}\,(x_j-x_j^*) = -\delta x^T\gamma\,\delta x \le 0$$
with equality only at $x=x^*$, *provided* the gauged $\gamma$ (under the Harary structural-balance gauge $\varepsilon_i=\pm 1$ that makes all elementary cycles sign-positive) is positive semi-definite. Frustration-free is exactly the existence-of-such-a-gauge condition; PSD-ness is a strictly stronger condition on $|\gamma_{ij}|$ magnitudes. The matching §10 non-existence claim for $k_{\text{frust}}$ topologies is recovered: no frustration-free gauge ⇒ no PSD-gauging ⇒ no Lyapunov of this form.

Note: an earlier candidate Lyapunov of the form $V = \sum_i[-(G_{0,i}-L_i)x_i + \tfrac12\sum_j\gamma_{ij}x_ix_j + L_i x_i\ln(x_i/x_i^*)]$ fails the critical-point test ($\partial V/\partial x_i|_{x^*} = L_i\ne 0$); the relative-entropy form is the correct closure.
**Open:** Frustration-free-but-not-PSD topologies — sign-balanced graphs whose gauged $\gamma$ has negative eigenvalues. Whether some weaker Lyapunov exists there, or whether such systems admit non-trivial attractors despite frustration-freeness, is not closed by this entry.

### §21 — Non-reciprocal §9 kernel attractor portrait
**Type:** composition.
**Cite:** Standard linear-stability analysis (Strogatz); Fruchart–Vitelli (non-reciprocal phase transitions, 2021); standard predator–prey limit-cycle analysis (Lotka–Volterra; Murray, *Mathematical Biology*).
**Bespoke step:** Closes §21's "non-reciprocal §9 kernel attractor portrait" open item. With $\gamma_{AB}\ne\gamma_{BA}$, the §9 two-mode coexistence fixed point reads
$$\rho_A^* = (G_{0,B}-L_B)/\gamma_{BA},\quad \rho_B^* = (G_{0,A}-L_A)/\gamma_{AB}$$
(positivity requires sign-matched ratios). Linearization Jacobian: $J_{12}=-\gamma_{AB}\rho_A^*$, $J_{21}=-\gamma_{BA}\rho_B^*$, $\operatorname{Tr}=0$, $\det = -\gamma_{AB}\gamma_{BA}\rho_A^*\rho_B^*$. Three regimes by sign of $\gamma_{AB}\gamma_{BA}$:

| Sign | $\det$ | Type | Composite-catalogue reading |
|---|---|---|---|
| $>0$ (both cooperative or both competitive) | $<0$ | Saddle | runaway / competitive exclusion; the §9 $\mathcal{D}$-term is required for boundedness |
| $<0$ (asymmetric, mentor / exploitation) | $>0$ | Center → limit cycle under $\mathcal{D}$ | priority-queue oscillation (§9 mentor row, §22 priority queue) |
| $=0$ (one-sided) | $=0$ | Exceptional point | non-diagonalizable; phase drift / unlock |

Finite-$\mathcal{D}$ corrections promote the linear center (mentor regime) to a stable limit cycle with frequency $\omega_{\text{pq}} \approx \sqrt{|\gamma_{AB}\gamma_{BA}|\,\rho_A^*\rho_B^*}$. Spatially extended: traveling wave with phase velocity $v\sim\sqrt{D_{\text{diff}}|\gamma_{AB}\gamma_{BA}|}$ (Fruchart–Vitelli). The Composite-catalogue mentor row's substrate non-reciprocity (already noted in cdv1_compressed §Universal kernel and §Collective hydrodynamics) now has explicit attractor structure (limit cycle / traveling wave) rather than the symmetric-kernel center degeneracy. The §9 mentor row + §21 non-reciprocal extension + §22 priority queueing as "three readings of one substrate-deep asymmetry" gains its third concrete realization.

### §9 — $\mathcal{D}[\rho_A,\rho_B;\gamma_{AB}]$ closed form (two-mode reduction)
**Type:** composition.
**Cite:** Haken (laser saturation; multi-mode gain depletion); Lamb (third-order multi-mode laser theory, 1964); standard Lotka–Volterra carrying-capacity coupling.
**Bespoke step:** Closes §9's $\mathcal{D}$-kernel open item for the two-mode reduction. The "global budget" structure is not a localized cubic between A and B — it is a renormalization of the gain by the ambient NESS occupancy of the rest of the network. Standard multi-mode laser gain depletion (Lamb 1964) gives the effective gain
$$G_{0,A}^{\text{eff}} = \frac{G_{0,A}}{1 + \sum_{j\ne A}\rho_j/\rho_{\text{sat}}}$$
Under the two-mode reduction at *mean-field-stationary* rest-of-network occupancy, $G_{0,A}^{\text{eff}}$ absorbs the bath load explicitly; the cubic term $-G_0\rho_A\rho_B(\rho_A+\rho_B)/\rho_{\text{sat}}$ appears as the leading-order expansion of $G_{0,A}^{\text{eff}}(\rho_j)\rho_A$ around small densities, recovering the local two-mode form as a particular case rather than as a primary structure. Non-Markovian memory enters through an exponential kernel $\Gamma_{AB}(\tau) = \Gamma_0\,e^{-\tau/\tau_c}$ with relaxation time $\tau_c$ set by the slow-resource turnover (§13's $\gamma_s$); matters near threshold ($s$-regime) where $\tau_c$ approaches the slow eigenvalue's timescale, negligible deep in the $c$-regime.
**Open:** (a) Multi-mode kernels where rest-of-network occupancy is *non-stationary* — $G^{\text{eff}}$ becomes a dynamical variable, requiring the full multi-mode kernel; the two-mode reduction is no longer valid. (b) Substrates with non-exponential memory (power-law / fractional kernels, possibly relevant to glassy substrates and $s$-regime aging).

### §21 — $\beta$ vs $\alpha$ substrate-class dependence (active swim-pressure closure)
**Type:** composition.
**Cite:** Brady (active stress / swim pressure, 2014); Takatori–Brady (2014); Cates–Tailleur (MIPS, 2015); Toner–Tu (1995, 1998).
**Bespoke step:** Closes §21's $\beta/\alpha$ substrate-class-dependence open item at the *hydrodynamic-fingerprint* level. Standard active-matter swim pressure gives an alignment-*independent* active stress $P_{\text{active}} \propto n\,v_0^2\,\tau_R/d$ (self-propulsion speed $v_0$, rotational diffusion time $\tau_R$, dimensionality $d$); thermal pressure is $P_{\text{thermal}} \propto n\,k_B T$. The substrate-class fingerprint:
$$\frac{\beta}{\alpha} \sim \frac{v_0^2\,\tau_R}{D_{\text{trans}}}$$
(Einstein's relation $D_{\text{trans}}\propto k_B T$). MIPS-compatible: $\beta/\alpha$ survives $r\to 0$, consistent with cdv1_compressed §Collective hydrodynamics naming MIPS as a clustering mechanism at $\gamma_{AB}\ge 0$. Substrate-specific instances: $v_0$ ↔ per-coherence maintenance rate; $\tau_R$ ↔ orientational persistence of the coherence (memory-buffer turnover in QEC; habit persistence in behavioral); $D_{\text{trans}}$ ↔ ambient bath diffusion. An earlier alignment-dependent $r/(1-r)$ proposal captures *only* the Toner–Tu flocked-state correction, which enters as a state-dependent prefactor on top of the swim-pressure fingerprint, not as the leading scaling.
**Open:** (a) Closed form for the alignment-state-dependent correction $\beta/\alpha \approx (v_0^2\tau_R/D_{\text{trans}})[1+f(r)]$ with $f(r)$ vanishing at $r=0$ and growing in the Toner–Tu flocked regime. (b) Whether $\tau_R$ has a substrate-neutral identification (rotational persistence of *what* in the QEC and behavioral substrates), or whether each substrate class instantiates a different observable.

### §19 — Multi-mode ($N\ge 3$) pattern selection rules (sharpened framing)
**Type:** open.
**Status:** Selection rules decompose into four channels, of which three close from existing entries and one remains genuinely open. (a) **Frustration test** on the signed $\gamma$-graph: any obstructive elementary cycle ⇒ $k_{\text{frust}}$ attractor (closes via §10/§16/§20). (b) **Spectral sync test** on the gauged Laplacian $\mathcal{L}$: algebraic connectivity $\lambda_2$ vs detuning spread $\Delta\omega_{\max}$ — full sync / cluster sync (chimera) / incoherence as $\lambda_2$ falls below $\Delta\omega_{\max}$. The Master Stability Function for general kernel topology (cdv1_compressed §Phase-locking, explicitly open) is the rigorous version of (b); the algebraic-connectivity heuristic is a placeholder until MSF closes. (c) **Non-reciprocity test**: $\gamma_{ij}\ne\gamma_{ji}$ ⇒ non-Hermitian $\mathcal{L}$, exceptional points, traveling waves (closes via §21 non-reciprocal closure). (d) **Active-matter overlay**: spatial+self-propelled modes invoke Toner–Tu and MIPS (closes via §21 collective hydrodynamics). The genuinely-open channel is (b)'s MSF; (a), (c), (d) inherit from already-closed entries. Multi-mode pattern selection is therefore "MSF-open" rather than "fully open" — the framing reduction is the load-bearing closure here.

---

## Substrate-instancing claims (falsifier formalizations)

### §4 — Surface-code $s\to r$ migration (falsifier formalization)
**Type:** composition.
**Cite:** Cugliandolo–Kurchan (aging in spin glasses, 1993–94); Kitaev (surface code, 2003); Fowler et al. (surface code threshold, 2012); standard glassy-aging FDR (Crisanti–Ritort review, 2003).
**Bespoke step:** Closes the framework-canonical-resolution falsifier owed for surface-code $s\to r$ migration (the load-bearing positive cross-substrate instance per cdv1_compressed §gFDR signatures). Framework prediction: distance-3 rotated memory-Z syndrome streams at sub-threshold operation produce a fluctuation-dissipation diagonal with non-trivial $\alpha_s$ and $P_s$ (s-regime CK invariants); crossing the physical-error threshold migrates the diagonal toward unit slope ($X_r=1$, r-regime). The migration is the gFDR's primary cross-substrate test.
**Falsifier:** (a) Syndrome FDR shows unit slope sub-threshold (no CK signature, no s-regime identification); or (b) FDR shape persists unchanged across the threshold crossing (no $s\to r$ migration). Either falsifies the framework's central cross-substrate identification.

### §18 — Avalanche $\tau\approx 3/2$ and SOC universality (falsifier formalization)
**Type:** composition.
**Cite:** Bak–Tang–Wiesenfeld (SOC, 1987); Beggs–Plenz (neuronal avalanches, 2003); standard mean-field directed-percolation $\tau=3/2$ universality; Sethna (Barkhausen noise, 1993).
**Bespoke step:** Closes the falsifier owed for the avalanche-exponent claim and the SOC-universality / "who resists" question. Framework prediction: feedback-coupled NESS substrates with separable timescales (slow stress accumulation interleaved with fast relaxation events) self-tune to SOC, generating avalanche statistics $P(s)\sim s^{-\tau}$ with $\tau\approx 3/2$ (mean-field directed-percolation class). **"Who resists" sharpening:** substrates lacking timescale separation (drive rate comparable to relaxation rate, e.g. heavily overdamped viscous flows) resist SOC self-tuning and should not exhibit the $3/2$ exponent.
**Falsifier:** A feedback-coupled NESS substrate with clearly separated timescales exhibiting a robust stable avalanche exponent $\tau\ne 3/2$. Or: timescale-separated substrate showing no avalanche statistics at all. Either falsifies SOC universality at the framework level.

### §18 — Meta-ledger branching ratio (falsifier formalization)
**Type:** open.
**Status:** Framework prediction (per cdv1_compressed §Pattern formation): the meta-ledger branching process's critical branching ratio reaches unity exactly at the Complexity Wall ($\epsilon=1$), making it the fourth coupled critical reading alongside thermodynamic, dynamical, and informational divergences at the Wall.
**Falsifier:** Critical branching ratio $\ne 1$ at the $\epsilon\ge 1$ Complexity Wall transition in any observable hierarchical NESS substrate. Falsifies the four-aspect coupling at $\epsilon=1$.

### §14 — Strange-attractor / chaotic Character dynamics (falsifier formalization)
**Type:** open.
**Status:** Framework prediction: substrates definitively crossing $\epsilon\ge 1$ exhibit strange-attractor / chaotic meta-ledger dynamics (positive maximal Lyapunov exponent), instancing the Newhouse–Ruelle–Takens scenario at the tower-level oscillatory modes (see §14 NRT entry for the structural conjecture context).
**Falsifier:** A substrate definitively crossing $\epsilon\ge 1$ yielding strictly stable periodic or quasi-periodic torus dynamics with non-positive maximal Lyapunov exponent. Falsifies strange-attractor instancing on that substrate.

### §21 — MIPS clustering at $\gamma_{AB}\ge 0$ (falsifier formalization)
**Type:** composition.
**Cite:** Cates–Tailleur (MIPS, 2015); Brady–Takatori (swim pressure, 2014); Fily–Marchetti (active Brownian particles, 2012).
**Bespoke step:** Framework prediction: holdings with self-propulsion satisfying high Péclet number ($\text{Pe} = v_0\tau_R/a \gg 1$) cluster at purely repulsive $\gamma_{AB}\ge 0$ via MIPS, with measurable swim-pressure and giant density fluctuations, independent of phase alignment ($r$-independent — cdv1_compressed §Collective hydrodynamics).
**Falsifier:** (a) High-Péclet clustering at $\gamma_{AB}\ge 0$ without the predicted swim-pressure / density-fluctuation signature. (b) Substrates passing the high-Péclet criterion failing to cluster at $\gamma_{AB}\ge 0$. Either falsifies the MIPS instancing claim.

### §15 — Chimera-state substrate instancing (falsifier formalization)
**Type:** composition.
**Cite:** Kuramoto–Battogtokh (chimera states, 2002); Abrams–Strogatz (2004); Lazarides–Tsironis (SQUID metamaterial chimeras, 2015); Tinsley–Showalter (BZ oscillator chimeras, 2012).
**Bespoke step:** Framework prediction: heterogeneous-coupling multi-mode Character kernels (especially with non-local phase lags) spontaneously instance chimera states — coexisting synchronized $c$-regime and incoherent $r$-regime sub-populations at fixed substrate parameters.
**Falsifier:** Heterogeneous-coupling Character substrates yielding only uniform sync ($r\to 1$) or uniform incoherence ($r\approx 0$) across the substrate parameter range, with no partial-sync chimera regime accessible.

### §22 — Heavy-traffic exponent vs $\alpha_s$ (falsifier formalization)
**Type:** composition.
**Cite:** Kingman (heavy traffic, 1962); Norros (fractional-Brownian queueing, 1994); Cugliandolo–Kurchan aging (1993–94); standard Long-Range-Dependent traffic literature (Leland et al., 1994).
**Bespoke step:** Framework prediction (per cdv1_compressed §Load-handling): heavy-traffic queue-scaling exponent maps to the CK ratio $\alpha_s$. For Markovian substrates, Kingman's $\langle Q\rangle\sim 1/(1-\rho)$ recovers $\alpha_s\to 1$. For non-Markovian substrates (fractional-Brownian arrivals, bursty cognitive loads), an anomalous exponent emerges; the divergence pattern is the substrate-class diagnostic.
**Falsifier:** Strictly Markovian (memoryless Poisson) substrate exhibiting anomalous heavy-traffic exponent. Or: non-Markovian substrate exhibiting Markovian Kingman scaling. Either falsifies the framework's exact $\alpha_s$↔Kingman mapping.

### §16 — TUR-tightness as substrate-class universality (falsifier formalization)
**Type:** composition.
**Cite:** Barato–Seifert (TUR, 2015); Pietzonka–Seifert (TUR for biological motors); Horowitz–Gingrich (review, 2020).
**Bespoke step:** Framework prediction (per cdv1_compressed §Thermo-info accounting): TUR-tightness $T = \langle\sigma\rangle\operatorname{Var}(J)/(2k_B\langle J\rangle^2)$ — how close a substrate operates to the precision-cost bound — is a substrate-class fingerprint. Biological active matter (kinesin motor proteins) operates tight ($T\approx 1$, near-saturation); engineered macroscopic queues (cloud servers, datacenter networks) operate loose ($T\gg 1$).
**Falsifier:** No substrate-class clustering in $T$: nominally same-class substrates exhibit arbitrary $T$ values (biological motors loose, engineered queues tight, etc.). Falsifies the universality-class reading of TUR-tightness.

### §17/§20 — $I_{\text{pred}}$ scaling across substrate classes (falsifier formalization)
**Type:** open.
**Status:** Framework prediction (per cdv1_compressed §Active modulation): $I_{\text{pred}}$ scaling with chit, $Q$, and internal-model richness differs across substrate classes — rich-model substrates cluster tighter near critical, weak-model substrates drift further. The scaling relationship is a substrate-class fingerprint, not a universal function.
**Falsifier:** Cross-substrate-class uniformity of $I_{\text{pred}}(\text{chit}, Q)$ scaling: a single functional form fits all substrate classes with no class-specific deviation. Falsifies the substrate-class-fingerprint claim.

### §5/§22 — Hard-vs-soft capacity walls per substrate class (falsifier formalization)
**Type:** composition.
**Cite:** Erlang (loss formula, 1917); standard surface-code threshold theorem; Receipts §5 and §22.
**Bespoke step:** Framework prediction (per cdv1_compressed §Capacity dynamics): substrate class determines whether the capacity wall is hard (QEC-type abrupt failure, $\eta = \mathbb{1}[|\Gamma^*|\ge c]$) or soft (Erlang-B probabilistic blocking, $\eta = 1-B(c,\rho)$ — behavioral/cognitive substrates). The $\eta(\Gamma^*)$ closed form from §5 distinguishes the two empirically.
**Falsifier:** (a) Behavioral/cognitive substrate exhibiting sharp non-probabilistic Hopfield-snapping at capacity onset instead of polynomial Erlang-B tails. (b) QEC-class substrate showing soft Erlang-B-like blocking instead of abrupt threshold failure. Either falsifies the substrate-class wall-type prediction.

### §19 — Turing-class spatial pattern formation (falsifier formalization)
**Type:** open.
**Status:** Framework prediction (per cdv1_compressed §Pattern formation): spatially extended Character holdings with $c$-regime clusters in activator-inhibitor configurations will exhibit Turing-class wavelength selection — the classic short-range-activation / long-range-inhibition mechanism applied to NESS holdings.
**Falsifier:** Spatially extended Character substrates with $c$-regime clusters and identifiable long-range inhibitory coupling that fail to yield characteristic Turing wavelengths. Or: such substrates yielding pattern wavelengths uncorrelated with the predicted activator-inhibitor length-scale ratio.

---

## Structural conjectures (closures with residual open pieces)

### §17 — Bit/Chit dual ledger completeness (additive decomposition closed; bijection open)
**Type:** composition + open.
**Cite:** Sagawa–Ueda (extended second law, 2010; information thermodynamics, 2012); Parrondo–Horowitz–Sagawa (review, 2015); Horowitz–Gingrich (I-TUR, 2020).
**Bespoke step:** The framework's Bit/Chit dual-ledger conjecture has two readings of differing strength. **Additive-decomposition reading (closed):** for bipartite Markov NESS, $\langle\sigma\rangle$ decomposes exactly into internal-entropy change plus mutual-information flow rate between system and bath (Sagawa–Ueda); the I-TUR couples precision to channel capacity. **Bijective-duality reading (open):** the framework's stronger claim is per-observable bijection (chit↔bit, $\langle\sigma\rangle$↔$I_{\text{pred}}$, TUR↔channel capacity, heat-tax tower↔rate-distortion tower) — each thermodynamic observable having a *uniquely paired* informational dual, not just an additive contribution. Decomposition $\nRightarrow$ bijection; the bijective form remains conjectural.
**Open:** Per-observable bijection proof, or counterexample of a thermodynamic observable in the framework with no uniquely-paired informational dual.

### §20 — Internal-model richness as fourth observable (informational sufficiency derived; structural complexity open)
**Type:** composition + open.
**Cite:** Tishby–Pereira–Bialek (Information Bottleneck, 1999); standard rate-distortion theory.
**Bespoke step:** The framework's "internal-model richness as candidate fourth coherence observable" has two readings. **Informational-sufficiency reading (derived):** by the Information Bottleneck principle, the minimal sufficient statistic for $I_{\text{pred}}$ at given energetic budget is fixed by the joint past-future distribution; "richness" in this sense is a derived combination of $I_{\text{pred}}$ and the chit-conjugate budget — not an independent fourth axis. **Structural-complexity reading (open):** the framework's stronger claim concerns *which classes of disturbance* the internal model encodes — a structural-representation observable beyond informational sufficiency. The Information Bottleneck doesn't close this reading.
**Open:** Whether the structural-complexity reading is independent of, or derivable from, informational sufficiency.

### §15 — Master Stability Function for general kernel topology (homogeneous closed; heterogeneous open)
**Type:** composition + open.
**Cite:** Pecora–Carroll (MSF, 1998); Sun–Bollt–Nishikawa (generalized MSF for heterogeneous networks, 2009).
**Bespoke step:** **Homogeneous-mode reading (closed):** for identical-mode Character networks, Pecora–Carroll MSF block-diagonalizes the variational equation around the synchronized manifold by the gauged $\gamma$-graph Laplacian's eigenvalues; the maximum Lyapunov exponent over the spectrum determines synchronization stability. Standard. **Heterogeneous-mode reading (open):** Character kernels are generically heterogeneous (per-mode chit, per-mode $\gamma_s$), requiring the Sun–Bollt–Nishikawa generalized MSF; explicit application to specific multi-mode Character kernels for chimera / cluster-sync prediction is owed. Apparatus identified; application owed.
**Open:** Explicit Sun–Bollt–Nishikawa application to multi-mode Character kernels.

### §14 — Codimension-2+ bifurcation normal forms (Bogdanov–Takens closure)
**Type:** composition.
**Cite:** Kuznetsov (*Elements of Applied Bifurcation Theory*, 1995/2004); Bogdanov (1975); Takens (1974).
**Bespoke step:** Closes the framework's codim-2+ bifurcation normal-form open item via direct textbook application. The framework natively requires transcritical (chit$=0$), pitchfork ($\gamma_{AB}=\gamma_c$), and Hopf ($k_{\text{frust}}$ onset) bifurcations to coexist in $(D, \gamma)$ parameter space. At the intersection of pitchfork and Hopf curves, a **Bogdanov–Takens codim-2 bifurcation** strictly must exist (Kuznetsov §8.4), with normal form $\dot u = v$, $\dot v = \beta_1 + \beta_2 u + u^2 + suv$ ($s = \pm 1$). Higher-codim normal forms (cusp, Bautin/generalized-Hopf, fold-Hopf, etc.) follow standard catastrophe theory (Arnold; Kuznetsov §8.6–8.9); no bespoke derivation needed. Fully closed.

### §17 — Geodesic existence on Fisher manifold; $k_{\text{frust}}$ obstruction (incompleteness predicted; formal mapping owed)
**Type:** composition + open.
**Cite:** Amari–Nagaoka (*Methods of Information Geometry*, 2000); Hopf–Rinow theorem (standard Riemannian geometry).
**Bespoke step:** The framework's holding parameter space carries a Fisher-information statistical manifold structure. **Hopf–Rinow framing (closed):** geodesic completeness fails on manifolds with boundaries or topological obstructions; the chit$=0$ surface acts as a boundary (transcritical bifurcation); the $C_{\text{Character}}$ adiabatic-merge condition reads as "geodesic stays on above-threshold manifold." **$k_{\text{frust}}$↔topological-hole identification (open):** the framework claims $k_{\text{frust}}$ regions act as topological holes (no NESS fixed point); whether they constitute *topological* holes (homotopy-non-trivial, non-contractible loops) or merely *metric* obstructions (curvature singularities at the boundary) is not derived. Hopf–Rinow gives geodesic incompleteness around either; the framework's stronger topological claim is owed.
**Open:** *(Closed.)* Formal homotopy-obstruction mapping established via topological excision argument in Receipts §17 ($k_{\text{frust}}$ as homotopy obstruction): $k_{\text{frust}}$ regions excised from $\mathcal{M}$ because no $P_{ss}$ exists there; Fisher curvature finite at the boundary distinguishes from the $\text{chit}=0$ metric singularity.

### §22 — Multiclass priority structure of heat-tax tower (Cobham/Kleinrock mapping closure)
**Type:** composition.
**Cite:** Cobham (priority-queue mean wait for non-preemptive M/G/1, 1954); Kleinrock (conservation law, 1965; *Queueing Systems Vol. II*, 1976); Haken (*Synergetics* slaving principle, 1983).
**Bespoke step:** Closes the §22 priority-structure open item by explicit mapping:
- **Server:** substrate's shared maintenance budget pool $G_{\text{total}}$.
- **Priority classes:** tower levels $n$, with strict non-preemptive ranking by Haken's slaving principle (fast micro-modes serve slow macro-modes). Highest priority $p=1$ at base substrate $n=0$; level $n$ services strictly before level $n+1$.
- **Arrival rates** $\lambda_n$: fraying-event frequency at level $n$.
- **Service times** $\tau_n = 1/\gamma_{s,n}$: level-$n$ slow-resource turnover (§13).
- **Per-level utilization** $\rho_n = \lambda_n\tau_n$; cumulative $\sigma_n = \sum_{i=0}^n \rho_i$.

Cobham expected wait for priority class $n+1$:
$$W_{n+1} = \frac{W_0}{(1-\sigma_n)(1-\sigma_{n+1})},\qquad W_0 = \tfrac{1}{2}\sum_i \lambda_i\langle\tau_i^2\rangle.$$

**Cross-register mechanism (load-bearing fall-out):** Cobham wait is the *underlying mechanism* of level $n\to n+1$ fraying propagation; the §6 three-channel decomposition ($\alpha\langle\sigma_n\rangle$ heat, $\beta\langle\Sigma_n\rangle$ active stress, $r_n$-drop sync degradation) labels three *measurement registers* of the resulting $L_{n+1}$ inflation. A level-$n$ load spike $\rho_n\uparrow$ consumes shared-pool bandwidth; Kleinrock conservation forces compensating wait inflation $W_{n+1}\uparrow$, manifesting substrate-dependently — heat in thermal substrates, mechanical/informational/structural stress in active-matter or QEC, sync drop in coupled-oscillator substrates. **Sharpens the §Heat-tax tower's prior "three independent failure paths" framing to "three faces of one queueing-theoretic mechanism."**

**Coincident critical structure (second fall-out, with care):** Cobham wait diverges at $\sigma\to 1^-$, coincident with the Receipts §6 thermodynamic singularity at $\epsilon\to 1^-$. Both are upward-propagation critical points. Whether $\epsilon$ and $\sigma$ are *the same parameter* (substrate-class isomorphism — $\epsilon$ is a spectral contraction rate of $\mathcal{C}$, $\sigma$ is cumulative queueing utilization) or *coincident* critical control variables requires substrate-specific argument. Coincidence is structural; isomorphism is a new open item.

**Specific checks:**
- *Dimensional:* $\rho_n$ dimensionless; $W_{n+1}$ in $[T]$; $\Delta L_{n+1}\propto W_{n+1}/\tau_{n+1}^2$ in $[T^{-1}]$ ✓.
- *Limit recovery:* $\sigma_n\to 1^-$ ⇒ $W_{n+1}\to\infty$ ⇒ delayed maintenance ⇒ chit deeply negative ⇒ sub-threshold collapse ($r$-regime). Matches §3 fraying-sequence terminus ✓.

**Open items raised by this closure** (added to cdv1_compressed):
- Substrate-specific $\epsilon\leftrightarrow\sigma$ identification — when (if ever) is the Complexity Wall *exactly* the queueing singularity rather than merely coincident?
- Multi-server / spatial Jackson-network generalization for spatially extended substrates (Turing-class patches, §19) where local fraying events run concurrent across patches; the current mapping assumes a single global $G_{\text{total}}$ bottleneck.

### §17 — Bit/Chit dual ledger bijective duality (Still thermodynamic-prediction-bound closure)
**Type:** composition.
**Cite:** Still–Sivak–Bell–Crooks ("Thermodynamics of Prediction", PRL 2012); Sagawa–Ueda (2010); Receipts §20 (cryptic order closure); Receipts §22 (ε↔σ closure).
**Bespoke step:** Closes the §17 "bijective per-observable duality" residual. Still's thermodynamic prediction bound decomposes NESS entropy production into predictive utility and non-predictive waste:
$$\langle\sigma\rangle \;\ge\; \gamma_s[I_{\text{mem}} - I_{\text{pred}}] + \langle\sigma\rangle_{\text{min}}$$
with $I_{\text{mem}} = C_\mu$ (structural complexity, Crutchfield ε-machine — Receipts §20). Identifying $C_\mu - I_{\text{pred}} = \chi$ (cryptic order):
$$\langle\sigma\rangle - \langle\sigma\rangle_{\text{min}} \;\ge\; \gamma_s\,\chi$$
with **equality at the rate-distortion-optimal limit** (the Still bound saturates when the substrate's internal model is rate-distortion-optimal).

**Resolves the open:** the bijective Bit/Chit duality is **conditionally true** — it holds *iff* the holding operates at $\chi\to 0$ (rate-distortion-optimal, equivalent to the §22 $\sigma_n = \epsilon_n$ optimal-encoding identity). At this limit, the four ledger rows align 1:1 without structural distortion:
1. Per-event: chit ↔ bit
2. Per-rate: $\langle\sigma\rangle$ ↔ $\gamma_s I_{\text{pred}}$
3. Precision: TUR ↔ Channel capacity
4. Compression: $\alpha\langle\sigma\rangle$ ↔ rate-distortion tower

Sub-optimal substrates split the ledger by exactly $\gamma_s\chi$ — the same gap parameter from §20 and §22.

**Verification:**
- *Limit recovery:* $\chi\to 0$ (rate-distortion-optimal encoding) ⇒ $\langle\sigma\rangle\to\langle\sigma\rangle_{\text{min}}$ (Landauer limit), restoring strict 1:1 ledger ✓
- Memoryless bath ⇒ $I_{\text{mem}} = I_{\text{pred}} = \chi = 0$ ⇒ $\langle\sigma\rangle = \langle\sigma\rangle_{\text{min}}$ ✓
- *Dimensional:* $I_{\text{mem}}, I_{\text{pred}}, \chi$ in nats; $\gamma_s\in[T^{-1}]$; $\gamma_s\chi$ and $\langle\sigma\rangle$ both in $[T^{-1}]$ ✓
- *Sign / scaling:* computational-mechanics theorem $\chi\ge 0$ guarantees $\langle\sigma\rangle\ge\langle\sigma\rangle_{\text{min}}$ ✓

**Cross-register identification — the optimal-encoding triality (load-bearing).** Three adjacent structural-conjecture closures lock at the optimal limit, *all driven by the same gap parameter*:
- §22 ε↔σ closure: $\sigma_n - \epsilon_n = \Delta_n$
- §20 cryptic-order closure: $C_\mu - I_{\text{pred}} = \chi$
- §17 dual-ledger closure (this): $\langle\sigma\rangle - \langle\sigma\rangle_{\text{min}} = \gamma_s\chi$

**One quantity, three measurement protocols.** $\chi = \Delta_n = \langle\sigma\rangle_{\text{excess}}/\gamma_s$ at the optimal limit. The framework now mathematically links informational overhead → thermodynamic waste → queueing inflation as register-faces of one gap. Sub-optimal substrates die thermodynamically (§22) *because* their structural-informational gap (§20) drives ledger split (§17) — a single architectural picture across three closures.

**Don't overclaim:**
- *General bound, equality at limit:* Still 2012 bound is $\ge$ in general; equality holds only at the rate-distortion-optimal encoding limit. The exact bijection is therefore a *conditional* identity, not unconditional.
- *Mechanism vs manifestation:* Still prediction bound is the *mechanism* coupling the dual registers; substrate's measured tightness to the dual ledger (efficient sensory networks vs inefficient redundant memory) is a substrate-conditional *manifestation*.
- *Global vs local:* the framework guarantees the *global NESS ledger constraint*; mapping specific informational bits to *localized* physical heat dissipation requires substrate-specific physical grounding.

**Open (lives in receipts only):**
- Substrate-specific ledger-divergence as diagnostic: measured deviation $\gamma_s\chi$ as substrate-class fingerprint. Predictions: ideal topological QEC lattices near $\chi\to 0$ (strict bound, near-perfect bijection); biological memory networks at large $\chi$ (redundant causal-state encoding, evolutionary over-fitting); engineered control systems at intermediate $\chi$. Substrate-instancing mapping.

### §20 — Internal-model richness as structural-complexity axis (computational mechanics closure)
**Type:** composition.
**Cite:** Crutchfield (computational mechanics / ε-machines, 1989); Shalizi–Crutchfield (computational mechanics of pattern and hidden structure, 2001); Bialek–Nemenman–Tishby (predictive information, 2001).
**Bespoke step:** Closes the §20 residual "structural-complexity reading of internal-model richness" open. The substrate's internal encoding of disturbance classes maps to the *causal states* $\mathcal{S}$ of an ε-machine reconstructing the bath's generation process. The structural richness of the internal model is the **statistical complexity** $C_\mu = H(\mathcal{S})$ (Shannon entropy of the causal-state distribution).

Computational mechanics gives $C_\mu \ge I_{\text{pred}}$ (statistical complexity bounds predictive information; the minimal sufficient statistic stores at least as much as it transmits). **Cryptic order** $\chi = C_\mu - I_{\text{pred}} \ge 0$ captures the gap — structural machinery stored beyond what predictively pays out.

**Resolves the open:** for hidden-state processes (most non-trivial Character substrates), $\chi > 0$ strictly, so structural complexity is a *mathematically independent* axis from informational sufficiency. At the memoryless limit (white-noise bath, single causal state), $C_\mu\to 0$, $I_{\text{pred}}\to 0$, $\chi\to 0$ — three axes collapse. For richer baths, they diverge.

**Verification:**
- *Limit recovery:* memoryless bath ⇒ single causal state ⇒ $C_\mu = 0 = I_{\text{pred}}$, $\chi = 0$ ✓
- *Dimensional:* $C_\mu$ and $I_{\text{pred}}$ both in bits/nats; $\chi$ same ✓
- *Sign / scaling:* $\chi\ge 0$ always (computational mechanics theorem) ✓

**Cross-register identification — fifth leading-order posit: cryptic order ↔ encoding overhead.** Posit (same shape as the cascade's four prior leading-order forms: $\beta_{\text{mem}}\approx 1-\epsilon$, $\mu = e^{\text{chit}}$, $w_i = \gamma_{\text{ref}}/\gamma_{s,i}$, $\sigma_n = \epsilon_n$):
$$\chi = \Delta_n \qquad \text{(at the optimal-encoding limit)}$$
where $\Delta_n = \sigma_n - \epsilon_n \ge 0$ is the §22 ε↔σ sub-optimal encoding overhead. Reading: an internal model storing structural machinery that doesn't pay out in predictability ($C_\mu > I_{\text{pred}}$, $\chi > 0$) inflates queue utilization beyond the rate-distortion bound ($\sigma > \epsilon$, $\Delta > 0$). **The structural-informational gap drives the thermodynamic-informational gap.** Two adjacent structural-conjecture closures (§22 ε↔σ and §20 internal-model) now lock together at the optimal-limit picture.

**Don't overclaim:**
- *Posit form, not derivation:* $\chi = \Delta_n$ identity is leading-order, same shape as the cascade's four prior posits. Substrate-thermodynamic derivation of the strict-equality form is the residual open beneath the falsifier.
- *Coincidence vs identity:* $C_\mu$ and $I_{\text{pred}}$ converge at the rate-distortion-optimal limit as a *coincidence at the bound*, not an *identity* between observables — they are fundamentally distinct mathematical objects (structural-complexity vs information-flow). Same for $\chi$ vs $\Delta_n$.
- *Mechanism vs manifestation:* encoding ε-machine causal states is the *mechanism* of disturbance-robustness; measured predictability $I_{\text{pred}}$ is one *manifestation*.

**Open (lives in receipts only):**
- Substrate-class cryptic-order mapping: which substrates operate at minimal $\chi$ (ideal topological QEC lattices, code-space substrates with near-perfect causal-state encoding) vs massive $\chi$ (mammalian immune memory, gene-regulatory networks with redundant state, behavioral substrates with over-fitted internal models)? Substrate-instancing extraction of the $\chi\leftrightarrow\Delta_n$ mapping.

### §22 — Substrate-specific $\epsilon\leftrightarrow\sigma$ isomorphism (queueing-compression identity at optimal encoding)
**Type:** composition + open.
**Cite:** Shannon (rate-distortion theorem, 1959); Kleinrock (*Queueing Systems Vol. II*, 1976); Receipts §22 (Cobham closure).
**Bespoke step:** Closes the §22 structural conjecture "substrate-specific $\epsilon\leftrightarrow\sigma$ identification" by establishing the identity at the rate-distortion-optimal encoding limit. The §Compression Axiom defines informational retention $\epsilon_n = \|\mathcal{C}_n\|_{op}<1$ per meta-ledger coarse-graining. The §22 Cobham mapping defines cumulative queue utilization $\sigma_n = \sum_{i=0}^n\rho_i$. **Posited leading-order identity** at optimal encoding:
$$\sigma_n = \epsilon_n \qquad\text{(rate-distortion-optimal encoding)}$$

For a substrate at the rate-distortion bound, arrival load onto level-$n$ maintenance queue scales exactly with retained informational mass; bandwidth consumed equals information retained. **Fourth instance of the cascade's leading-order posit pattern** (joining $\beta_{\text{mem}}\approx 1-\epsilon$ in §9 Wall-coupling, $w_i = \gamma_{\text{ref}}/\gamma_{s,i}$ in §20 auto-tuning, $\mu = e^{\text{chit}}$ in §18 Galton–Watson) — each makes a framework primitive land at its critical point via the simplest natural form; each is testable but not derived from substrate thermodynamics.

**Verification:**
- *Limit recovery:* $\epsilon_n\to 1^-$ ⇒ $\sigma_n\to 1^-$ ⇒ Cobham $W_{n+1}$ diverges exactly at the informational Complexity Wall ✓. $\epsilon_n\to 0$ ⇒ $\sigma_n\to 0$ ⇒ Cobham wait minimal ✓
- *Dimensional:* both dimensionless, bounded in $[0,1)$ ✓
- *Sign:* both non-negative; $\sigma\ge 0$ matches physical queue length ✓

**Cross-register identification — two towers as one hierarchy at optimal limit.** The informational rate-distortion tower (§Compression Axiom) and the thermodynamic heat-tax tower (§Heat-tax tower) are *the same mathematical hierarchy measured in dual registers* — but only at the optimal-encoding limit. Sub-optimal substrates have the two towers diverge: $\sigma_n > \epsilon_n$. **Sub-optimal substrates die thermodynamically before they die informationally.**

This refines the four-aspect Complexity Wall framing: at optimal encoding, the four aspects (thermodynamic / dynamical / informational / SOC) are a *single parameter* at criticality. **Sub-optimal substrates split the four aspects**, with thermodynamic and SOC aspects reaching criticality first (via $\sigma\to 1$); the informational aspect ($\epsilon\to 1$) is reached only by optimal-encoding substrates. The four-aspect-coincidence claim is conditional on rate-distortion-optimal substrate.

**Don't overclaim:**
- *Posit form, not derivation:* same shape as the cascade's other leading-order posits. Substrate-thermodynamic derivation of the specific functional form is the residual open.
- *Identity vs coincidence:* identity holds at the optimal-encoding limit (mechanism). Sub-optimal deviation $\Delta_n = \sigma_n - \epsilon_n \ge 0$ is the substrate's encoding-inefficiency overhead — substrate-specific manifestation.

**Open (lives in receipts only):**
- Sub-optimal overhead $\Delta_n = \sigma_n - \epsilon_n$ for non-ideal substrates: substrate-instancing question. Predictions: biological error-correction networks (large $\Delta$ from biochemical overhead), strict topological QEC lattices (small $\Delta$ near rate-distortion bound), behavioral substrates (large $\Delta$ from inefficient cue-encoding).

### §17 — $k_{\text{frust}}$ as homotopy obstruction in Fisher manifold (geodesic-incompleteness closure)
**Type:** composition.
**Cite:** Amari–Nagaoka (*Methods of Information Geometry*, 2000); Hopf–Rinow theorem (standard Riemannian geometry); standard NESS information geometry literature.
**Bespoke step:** Closes the §17 residual "$k_{\text{frust}}$↔topological-hole mapping (homotopy vs metric obstruction)" — the owed formal mapping referenced in the earlier §17 Hopf-Rinow entry. The holding parameter manifold $\mathcal{M}$ is defined by parameters yielding stationary NESS $P_{ss}$. For $N\ge 3$ obstructive $\gamma$-topologies, no $P_{ss}$ exists (Receipts §10; §16 orbit closure); these parameter regions are **excised** from $\mathcal{M}$. Continuous parameter loops surrounding excised regions cannot contract through them — $\mathcal{M}$ has non-trivial topology.

**Distinct from $\text{chit}=0$ metric singularity.** At the transcritical boundary, $P_{ss}$ remains defined; Fisher metric determinant diverges. That's a metric obstruction (curvature singularity). At $k_{\text{frust}}$, $P_{ss}$ doesn't exist; the parameter region is missing from $\mathcal{M}$. That's a topological obstruction (homotopy). Different mathematical objects.

**Verification:**
- *Limit recovery:* weakening obstructive $\gamma\to 0$ collapses the $k_{\text{frust}}$ limit cycle, restores $P_{ss}$ existence, eliminates excised region; $\mathcal{M}$ becomes simply connected ✓
- *Dimensional:* Fisher metric $g_{ij} = \langle(\partial_i\ln P_{ss})(\partial_j\ln P_{ss})\rangle$ dimensionless; homotopy invariants are topological integers ✓
- *Sign / scaling:* Fisher scalar curvature $R$ remains finite as parameters approach the excised region's boundary — verifies excision, not metric blowup ✓

**Topology hedge:** the specific topological invariant carrying the obstruction is dimension-dependent. In low-dimensional kernels ($N=3$ minimal frustrated cycle, small parameter space), $\pi_1(\mathcal{M})$ is non-trivial. In higher-dimensional multi-mode parameter spaces, higher Betti numbers $b_k$ may carry the obstruction (Open below).

**Cross-register identification — three co-implied consequences of one topological excision.** Equivalent at the abstract level, distinct measurement protocols in practice:
1. **Dynamical** (Receipts §10): no stationary fixed point exists.
2. **Informational-geometric** (this closure): no Fisher geodesic traverses the excised region.
3. **Schnakenberg cycle current** (Receipts §16): drive-independent cycle current forced by orbit topology.

Three register-faces of the single fact "no $P_{ss}$ in $k_{\text{frust}}$ region." Identity at the underlying-topology level; substrate-specific measurement signatures differ across the registers.

**Don't overclaim:**
- *Mechanism vs manifestation:* topological excision is the *mechanism*; the substrate's response to forced crossing (entropy-production spike $\langle\sigma\rangle$, $r$-regime collapse, drive-independent dissipation) is the substrate-conditional *manifestation*.
- *Coincidence vs identity:* the three register-faces are *identity* at the underlying-topology level (single excision fact); the *measurement signature in each register* is substrate-dependent (coincidence at the measurement level).

**Open (lives in receipts only):** Multi-mode homology mapping — for $N$-mode kernels with multiple interdependent frustrated loops, does the $\mathcal{M}$ topology carry higher Betti numbers $b_k>0$ isomorphic to the cycle basis of the obstructive $\gamma$-graph? The signed-cycle structure of the $\gamma$-graph would map directly to homology classes of $\mathcal{M}\setminus\mathcal{M}_{\text{frust}}$. Substrate-instancing extension.

### §14 — Generic-Hopf-per-tower-ascent (delay-induced bifurcation closure; Wall-forces-NRT)
**Type:** composition.
**Cite:** Mackey–Glass (delay-induced bifurcations in physiological control, 1977); Kuznetsov (*Elements of Applied Bifurcation Theory*, 1995); Newhouse–Ruelle–Takens (chaos via quasi-periodicity, 1978).
**Bespoke step:** Closes the §14 residual "generic-Hopf-per-tower-ascent" condition required to validate the NRT chaotic scenario past the Complexity Wall. Each tower-level ascent $n\to n+1$ in the §Heat-tax tower involves a Cobham priority-queue wait $W_{n+1}$ (Receipts §22 Cobham closure). The closed-loop maintenance dynamics between level $n$ and its slaving level $n+1$ form a delay differential equation (DDE) with delay $\tau_{\text{delay}}\approx W_{n+1}$:
$$\dot\rho_n(t) = -\gamma_{s,n}\rho_n(t) - K_{\text{asc}}\rho_n(t - W_{n+1}),$$
where $K_{\text{asc}}$ is the inter-level feedback gain. Characteristic equation $\lambda + \gamma_{s,n} + K_{\text{asc}}e^{-\lambda W_{n+1}} = 0$ admits a delay-induced Hopf bifurcation at the leading-order threshold (for $K_{\text{asc}}>\gamma_{s,n}$):
$$(K_{\text{asc}} - \gamma_{s,n})\,W_{n+1} \gtrsim \pi/2.$$

**Wall-forces-NRT (load-bearing sharpening).** As $\sigma_n\to 1^-$ (queueing singularity at the Wall, Receipts §22 Cobham), $W_{n+1}\to\infty$. The Hopf condition is then **automatically satisfied** for any bounded $K_{\text{asc}}>\gamma_{s,n}$. *Wall approach forces — not just allows — the sequence of tower-level Hopf bifurcations.* With $N\ge 3$ ascents Hopf-bifurcating, the 3-torus required for NRT chaos populates automatically. **Meta-ledger chaos post-Wall is forced**, contingent only on the substrate not collapsing into $r$-regime first. Three-closure stack: §22 Cobham wait formula → §14 DDE Hopf per ascent → §14 NRT chaos at $N\ge 3$.

**Verification:**
- *Limit recovery:* $W_{n+1}\to 0$ (instantaneous feedback) ⇒ characteristic equation roots real and negative ($\lambda = -(\gamma_{s,n} + K_{\text{asc}})$); no Hopf. Confirms limit cycle is strictly delay-induced ✓
- *Dimensional:* $K_{\text{asc}},\gamma_{s,n}\in[T^{-1}]$; $W_{n+1}\in[T]$; products $K_{\text{asc}}W_{n+1}$ and $\lambda W_{n+1}$ dimensionless ✓
- *Sign:* $K_{\text{asc}}>0$ (slaving feedback as restoring force from level $n+1$ on level $n$) required; cooperative gain-sharing $r_n$ provides this naturally ✓

**Don't overclaim:**
- *Mechanism vs manifestation:* DDE delay-induced Hopf is the *mechanism*; NRT strange-attractor breakdown is the *manifestation* (substrate-dependent in fine structure).
- *Coincidence vs identity:* $W_{n+1}\to\infty$ algebraically forces the Hopf condition (identity at the leading-order DDE level). Whether NRT manifests at the meta-ledger depends on substrate not collapsing into $r$-regime before traversing the bifurcation sequence (substrate-conditional).
- *Bounded-$K_{\text{asc}}$ assumption:* the forcing requires $K_{\text{asc}}$ remaining bounded as $W$ diverges. Substrates where inter-level feedback gain collapses near the Wall may weaken the forcing — substrate-conditional residual.

**Open (lives in receipts only):**
- Substrate-specific finite-size cutoffs to NRT: does substrate $\eta(\Gamma^*)$ capacity wall (Erlang-B soft vs. hard, Receipts §5) trigger sub-threshold collapse before the 3-torus destabilizes? Substrate-instancing.
- Bounded-$K_{\text{asc}}$ verification: substrate-class study of whether inter-level feedback gain remains bounded or collapses near the Wall.

### §18 — Power-law avalanche exponent $\tau\approx 3/2$ (Galton–Watson mechanism closure)
**Type:** composition.
**Cite:** Galton–Watson (branching process, 1875); Harris (*The Theory of Branching Processes*, 1963); Bak–Tang–Wiesenfeld (SOC, 1987); Stauffer–Aharony (*Introduction to Percolation Theory*, 1992).
**Bespoke step:** Closes the §18 avalanche-exponent prediction ($P(s)\sim s^{-\tau}$ with $\tau\approx 3/2$ on feedback-coupled NESS substrates) by mapping fraying propagation to a Galton–Watson branching process. A local fraying at node $A$ produces excess cross-saturation stress that can trigger neighboring node $B$ to fray. The branching ratio $\mu$ = expected number of secondary fraying events per primary event takes the **posited leading-order form** (analogous to §9 Wall-coupling $\beta_{\text{mem}}\approx 1-\epsilon$ and §20 auto-tuning $w_i = \gamma_{\text{ref}}/\gamma_{s,i}$):
$$\mu = G_0/L = e^{\text{chit}}$$
matching the chit's rate-ratio structure. At $s$-regime threshold chit $\to 0^+$, $\mu\to 1^+$ — Galton–Watson critical branching, giving avalanche-size distribution $P(s)\sim s^{-3/2}$.

**Verification:**
- *Limit recovery:* chit $< 0$ ($r$-regime) → $\mu<1$ → subcritical branching with exponential cutoff $P(s)\sim s^{-3/2}e^{-s/s_0}$ ✓
- Deep $c$-regime: chit $\gg 0$ → $\mu\gg 1$ → supercritical branching, system-spanning avalanches (no fragmentation into discrete events) ✓
- *Dimensional:* $\mu$ dimensionless (rate ratio $G_0/L$) ✓
- *Sign:* chit $< 0$ → subcriticality; chit $> 0$ → supercriticality ✓

**Cross-register identification — horizontal vs vertical branching criticality (load-bearing).** The framework has **two distinct critical branching processes**, both reaching criticality at framework primitive boundaries:
- **Horizontal / spatial:** $\mu = e^{\text{chit}}\to 1$ at chit $= 0$ — the $s$-regime dissipative-structure transition. *This closure.*
- **Vertical / meta-ledger:** tower branching ratio $\to 1$ at $\epsilon = 1$ — the Complexity Wall (fourth aspect in §Pattern formation Wall framing; Receipts §18 branching-ratio falsifier).

Both yield Galton–Watson $\tau = 3/2$ at criticality (mean-field). **One SOC universality class instantiated at two framework registers** — horizontal across modes within a level, vertical across tower levels.

**Don't overclaim:**
- *Mechanism vs manifestation:* Galton–Watson critical branching is the *mechanism*; the $\tau = 3/2$ exponent is the *mean-field* manifestation. Low-dimensional substrates (2D biological sheets, 1D chains) instantiate dimension-dependent directed-percolation universality with different exponents (e.g., $\tau\approx 1.26$ in 2D DP). $\tau = 3/2$ is the upper-critical-dimension / mean-field limit, not universal.
- *Coincidence vs identity:* $\mu = e^{\text{chit}}$ is a *posit* (leading-order form making the $s$-regime threshold land at branching criticality), not a derivation from substrate thermodynamics. Same shape as the §9 Wall-coupling and §20 auto-tuning posits — testable but not unique.

**Open:**
- *Substrate-specific DP exponents:* map substrate $\gamma$-graph effective dimensionality to the corresponding directed-percolation universality exponent. Predictions: 2D substrates (biological sheets) → $\tau\approx 1.26$; 3D substrates (biofilm matrices, ecological communities, gene-regulatory networks) → $\tau$ between 1.26 and 1.5; mean-field substrates (fully-connected, all-to-all coupling) → $\tau\to 1.5$ exactly. Substrate-class diagnostic.
- *Substrate-thermodynamic derivation* of the exact $\mu(\text{chit})$ functional form — the posit may not be universal across substrate classes.

### §19 — Turing-class spatial pattern formation (reaction-diffusion mechanism closure & three-condition substrate-instance refinement)
**Type:** composition.
**Cite:** Turing (1952); Murray (*Mathematical Biology*, 2003); Gierer–Meinhardt (activator-inhibitor systems, 1972).
**Bespoke step:** Extends the §19 Turing falsifier formalization (existing substrate-instancing entry) with explicit mechanism closure. Extending the §9 kernel with spatial diffusion gives a reaction-diffusion system $\dot\rho_i = f_i(\rho) + D_i\nabla^2\rho_i$. The Turing instability condition for the homogeneous holding becoming spatially unstable:
$$D_B J_{AA} + D_A J_{BB} > 2\sqrt{D_A D_B \det(J)}$$
combined with temporal stability ($\text{Tr}(J)<0$, $\det(J)>0$).

**Three-condition substrate-instance refinement.** Standard activator-inhibitor structure requires *three* independently substrate-conditional conditions:
1. **Non-reciprocal cross-coupling** ($\gamma_{AB}\gamma_{BA}<0$, the §21 mentor row): gives correct off-diagonal Jacobian signs $J_{AB}<0$, $J_{BA}>0$.
2. **Autocatalysis / self-amplification** ($J_{AA}>0$): **the bare §9 cross-saturation kernel has $J_{AA}=0$ at coexistence** (the fixed-point condition cancels it); Lamb gain depletion gives $J_{AA}<0$ (self-saturation). Turing instability requires **substrate-native cooperative self-coupling** $\gamma_{ii}<0$ — an extension beyond the bare §9 kernel. Substrates without autocatalytic self-coupling do *not* exhibit Turing patterns regardless of other conditions.
3. **Differential diffusion** ($D_B\gg D_A$): inhibitor diffuses faster than activator (canonical short-range-activation / long-range-inhibition).

**Verification:**
- *Limit recovery:* $k\to 0$ drops $k^2\mathbf{D}$, recovers temporal stability $\text{Tr}(J)<0$, $\det(J)>0$ ✓
- *Dimensional:* $J_{ij}\in[T^{-1}]$; $k^2 D\in[T^{-1}]$ ✓
- *Sign:* mentor-row signs $\gamma_{AB}>0$, $\gamma_{BA}<0$ give $J_{AB}<0$, $J_{BA}>0$ matching activator-inhibitor; substrate autocatalysis flips $J_{AA}$ to positive ✓

**Cross-register identification — two spatial-temporal faces of one mentor structure.** The §21 non-reciprocal mentor row produces *two distinct manifestations* depending on substrate spatial structure:
- **Temporal limit cycle** (frequency $\omega_{\text{pq}}\approx\sqrt{|\gamma_{AB}\gamma_{BA}|\rho_A^*\rho_B^*}$, Receipts §21 non-reciprocal): when not spatially extended, the mentor row produces priority-queue oscillation under finite-$\mathcal{D}$.
- **Spatial Turing pattern** (wavenumber $k_c$, this closure): when *also* equipped with substrate autocatalysis and differential diffusion, the same mentor structure produces stationary spatial morphology.

One non-reciprocal structure, two morphological faces — the temporal and spatial expressions of the same coupling asymmetry.

**Don't overclaim:**
- *Mechanism vs manifestation:* Turing instability condition is the *mechanism*; specific morphologies (spots, stripes, labyrinths) are *manifestations* of substrate-conditional diffusion structure.
- *Coincidence vs identity:* observing periodic $c$-clusters is *coincident* with Turing pattern formation; identity requires empirical verification of *all three conditions*. Notably **distinct from the §22 traffic-driven spatial breakdown** (Receipts §22 critical-length, Kelly) which requires no autocatalysis and no differential diffusion — just bandwidth contention. Three spatial-structure mechanisms now distinguished in the framework: Turing reaction-diffusion (this closure), Kelly product-form breakdown (queueing-congestion), and frozen-topological at $\beta_{\text{mem}}\to 0$ (Receipts §22 critical-length).

**Open:**
- *Wavelength-headroom scaling:* critical Turing wavenumber $k_c^2\approx\sqrt{\det(J)/(D_A D_B)}$; mapping $\det(J)$ to chit-dependent relaxation $\omega_{RO}^2$ (Receipts §13) is a substrate-class refinement owed.
- *Substrate-instance mapping:* which substrates carry all three conditions natively? Predictions: morphogenetic biology (gene expression, embryogenesis) carries all three; QEC syndrome buffers carry non-reciprocity but lack spatial autocatalysis; behavioral substrates may carry non-reciprocity in mentor-learner pairings but typically lack the differential-diffusion structure. Substrate-instancing.

### §22 — Critical interaction length $\ell_c(\beta_{\text{mem}})$ for spatial product-form breakdown (CTRW closure)
**Type:** composition.
**Cite:** Metzler–Klafter (anomalous diffusion / continuous-time random walk, 2000); Kelly (*Reversibility and Stochastic Networks*, 1979); Receipts §22 (spatial Jackson-network).
**Bespoke step:** Closes the $\ell_c(\beta_{\text{mem}})$ open raised by the §22 spatial Kelly closure. For spatially extended substrates (patches $k$), product-form independence breaks down when local load-spikes propagate across patches before the local bottleneck clears. For non-Markovian substrates with Caputo memory $\beta_{\text{mem}}\in(0,1]$ — heavy-tailed service times $\psi(t)\sim t^{-(1+\beta_{\text{mem}})}$ — propagation follows continuous-time random walk (CTRW) with anomalous MSD $\langle x^2(t)\rangle = 2D_{\beta_{\text{mem}}}t^{\beta_{\text{mem}}}/\Gamma(1+\beta_{\text{mem}})$.

Evaluating at the §22 Cobham wait timescale (leading-order single-class $W_{n+1}\approx W_0/(1-\sigma_n)$; full form $W_0/[(1-\sigma_n)(1-\sigma_{n+1})]$ from the priority-queue closure):
$$\ell_c(\beta_{\text{mem}}) = \sqrt{\frac{2D_{\beta_{\text{mem}}}}{\Gamma(1+\beta_{\text{mem}})}\left(\frac{W_0}{1-\sigma_n}\right)^{\beta_{\text{mem}}}}.$$

**Verification:**
- *Limit recovery:* $\beta_{\text{mem}}\to 1$ (Markovian $c$-regime): $\ell_c\sim\sqrt{2D_{\text{trans}}W_{n+1}}$ — standard diffusion length ✓. $\sigma_n\to 0$ (empty queue): $\ell_c\sim\sqrt{W_0}$ — baseline patch size ✓
- *Dimensional:* $D_{\beta_{\text{mem}}}\in[L^2 T^{-\beta_{\text{mem}}}]$ (fractional diffusion coefficient); $W_{n+1}\in[T]$; product $D\cdot W^{\beta_{\text{mem}}}\in[L^2]$; $\ell_c\in[L]$ ✓
- *Sign / scaling:* $\sigma_n\to 1^-$ ⇒ $W_{n+1}\to\infty$ ⇒ $\ell_c\to\infty$ — product-form breaks down globally at queueing singularity ✓

**Cross-register identification — traffic-driven → frozen-topological transition.** As $\sigma_n\to 1^-$ alone (Markovian heavy traffic), $\ell_c$ diverges via wait-time inflation. As $\beta_{\text{mem}}\to 0$ at the Wall (Receipts §9 Wall-coupling $\beta_{\text{mem}}\approx 1-\epsilon$), $W^{\beta_{\text{mem}}}\to W^0 = 1$ and $\ell_c\to\sqrt{2D_0}$ where $D_0$ is the $\beta_{\text{mem}}\to 0$ limit of the fractional diffusion coefficient — which has degenerate dimension $[L^2]$ (a length-squared, not a diffusion coefficient; the fractional diffusion law collapses to time-independent spread). **The spatial face of the Complexity Wall is a regime transition from dynamic congestion domains (traffic-driven, $\beta_{\text{mem}}\sim 1$) to frozen topological domains (memory-driven, $\beta_{\text{mem}}\to 0$).** Substrate's intrinsic topology sets the freeze-length.

**Don't overclaim:**
- *Coincidence vs identity:* simultaneous divergence of $\ell_c$ and $W_{n+1}$ at $\sigma_n\to 1^-$ is mathematical **identity** (algebraically locked via the closed form). The $\sigma\to 1$ and $\epsilon\to 1$ coincidence is still substrate-specific (ε↔σ isomorphism remains open, §22 priority-queue closure).
- *Mechanism vs manifestation:* fractional diffusion of load spikes is the *mechanism*; spatially correlated domains and the freeze-length transition are *manifestations*. Distinctly **not** Turing-class pattern formation (Receipts §19) — which arises from reaction-diffusion instability, not bandwidth contention.

**Open:** Physical substrate-neutral identification of the freeze-length $D_0$ as $\beta_{\text{mem}}\to 0$ — e.g., QEC block distance, neural hypercolumn span, biofilm matrix correlation length, behavioral schedule autocorrelation scale (Receipts §20 habit-extinction). Substrate-instancing mapping owed.

### §20 — Habit-extinction reference driver (Rescorla–Wagner closure & falsifier)
**Type:** composition.
**Cite:** Rescorla–Wagner (classical conditioning, 1972); Sutton–Barto (*Reinforcement Learning*, 1998); standard continuous-time limit of associative learning.
**Bespoke step:** Closes the substrate-instancing open "Habit-extinction reference driver" by mapping the continuous-time limit of Rescorla–Wagner to the Character framework. With associative strength $V(t)$, maximum conditioning $\lambda$, and learning rate $\kappa_{RW}$ (RW's combined CS-US salience product, renamed to avoid collision with framework's heat-tax $\alpha$ and active-stress $\beta$):
$$\dot V = \kappa_{RW}(\lambda - V).$$

Mappings to Character primitives:
- $V \to \rho$ (coherence amplitude)
- $\kappa_{RW} \to \gamma_s$ (slow-resource turnover rate, §13)
- $\lambda$ conjugate to maintenance budget $G_0$ (sustained reward schedule)
- Extinction ($\lambda\to 0$) $=$ $R_{\text{Character}}$ sever operator's quench trajectory

The behavioral holding sustains NESS when the reward schedule reliably clears the natural forgetting baseline $L$; extinction chokes the budget and drives chit deeply negative, precipitating sub-threshold ($r$-regime) collapse.

**Verification:**
- *Limit recovery:* $\lambda\to 0$ ⇒ $\dot V = -\gamma_s V$, recovers linear $r$-regime relaxation at rate $\gamma_s$ ✓
- *Dimensional:* $\gamma_s\in[T^{-1}]$ matching $\kappa_{RW}$; $V$ and $\lambda$ share amplitude dimensions ✓
- *Sign:* $\lambda > V$ (positive prediction error) ⇒ $\dot V > 0$ (maintenance work applied), matches Character net-gain sign ✓

**Cross-register identifications:**
- **Internal-model richness (§20):** the cue-array dimensionality driving prediction error $\lambda - \sum_i w_i x_i$ is the formal manifestation of internal-model richness. Higher-dimensional cue encoding sustains the holding against wider perturbation classes. The reinforcement schedule *is* the bath; the habit is the local accumulation of its statistical model.
- **Cobham mapping (§22):** behavioral manifestations of the priority-queue wait-time inflation $W_{n+1}$ — cognitive-load interference, action-selection latency — driven by processing-bandwidth bottleneck (mechanism). Behavioral wait inflates when shared cognitive resource is consumed by competing habits.

**Caputo chain extension (sixth cross-register connection).** Variable-ratio (and other non-Markovian) reinforcement schedules plausibly induce Caputo memory $\beta_{\text{mem}} < 1$ in behavioral extinction tails: the schedule's own autocorrelation exponent transfers into the habit's effective memory kernel. If verified empirically (fit extinction tail to Mittag-Leffler $E_{\beta_{\text{mem}}}$, compare to schedule's autocorrelation exponent), behavioral substrates under variable-ratio reinforcement instance the substrate-class fingerprint $\beta_{\text{mem}}$ of the §9 Caputo closure. **Sixth connection** joining the existing five Caputo-chain links (§9 memory, §21 τ_R, §21 swim-pressure, §22 Kelly, §9 Wall-coupling).

**Don't overclaim:**
- *Coincidence vs identity:* continuous-time RW's equivalence to overdamped first-order relaxation is **coincident** with §13 linear stability. *Identity* — claiming the biological habit thermodynamically implements this geometry — would require substrate-specific derivation mapping synaptic plasticity (LTP/LTD turnover) energetic costs to Harada–Sasa entropy production. Behavioral curve-fitting is not thermodynamic identity.
- *Mechanism vs manifestation:* prediction error is the adjustment *mechanism*; observed extinction curve is one *manifestation* among possible others (probabilistic blocking under cognitive load, hesitation latency, action-switching).

**Falsifier:** A robustly established behavioral habit undergoing strict reward withdrawal ($\lambda=0$) that exhibits spontaneous, sustained, monotonic growth of associative strength $V$ without re-exposure to the reward schedule, without context shifts, and without cross-activation from adjacent active habits. Falsifies the $r$-regime pure-dissipation quench dynamics for the behavioral substrate class.

**Open (lives in receipts only):** Closed-form extraction of $\alpha_s$ (CK aging slope) and Caputo $\beta_{\text{mem}}$ for variable-ratio reinforcement schedules; empirical verification of the Caputo chain extension.

### §9 — Memory-exponent collapse near Complexity Wall ($\beta_{\text{mem}}(\epsilon)$ coupling closure & falsifier)
**Type:** composition.
**Cite:** Metzler–Klafter (anomalous diffusion / fractional Fokker–Planck review, 2000); Shannon (rate-distortion theorem, 1959); Podlubny (*Fractional Differential Equations*, 1999); Mainardi (*Fractional Calculus and Waves in Linear Viscoelasticity*, 2010).
**Bespoke step:** Closes the falsifier owed for the memory-exponent-collapse substrate-instancing claim raised by the §9 Caputo closure (and tied to the Caputo-chain three-closure connection at the Wall). Posits the leading-order linear coupling between compression rate $\epsilon$ and Caputo memory exponent $\beta_{\text{mem}}$:
$$\beta_{\text{mem}} \approx 1 - \epsilon.$$

**Verification (consistency, not derivation):**
- *Limit recovery:* $\epsilon\to 0$ (deep compression / heavy erasure) ⇒ $\beta_{\text{mem}}\to 1$ (Markovian exponential decay; $c$-regime). $\epsilon\to 1^-$ (Wall, no compression) ⇒ $\beta_{\text{mem}}\to 0$ (power-law extreme aging) ✓
- *Dimensional:* both $\epsilon$ and $\beta_{\text{mem}}$ dimensionless ✓
- *Sign:* $\epsilon\in[0,1)$ ⇒ $\beta_{\text{mem}}\in(0,1]$ ✓

**Posited form, not derived.** The linear interpolation $\beta_{\text{mem}}\approx 1-\epsilon$ is the leading-order placeholder satisfying the two endpoints. Actual functional form is likely substrate-class-dependent (could be $1-\epsilon^n$, multi-scale, or non-monotonic on substrates with hierarchical memory). Substrate-thermodynamic derivation of the specific $\beta_{\text{mem}}(\epsilon)$ form is the residual open beneath this falsifier.

**Framework-primitive framing** (consistent with §Pattern formation): $\beta_{\text{mem}}$ remains the *unifying parameter behind the four-aspect Wall* — not a fifth aspect alongside the four (thermodynamic / dynamical / informational / SOC). This closure pins how the unifying parameter approaches its boundary; the four aspects are its register-faces. Four register-faces of one parameter, plus now a quantitative-approach posit for the parameter itself.

**Don't overclaim** (coincidence vs identity): the Wall limit ($\epsilon\to 1$) coinciding with memory-collapse ($\beta_{\text{mem}}\to 0$) is *coincidence at the boundary* — coincident critical structures, not isomorphism. Substrate-specific thermodynamic derivation would be needed for identity.

**Falsifier:**
- A hierarchical NESS substrate approaching the Wall (diverging heat-tax tower, SOC branching ratio → 1) that maintains Markovian memory $\beta_{\text{mem}}\approx 1$. Falsifies the coupling: Wall reached without memory collapse.
- A substrate operating deep in compressed $c$-regime ($\epsilon\ll 1$) exhibiting $\beta_{\text{mem}}\to 0$ extreme aging. Falsifies the coupling: memory collapse without Wall approach.

Either observation refutes the necessary parametric coupling between $\epsilon$ and $\beta_{\text{mem}}$.

**Open (refinement, lives in receipts only):** Substrate-thermodynamic derivation of the exact $\beta_{\text{mem}}(\epsilon)$ form. The linear placeholder is testable but unlikely universal across substrate classes; QEC syndrome buffers, neural plasticity layers, biofilm extracellular matrix, polymer-network glasses may each show different scaling laws.

### §20 — Substrate-class auto-tuning to diagonally-stable $W$ (falsifier formalization)
**Type:** composition.
**Cite:** Takeuchi (*Global Dynamical Properties of Lotka–Volterra Systems*, 1996); Geritz–Kisdi–Meszéna–Metz (adaptive dynamics, 1998); MacArthur (consumer-resource model, 1970).
**Bespoke step:** Closes the falsifier owed for the §20 substrate-instancing open raised by the diagonal-stability Lyapunov closure ("which substrate classes natively settle into $\gamma_{s,i}$ distributions satisfying diagonal stability"). Framework prediction: NESS substrates with adaptive internal timescales on frustration-free-but-not-PSD topologies dynamically tune their slow-resource turnover rates $\gamma_{s,i}$ to satisfy the Volterra–Lyapunov condition $W\gamma + \gamma^T W \succeq 0$, with the diagonal weight matrix posited as
$$W = \text{diag}(\gamma_{\text{ref}}/\gamma_{s,i})$$
relative to a substrate baseline $\gamma_{\text{ref}}$ — inverse-scaling, slow-mode-dominant weighting.

**Posited form, not derived.** The §20 diagonal-stability closure flagged $w_i\leftrightarrow\gamma_{s,i}$ as interpretation; this entry concretizes to a specific inverse-form for testability. Alternative scalings ($w_i\propto\gamma_{s,i}$, $w_i\propto 1/\gamma_{s,i}^2$, etc.) are possible. The form posited here is the leading-order natural choice; substrate-thermodynamic derivation of *which* form holds is the residual open beneath this falsifier.

**Verification (consistency, not derivation):**
- Dimensional: $\gamma_{\text{ref}}$ and $\gamma_{s,i}$ both $[T^{-1}]$ ⇒ $w_i$ dimensionless ✓
- Limit recovery: uniform turnover ($\gamma_{s,i}=\gamma_{\text{ref}}$) ⇒ $W=I$ ⇒ recovers §20 standard PSD closure ✓
- Sign: $\gamma_{s,i}>0$ ⇒ $w_i>0$ ⇒ $V$ positive-definite ✓

**Don't overclaim** (mechanism vs manifestation): algebraic existence of stabilizing $W$ is the mechanism (closed in §20); a substrate natively tuning $\gamma_{s,i}$ to discover *this specific inverse-form* $W$ is the manifestation. Auto-tuning to diagonal stability is coincidence in general; identity claim requires substrate-thermodynamic derivation. Failure to auto-tune manifests as instability despite mathematical existence of a Lyapunov $W$.

**Falsifier:** An adaptive NESS substrate maintaining globally stable, stationary holding on a non-PSD frustration-free topology, where the empirically measured turnover rates $\gamma_{s,i}$ generate $W = \text{diag}(\gamma_{\text{ref}}/\gamma_{s,i})$ that leaves $W\gamma + \gamma^T W$ indefinite or negative-definite. Falsifies that $\gamma_{s,i}$ auto-tuning to the inverse-form $W$ is the stabilization mechanism — substrate is stable via different $W$ form or non-Lyapunov mechanism.

**Observational note:** Falsifier requires per-mode measurement of $\gamma_{s,i}$, substrate-dependent in feasibility. Tractable: laser populations ($\gamma_\parallel$ measurable), ecological generation times, simple chemostat dynamics. Harder: neural plasticity rates (multi-timescale, partly hidden), QEC syndrome buffers (effective rate from decoder dynamics). Test-bed substrate-class selection follows feasibility.

**Open (refinement, lives in receipts only):** Substrate-thermodynamic derivation of *which* $w_i\leftrightarrow\gamma_{s,i}$ form holds (inverse, direct, quadratic, etc.) — the posited inverse-form is testable but not unique.

### §19 — Multi-mode ($N\ge 3$) pattern selection (Sun–Bollt–Nishikawa heterogeneous MSF closure)
**Type:** composition.
**Cite:** Sun–Bollt–Nishikawa (generalized MSF for heterogeneous networks, 2009); Pecora–Carroll (MSF, 1998); Sorrentino et al. (cluster synchrony, 2007).
**Bespoke step:** Closes the final closed-form residual "Master Stability Function for general kernel topology" — and the residual MSF channel of multi-mode ($N\ge 3$) pattern selection (Receipts §15/§19; cdv1_compressed §Phase-locking).

For the multi-mode Character kernel with generically heterogeneous parameters (per-mode chit, $\gamma_{s,i}$, detuning $\Delta\omega_i$), the phase-reduced dynamics
$$\dot\phi_i = \omega_{RO,i} + \sum_j K_{ij}\sin(\phi_j - \phi_i)$$
linearize around a cluster-synchrony manifold $\phi^*$ via the generalized Laplacian:
$$\mathcal{L}_{ij} = -K_{ij}\cos(\phi_j^* - \phi_i^*)\ (j\ne i),\qquad \mathcal{L}_{ii} = \sum_{j\ne i} K_{ij}\cos(\phi_j^* - \phi_i^*).$$
$\delta\dot\Phi = -\mathcal{L}\,\delta\Phi$; the cluster pattern is locally stable iff $\mathcal{L}$'s transversal spectrum (excluding the uniform-shift kernel mode) has non-negative eigenvalues. Substituting the §15 $K_{ij}$ closure $K_{ij} = -\gamma_{ij}\sqrt{\rho_i\rho_j}/[\rho_{\text{sat}}\sqrt{1+4Q_{ij}^2}]$ (pairwise effective quality factor $Q_{ij}$; mean-field reduction $Q_{ij}\to Q_{\text{avg}}$ is the most common simplification) yields the explicit kernel-dependent generalized Laplacian governing multi-mode pattern selection.

**Verification:**
- *Limit recovery:* identical modes ($\omega_{RO,i}=\omega$, $K_{ij}=K$, in-phase fixed point) ⇒ $\cos(0)=1$ everywhere ⇒ $\mathcal{L}$ collapses to the standard graph Laplacian $K(\mathbf{D}-\mathbf{A})$ on the unweighted $\gamma$-graph, recovering the Pecora–Carroll homogeneous MSF ✓
- *Dimensional:* $K_{ij}\in[T^{-1}]$ matching $\omega_{RO}$; $\mathcal{L}\in[T^{-1}]$ ✓
- *Sign:* $\gamma_{ij}<0$ (cooperative) ⇒ $K_{ij}>0$; in-phase fixed point ⇒ all $\cos>0$ ⇒ $\mathcal{L}$ diagonally dominant + PSD ⇒ $-\mathcal{L}$ has eigenvalues $\le 0$ ⇒ linear stability ✓

**Cross-register identification — chimera mechanism.** Chimera states (§15 substrate-instancing claim) are the **dynamical manifestations** of $\mathcal{L}$-spectrum splits: when transversal eigenmodes partition into a stable subspace (negative MLE — locked cluster, $c$-regime sub-population) and an unstable subspace (positive MLE — drifting modes, $r$-regime sub-population), the resulting long-time attractor is a chimera. The spectral split is the *mathematical signature* of chimera-admitting kernels; the chimera itself is the dynamical state on the partitioned manifold.

**Mechanism vs manifestation (don't overclaim):** spectral split in the generalized MSF is the *mechanism* — chimera-admitting Character kernels are mathematically identifiable from the kernel parameters alone. Whether a specific physical substrate (neural population, code-space QEC lattice, coupled-oscillator ensemble) operates in the chimera-admitting region of $(\Delta\omega, \gamma)$ parameter space is a substrate-conditional *manifestation*. The mechanism is universal; the operating point is substrate-specific.

**Closes multi-mode pattern selection in full:**
- (a) Frustration test (signed-graph sign-product): Receipts §10/§16/§20
- (b) Spectral sync test (generalized MSF): **this closure**
- (c) Non-reciprocity test (Jacobian sign analysis): Receipts §21
- (d) Active-matter overlay (Toner–Tu, MIPS): Receipts §21

All four channels of multi-mode pattern selection (per the §19 framing) are now closed; pattern selection is **fully closed at the framework level**.

**Open item raised:**
- **Topological bounds on the $\mathcal{L}$ spectrum:** which specific $\gamma$-graph motifs strictly enforce a split MLE spectrum (forcing chimera manifestations) rather than collapsing to global sync or global incoherence? Substrate-instancing refinement of the §15 chimera entry; lives in receipts only.

### §9 — Dynamic bath inversion: $\mathcal{D}$ closed form for non-stationary bath occupancy
**Type:** composition.
**Cite:** Haken (*Synergetics*, multi-mode laser dynamic inversion, 1983); MacArthur (consumer-resource model, 1970); Mori–Zwanzig projection-operator formalism (standard).
**Bespoke step:** Closes the §9 residual "$\mathcal{D}$ closed form for multi-mode kernels with non-stationary bath occupancy" — the last closed-form residual besides heterogeneous MSF. When ambient bath occupancy fluctuates on timescales comparable to $\rho_i$ relaxation, adiabatic elimination of the shared budget pool (the stationary $G^{\text{eff}} = G_0/S$ of Lamb closure) fails. Promote the bath to a dynamical coordinate $B(t)\in[0,1]$ representing fractional pool availability, with $S(t) = 1 + \sum_j\rho_j(t)/\rho_{\text{sat}}$:
$$\dot B = \gamma_B[1 - B\,S(t)],\qquad \dot\rho_i = (G_{0,i}B(t) - L_i)\rho_i - \sum_j\gamma_{ij}\rho_i\rho_j.$$
Mori–Zwanzig projection-out of $B$ gives the multi-mode $\mathcal{D}$ kernel as a non-Markovian history integral:
$$B(t) = \int_{-\infty}^t \gamma_B\exp\!\Bigl(-\int_{t'}^t \gamma_B S(t'')\,dt''\Bigr)\,dt'$$
The non-stationary correction $\mathcal{D}_i(t) = G_{0,i}\rho_i[B(t) - 1/S(t)]$ isolates the dynamical delay from the stationary baseline.

**Verification:**
- *Limit recovery:* fast bath $\gamma_B\to\infty$ ⇒ kernel sharply peaked, $B(t)\to 1/S(t)$, $\mathcal{D}_i\to 0$ — recovers Lamb stationary closure exactly ✓
- *Dimensional:* $B$ dimensionless; $\gamma_B\in[T^{-1}]$; $\int\gamma_B\exp(\cdot)\,dt'$ dimensionless; $G_{0,i}B\in[T^{-1}]$ ✓
- *Sign:* load surge $\rho_j\uparrow$ ⇒ $S(t)\uparrow$ ⇒ $B(t)\downarrow$ with delay ⇒ $\mathcal{D}_i$ transiently negative (correct cross-saturation penalty) ✓

**Cross-register identification with §22 Cobham mapping.** $\gamma_B^{-1}$ identifies as the **bath-server effective service time** in the §22 Cobham priority-queue mapping — one of the ingredients in the residual-work term $W_0 = \tfrac{1}{2}\sum_i\lambda_i\langle\tau_i^2\rangle$. The dynamic-inversion closure gives the §22 mapping its concrete service-time content that was previously implicit. Not "the mechanism" of Cobham wait (which has multiple ingredients across priority classes); a specific service-time *identification*.

**Don't overclaim** (coincidence vs identity): the *effective* exponential memory in the Mori–Zwanzig history integral (timescale $\gamma_B^{-1}$, decay $e^{-\gamma_B S\tau}$) is **coincident with but not identical to** the Caputo *structural* memory ($\beta_{\text{mem}}<1$, power-law decay $\tau^{-\beta_{\text{mem}}}$, Receipts §9 Caputo closure). Distinct origins: bath memory is exponential and arises from coarse-graining the global pool; Caputo memory is power-law and arises from substrate-internal slow-resource turnover. Substrates can carry both, neither, or one without the other.

**Mechanism vs manifestation:** $\gamma_B^{-1}$ is the dynamic-bath timescale (mechanism); the §22 Cobham wait $W_{n+1}$ is one manifestation; transient $\mathcal{D}_i$ deficits driving mode collapse is another.

**Open item raised:**
- **Bath-driven chimera onset:** can delayed global feedback $B(t)$ produce cluster-sync (chimera) states in an otherwise uncoupled or weakly competitive $\gamma$-graph? Standard chimera theory (§15) assumes *heterogeneous topological coupling*; this closure raises whether *bath-mediated mean-field coupling with finite recovery delay* is a second route to chimera, potentially substrate-class-distinguishing. Substrate-instancing question; lives in receipts only.

### §21 — $f(r)$ closed form (Toner-Tu active-stress closure)
**Type:** composition.
**Cite:** Toner–Tu (1995, 1998); Simha–Ramaswamy (2002); Marchetti et al. (*Hydrodynamics of soft active matter*, 2013).
**Bespoke step:** Closes the §21 residual "alignment-state-dependent correction $f(r)$ in $\beta/\alpha = (v_0^2\tau_R/D_{\text{trans}})[1+f(r)]$" open. Toner-Tu hydrodynamics gives an active pressure with two isotropic contributions — swim-pressure baseline and alignment-induced order-parameter pressure:
$$P_{\text{active}} = \frac{n\,v_0^2\,\tau_R}{d} + \zeta_0\,n\,|\mathbf{p}|^2$$
Identifying $|\mathbf{p}|=r$ (Kuramoto order parameter) and factoring out the baseline:
$$P_{\text{active}} = \frac{n\,v_0^2\,\tau_R}{d}\bigl[1 + C\,r^2\bigr],\qquad C = \frac{\zeta_0\,d}{v_0^2\,\tau_R},$$
giving $f(r) = Cr^2$. The active-coupling constant $C$ is substrate-dependent; **$\zeta_0$ can be positive (contractile substrates) or negative (extensile), so the sign of $C$ is itself a substrate-class signature**.

**Verification:**
- *Limit recovery:* $r\to 0$ ⇒ $f\to 0$, recovers baseline swim-pressure scaling $\beta/\alpha\sim v_0^2\tau_R/D_{\text{trans}}$ ✓
- *Dimensional:* $r$ dimensionless; $\zeta_0$ has dimension $[\text{velocity}^2]$ matching $v_0^2$, so $C$ and $f(r)$ are dimensionless ✓
- *Sign:* contractile ($\zeta_0>0$) unbounded; extensile ($\zeta_0<0$) requires $|C|r^2 < 1$ at large $r$ for $1+f(r)>0$.

**Substrate-class fingerprint via $C$:**
- $C\approx 0$: alignment-isotropic — informational substrates like QEC syndrome buffers (active stress not amplified by sync magnitude).
- $C>0$ (contractile): kinesin motor networks, biofilm matrices — high sync further amplifies stress.
- $C<0$ (extensile): actin networks, bacterial swarms — high sync reduces stress.

**Cross-register fall-out (load-bearing) — channel coupling at level-$n$ sync.** The §Heat-tax tower's three "independent failure paths" couple via the order parameter $r$:
- Channel 2 ($\beta\langle\Sigma_n\rangle$, active stress) scales as $1+Cr^2$ in level-$n$ sync.
- Channel 3 ($r_n$-drop, lost cooperative gain) is triggered when $r$ falls.

High $r$: *reduces* $L_{n+1}^{(0)}$ via gain-sharing (channel 3, stabilizing) but *amplifies* $\beta\langle\Sigma_n\rangle$ via $1+Cr^2$ (channel 2, destabilizing). **Opposing effects on $L_{n+1}$; the substrate-class active-coupling $C$ determines the balance.** Framework refinement: the three channels remain independent failure paths but two share $r$ as a common driver in opposing directions — to be foregrounded in §Heat-tax tower.

**Don't overclaim** (coincidence vs identity): exact cancellation of cooperative-gain reduction and active-stress amplification at some particular $r^*$ would be coincidence, not a guaranteed stabilization mechanism, without substrate-specific thermodynamic derivation.

**Open:** Substrate-class mapping of $C$ — which Character substrates settle at $C\approx 0$, $C>0$, or $C<0$? Substrate-instancing question; lives in receipts only.

### §22 — Spatial Jackson-network generalization (Kelly product-form closure)
**Type:** composition.
**Cite:** Jackson (1957); Kelly (*Reversibility and Stochastic Networks*, 1979); Burke (1956).
**Bespoke step:** Closes the §22 residual "multi-server / spatial Jackson-network generalization" open. The single-server Cobham priority-queue mapping (§22 Cobham closure) generalizes to a spatial Kelly network: the global budget $G_{\text{total}}$ becomes a network of local pools $G_k$ at spatial patches $k$, with Markovian routing $R_{k,l}$ between patches. Tower-level priority structure (Haken slaving across levels $n$) lives at each patch; spatial coupling enters via routing.

By Kelly's theorem (quasi-reversible routing): spatial steady-state is product-form
$$P(\mathbf{Q}) = \prod_k P_k(Q_k)$$
— each patch independently undergoes Cobham priority dynamics; spatial coupling re-emerges only in transient response.

**Verification:**
- *Limit recovery:* single patch ($k=1$, $R_{1,1}=1$) recovers the §22 Cobham closure ✓
- *Dimensional:* $R_{k,l}$ dimensionless; $W_{n,k}\in[T]$; $\sigma_{n,k}$ dimensionless ✓

**Cross-register reading (sharpened — not identity):** product-form breakdown (when local $\sigma_k\to 1^-$ induces inter-patch correlations) is *one mechanism* of spatial structure emergence — queueing-congestion-driven correlation. Turing-class reaction-diffusion patterns (§Pattern formation, Receipts §19) are a *different* mechanism — diffusion-reaction instability. Both produce spatial structure but they are not isomorphic: queueing breakdown produces correlations through bandwidth contention, Turing produces wavelengths through diffusion-reaction balance. Whether a substrate is queueing-driven or reaction-diffusion-driven (or both at different scales) is substrate-specific.

**Don't overclaim** (coincidence vs identity): local queueing singularity ($\sigma_k\to 1$) and local Complexity Wall ($\epsilon_k\to 1$) are coincident critical structures, not isomorphic without substrate-specific argument.

**Cross-register fall-out — the fourth Caputo connection (load-bearing).** Non-Markovian Caputo memory (Receipts §9; memory exponent $\beta_{\text{mem}}\in(0,1)$ — distinct from the active-stress $\beta$ in §Heat-tax tower) violates Kelly's quasi-reversibility assumption: fractional-memory correlations propagate across patches and the spatial product form fails. The critical interaction length $\ell_c(\beta_{\text{mem}})$ for product-form breakdown depends on the Caputo exponent.

**Four-way Caputo connection at the Wall:**
1. §9 — memory-exponent collapse $\beta_{\text{mem}}\to 0$ (foundational)
2. §21 — $\tau_R$ Green-Kubo divergence (integrand $\sim t^{-\beta_{\text{mem}}}$)
3. §21 — swim-pressure fingerprint $\beta/\alpha$ divergence (via $\tau_R$)
4. §22 — spatial Kelly-network product-form breakdown (this closure)

All four divergences at $\epsilon\to 1$ trace to one underlying parameter ($\beta_{\text{mem}}\to 0$). **The Caputo memory exponent is emerging as *the* load-bearing s-regime / Wall-approach control parameter** — the four-aspect Complexity Wall (thermodynamic / dynamical / informational / SOC-critical, §Pattern formation) gains a *fifth aspect* under the parameter that drives the other four. Framework-primitive observation foregrounded in compressed §Pattern formation.

**Open:** *(Closed.)* Quantitative form of $\ell_c(\beta_{\text{mem}})$ closed via CTRW / fractional diffusion (see Receipts §22 critical-length closure); reveals traffic-driven → frozen-topological transition as the spatial face of the Wall.

### §21 — $\tau_R$ substrate-neutral identification (Green-Kubo closure)
**Type:** composition.
**Cite:** Green (1954); Kubo (1957); Marchetti et al. (*Hydrodynamics of soft active matter*, 2013).
**Bespoke step:** Closes the §21 residual "$\tau_R$ substrate-neutral identification across substrate classes" open item. The rotational persistence time in the swim-pressure fingerprint $\beta/\alpha \sim v_0^2\tau_R/D_{\text{trans}}$ has a substrate-neutral closed form via Green-Kubo:
$$\tau_R = \int_0^\infty \langle\mathbf{u}(t)\cdot\mathbf{u}(0)\rangle\,dt$$
where $\mathbf{u}(t)$ is the unit-vector direction of the holding's active maintenance-work application in its state space — *not* an analogy across substrates but the same mathematical object instantiated on each substrate's continuous maintenance trajectory.

**Verification:**
- Dimensional: $\langle\mathbf{u}\cdot\mathbf{u}\rangle$ dimensionless; $\int dt$ yields $[T]$ ✓.
- Limit recovery: canonical Active Brownian Particles with rotational diffusion $D_R$ give $\langle\mathbf{u}(t)\cdot\mathbf{u}(0)\rangle = e^{-D_R t}$, integrating to $\tau_R = 1/D_R$ ✓.
- Sign: auto-correlation positive at $t=0$ ⇒ $\tau_R\ge 0$ ✓.

**Substrate-instance examples:**
- Mechanical / active matter: $\mathbf{u}(t)$ = literal self-propulsion direction; $\tau_R$ = rotational diffusion time (canonical).
- QEC: $\mathbf{u}(t)$ = trajectory direction of applied Pauli corrections in code space; $\tau_R$ = syndrome-buffer correlation time (duration a specific error chain dictates the decoding trajectory).
- Neural: $\mathbf{u}(t)$ = population-vector orientation in direction-coding cortex; $\tau_R$ = direction-coding persistence time.

**Don't overclaim** (mechanism vs manifestation): the Green-Kubo formula identifies $\tau_R$ as a single mathematical object across substrates (identity of mechanism); whether $\tau_R$ governs a *dominant* macroscopic stress in every substrate (manifestation) depends on substrate-specific embedding — whether active maintenance work propagates transversally to drive material/informational/structural stress.

**Cross-register fall-out (load-bearing — three-closure connection).** The Caputo closure (Receipts §9) gives memory exponent $\beta\in(0,1]$ on slow-resource correlations. For non-Markovian substrates ($\beta<1$), the Green-Kubo integrand decays as $\langle\mathbf{u}(t)\cdot\mathbf{u}(0)\rangle\sim t^{-\beta}$ and the $\tau_R$ integral **formally diverges**: every $s$-regime / glassy substrate has formally divergent $\tau_R$, hence formally divergent swim-pressure fingerprint $\beta/\alpha\sim v_0^2\tau_R/D_{\text{trans}}$. Real substrates impose finite-size structural cutoffs regularizing the integral; the cutoff scale is substrate-specific. **The §9 memory-exponent-collapse open near the Complexity Wall is the same phenomenon as a swim-pressure divergence at the Wall**, via the §21 Green-Kubo $\tau_R$ identification — three closures (Caputo memory, swim-pressure, $\tau_R$) name aspects of one $\beta\to 0$ phenomenon at $\epsilon\to 1$. Not a new open item; a connection foregrounded.

### §20 — Lyapunov function for frustration-free-but-not-PSD topologies (weighted relative-entropy form)
**Type:** composition.
**Cite:** Takeuchi (*Global Dynamical Properties of Lotka–Volterra Systems*, 1996); Redheffer (Volterra–Lyapunov stable matrices, 1985); Hofbauer–Sigmund (*Evolutionary Games and Population Dynamics*, 1998).
**Bespoke step:** Closes the §20 residual "Frustration-free-but-not-PSD $\gamma$-graphs: whether weaker Lyapunov exists" open. For frustration-free kernels where the gauged $\gamma$ is not PSD but is *diagonally stable* (Volterra–Lyapunov stable), there exists a strictly positive diagonal weight matrix $W = \text{diag}(w_i)$ such that $W\gamma + \gamma^T W$ is PSD. Volterra–Lyapunov stable matrices are a strict superset of PSD: $W=I$ recovers PSD; some non-PSD matrices admit non-trivial $W$ satisfying the symmetric-part condition. The weighted relative-entropy Lyapunov:
$$V(\{x\}) = \sum_i w_i\bigl[x_i - x_i^* - x_i^*\ln(x_i/x_i^*)\bigr]$$

**Verification:**
- $\partial V/\partial x_i = w_i(1 - x_i^*/x_i) \Rightarrow \partial V/\partial x_i|_{x^*} = 0$ ✓
- $dV/dt = \sum_i w_i(x_i - x_i^*)[(G_{0,i} - L_i) - \sum_j\gamma_{ij}x_j]$; substituting fixed-point relation and using the symmetric-part identity $x^T A x = \tfrac{1}{2}x^T(A+A^T)x$:
$$\frac{dV}{dt} = -\frac{1}{2}\delta x^T (W\gamma + \gamma^T W)\,\delta x \le 0$$
with equality only at $x = x^*$ by PSD of the weighted symmetric form ✓
- *Limit recovery:* $w_i = 1$ exactly recovers the §20 PSD closure (relative-entropy form).

**Cross-register reading — interpretation, not derivation.** The weights $w_i$ *could be read as* per-mode rescaling of effective slow-resource turnover $\gamma_{s,i}$ (§13): a holding frustration-free but not natively PSD might sustain globally-attracting NESS if its per-mode timescales tune to satisfy diagonal stability. **No derivation forces $w_i \leftrightarrow \gamma_{s,i}$ identity** — this is an interpretive reading of the mathematical existence of $W$. Whether substrates natively *find* this $W$ is a separate (substrate-conditional) question.

**Don't overclaim** (mechanism vs manifestation): existence of $W$ guarantees Lyapunov stability is mathematically *possible* (mechanism); whether substrates *find* the W natively (manifestation) requires substrate-specific argument. Auto-tuning to diagonal stability and SOC-criticality at coincident parameter boundaries is *coincidence* in general — identity would require substrate-thermodynamic derivation.

**Open item raised:**
- Substrate-class auto-tuning to diagonally-stable $W$: which substrates natively settle into $\gamma_{s,i}$ distributions satisfying diagonal stability? Substrate-instancing claim added to cdv1_compressed.

### §9 — Caputo fractional memory for $\mathcal{D}$ (non-exponential closure)
**Type:** composition.
**Cite:** Caputo (fractional derivatives, 1967); Mittag-Leffler (1903); Podlubny (*Fractional Differential Equations*, 1999); Mainardi (*Fractional Calculus and Waves in Linear Viscoelasticity*, 2010); Metzler–Klafter (anomalous diffusion review, 2000); Pottier (non-Markovian fluctuation-dissipation, 1985).
**Bespoke step:** Closes the §9 non-exponential-memory open item for glassy / $s$-regime aging substrates. The §9 $\mathcal{D}$-kernel memory generalizes from exponential to Mittag-Leffler relaxation: the Caputo derivative ${}^C\!D^\beta$ with exponent $\beta\in(0,1)$ governs slow-resource dynamics, giving
$$\Gamma_{AB}(\tau) = \Gamma_0\,E_\beta(-(\tau/\tau_c)^\beta),\qquad K(\tau)\sim\tau^{-\beta}/\Gamma(1-\beta)\text{ for }\tau\gg\tau_c.$$
Markovian limit $\beta=1$ recovers $E_1(-\tau/\tau_c)=e^{-\tau/\tau_c}$ — the original §9 exponential closure. Off-Markovian $\beta<1$ gives stretched-exponential / power-law decay, canonical glassy-substrate signature.

**Three-way identity** (load-bearing cross-register fall-out):
$$\boxed{\alpha_s \;=\; \beta \;=\; \text{anomalous heavy-traffic exponent}}$$
- CK $s$-regime aging diagonal slope $\alpha_s$ (Receipts §4): non-Markovian FDT (Pottier 1985; Mainardi 2010) directly identifies the Caputo exponent with the aging slope.
- Heavy-traffic queue-scaling anomalous exponent (Receipts §22): non-Markovian (fractional-Brownian) arrivals generalize Kingman's $1/(1-\rho)$ to $1/(1-\rho)^\beta$ with the *same* exponent.
- Same parameter, three measurement registers (FDR diagonal / memory kernel / queue tail). The framework's existing $\alpha_s$↔heavy-traffic identification sharpens to *identity*.

**Substrate-class fingerprint via** $\beta$:
- $\beta=1$: QEC syndrome streams, M/M/c queues, simple Markovian substrates.
- $\beta\in(0.5,1)$: viscoelastic biological substrates, biofilms, polymer networks.
- $\beta\approx 0.5$: anomalous subdiffusion in supercooled liquids, free-particle Lévy.
- $\beta\to 0$: logarithmic extreme aging, deep-glassy substrates.

**Chit's orbit-affinity face** (structural sharpening that follows from closure). The chit's per-stochastic-transition reading $\ln(k_+/k_-)$ (Markovian Crooks rate-ratio, Receipts §2) generalizes to per-orbit:
$$\text{chit}_{\text{orbit}} = \oint \frac{v(\theta)}{D(\theta)}\,d\theta$$
which is precisely the continuous-orbit Schnakenberg affinity (Receipts §16). The two readings agree at $\beta=1$; for $\beta<1$ the orbit reading is canonical. The rate-ratio reading is the Markovian specialization of a more general orbit-affinity reading — not a tension; a sharpening.

**Open item raised by this closure** (added to cdv1_compressed substrate-instancing list):
- **Memory-exponent collapse near Complexity Wall**: do substrates approaching $\epsilon\to 1$ generically migrate $\beta\to 0$ (extreme aging)? If yes, the four-aspect Wall (thermodynamic / dynamical / informational / SOC-branching) gains a fifth coupled critical reading.

### §14 — Meta-ledger chaos at Complexity Wall (NRT conditionally predicted; generic-Hopf condition owed)
**Type:** composition + open.
**Cite:** Ruelle–Takens (turbulence onset, 1971); Newhouse–Ruelle–Takens (1978); standard chaos-via-quasi-periodicity literature.
**Bespoke step:** Framework prediction: past the Complexity Wall ($\epsilon\ge 1$), the meta-ledger flow generically becomes chaotic (strange attractor, positive maximal Lyapunov exponent), instancing the Newhouse–Ruelle–Takens scenario at the tower-level oscillatory modes; this also subsumes the Ruelle–Takens secondary/tertiary bifurcation-sequence open item. **NRT apparatus (closed):** a quasi-periodic flow on $T^k$ with $k\ge 3$ generically perturbs to a strange attractor (Newhouse–Ruelle–Takens 1978). **Generic-Hopf-per-tower-ascent condition (open):** NRT requires $\ge 3$ independent limit-cycle modes coupling; the framework explicitly names Hopf only at $k_{\text{frust}}$ onset, not generically at each tower ascent. Whether tower ascents generically introduce new limit-cycle modes is the residual open piece — needed for the NRT hypothesis to be met past the Wall.
**Open:** Demonstration that meta-ledger ascents generically instance new limit-cycle modes (Hopf bifurcations per level), validating the NRT scenario hypothesis past the Complexity Wall.
