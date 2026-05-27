# MPA-Character (operational source of truth)

**Status:** Claim-only operational source of truth, under falsifiability discipline: every claim states a predicted measurement on a named substrate (or substrate class) and is mpa-legal (dynamical quantities flow with the operating point; no inert constants in places the physics requires flow).

**Companions:**
- `cdv1_unabridged.md` — prose-and-prior-art paper. Allowed to lag this file by at most one closure.
- `cdv1_receipts.md` — line-keyed justifications and falsifier formalisations.
- `FALSIFICATION.md` — the open attack front. Read this when asking *what are we trying to break?*

If this file disagrees with `v9_compressed.md` on shared primitives, treat as bug. If this file disagrees with receipts on a falsifier formalisation, treat as bug.

**Scope.** Continuous physical economics of sustained NESS traversal — what a structure is *being* against a bath. v9 specifies topology, edge shears $\gamma_{AB}$, and discrete operator algebra; this file specifies the driven-dissipative dynamics that traverse it.

---

## Setting and primitives

A **coherence** is a macroscopic pattern of continuation maintained against natural dissolution. A **holding** is the continuous extraction of entropy or application of work that maintains it.

**Substrate primitives.** Maintenance budget $G_0$ (unsaturated active work supplied per unit time, scales with $D$; laser-analogue small-signal gain). Decay rate $L$ (spontaneous relaxation rate to bath; cavity loss). Signed edge structure $\gamma_{AB}$ on the mode graph (inherited from v9).

**Derived primitive (operational anchor): $\text{chit} = \ln(G_0/L)$** — headroom above threshold. The framework's operational content keys to chit.

**Topological invariant: $k_{\text{frust}}$.** Receipts §10 lists $k_{\text{frust}}$ as derived (heteroclinic-cycle consequence of the universal kernel + Harary structural balance). Its operational content — *the stationary state is irreducibly a NESS: a topologically-forced circulating current (broken detailed balance)* — survived the R1/R2/R3 falsification ladder (Receipts §846 PROMOTED; FALSIFICATION.md Finding 4). The operational content stands at the level of v9 §Three typed objects + the refinement below; elevation to a numbered framework primitive awaits a real cross-substrate instance (§Open items). See §k_frust drain for content.

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

The log form is required by stochastic thermodynamics: $\ln(k_+/k_-)$ is the Crooks rate-ratio entropy production per stochastic transition.

**Markovian / orbit-affinity faces.** The rate-ratio reading is the Markovian specialisation of a per-orbit reading: $\text{chit}_{\text{orbit}} = \oint v(\theta)/D(\theta)\,d\theta$ — the continuous-orbit Schnakenberg affinity. The two faces agree at $\beta_{\text{mem}}=1$; for non-Markovian (Caputo-memory) substrates the orbit-affinity face is canonical.

**Saturation.** In sustained NESS, saturated gain clamps to loss: $G_{sat} = L$. Chit measures the *unsaturated* excess — headroom above threshold, not operating point.

**Threshold behaviour.** chit $\gg 0 \Rightarrow c$; chit $\to 0^+ \Rightarrow s$; chit $< 0 \Rightarrow r$.

**Limit-point status.** chit $= 0$ is a critical limit, not an attainable operating state. Substrates approach it asymptotically; the $s$-regime is a finite window around the limit. Width: drive-axis substrates carry irreducible thermodynamic floor ($kT/q$); damping-axis vanishes in deterministic limit (F-003-rlc $Q=0.5$ zero).

**Domain (open interval, not endpoints).** Observables are continuous on an open interval; Boolean/discrete logic is the degenerate limit at the endpoints ($0, 1, \infty$). chit is the per-event instance — continuous $\ln(G_0/L)$ whose Boolean endpoint is the bit ($\ln 2$; §Thermo-info accounting). An *attained* endpoint has left the domain, so it surfaces as a NaN falsification tripwire, not a fillable value. (Scope statement; not the demoted claim that the bit↔chit *mapping* is substrate-independent — §Open conjectures.)

## Fraying sequence

Load monotonically reduces the chit:

> Saturated holding (chit $\gg 0$, $c$, resilient) → visible strain (chit $\to 0^+$, $s$) → mode-hopping (chit $\approx 0$, $s$ multistability) → sub-threshold collapse (chit $< 0$, $r$).

Detailed fluctuation theorem $P(\sigma)/P(-\sigma) = e^\sigma$: anomalous fraying-resistance trajectories are exponentially rare in $|\sigma|$. The fraying sequence is the *typical* trajectory.

## gFDR signatures

Coherences are path-dependent NESS; equilibrium FDR fails. The Apparatus reads spontaneous fluctuations $C(\tau)$ and response $\chi(\tau)$. Harada–Sasa: integrated FDR-violation = steady-state entropy production rate $\langle\sigma\rangle$.

| Regime | Chit | Invariant | Reading |
|---|---|---|---|
| $c$ | $\gg 0$ | $X_c = 0$ | suppression / narrow horizontal locus |
| $s$ | $\to 0^+$ | $\alpha_s$ slope of aging segment | CK ratio |
| $s$ | $\to 0^+$ | $P_s = \lim_\tau C(\tau)/C(0)$ | plateau height |
| $r$ | $< 0$ | $X_r = 1$ | unit-slope FDR |
| $k_{\text{frust}}$ | non-stationary | drive-independent cycle affinity; complex Jacobian spectrum | spin-glass loop signature; see §k_frust drain |

$\alpha_s$ and $P_s$ are the load-bearing cross-substrate observables.

**$s$-regime FDR is two-step** (Receipts §gFDR staged candidate). Quasi-equilibrium ($X=1$) on short lags; FDR-violated aging ($X<1$, slope $\alpha_s$) on long lags. A short-lag $X=1$ reading alone does not place a substrate in $r$ — the long-lag aging segment is the c/s/r discriminator. (Survived 2026-05-20 on driven-critical RFIM: $X=0.118$ via self-overlap + staggered-field estimator. Not the collective magnetisation, which is soft-mode-dominated near criticality and gives unstable $X$.) $X$ is recoverable by the five-vector inversion (mpa-conform), domain-gated against out-of-family inputs — Receipts §gFDR; FALSIFICATION FINDING 2 closed 2026-05-21.

**Two conjugate FDR frames** (Receipts §gFDR/§16 two-frame; promoted 2026-05-22). The FDR-violation reads from two conjugate force–flux frames. *External-probe:* (amplitude × external field $h$) → violation factor $X$ ($\alpha_s, P_s$ the aging observables); needs a probe. *Self-probe:* (current $J$ × intrinsic affinity $A$, in nats) → violation factor is the TUR-tightness $T=\langle\sigma\rangle\,\mathrm{Var}(J)/(2\langle J\rangle^2)$, measurable core $\mathrm{SNR}_J=\langle J\rangle^2/\mathrm{Var}(J)\le\langle\sigma\rangle/2$; **dimensionless by construction**, **defined iff a current exists** ($k_{\text{frust}}$-bearing). Harada–Sasa bridges them in principle ($\int$FDR-violation $=\langle\sigma\rangle=J\!\cdot\!A$). The operational claim is **same regime verdict where both frames are computable** — confirmed on a real substrate (class-B laser: both frames flag NESS; driven_ring: self-frame closes with exact $\langle\sigma\rangle=J\!\cdot\!A$). Their *disagreement* is the falsifier. The frames are *different functionals* (verdict-agreement, not magnitude identity); the exact cross-frame $V_{ext}=\langle\sigma\rangle$ via velocity-frame Harada–Sasa is a refinement, not a gate.

**Surface-code identification (load-bearing positive instance).** Distance-3 rotated memory-Z syndrome streams trace clean $s$-aging at sub-threshold operation; placing surface-code QEC in the Cugliandolo–Kurchan universality class. The $s \to r$ migration across the physical-error threshold is the framework's primary cross-substrate test. Falsifier (Receipts §4): (a) syndrome FDR shows unit slope sub-threshold (no CK signature); or (b) FDR shape persists unchanged across threshold crossing.

**Substrate-conditional reading rules** (inherited from v9 §F):
- *Markovian sign caveat:* stiff/Markovian substrates invert $\gamma$ signs (kernel-width artefact); use $|\gamma|$ + FDR shape jointly. For $k_{\text{frust}}$-bearing content this is chirality-flipping (sign reverses); chit-axis content is preserved.
- *Detection-event preprocessing:* for non-local readouts, $e_i(t) = s_i(t) \oplus s_i(t-1)$; trail by EMA against detection events.

**Apparatus measurement notes** (from FALSIFICATION.md). Do not infer X from a single linear FDR slope on aging loci — it biases up (kww_oracle calibration: prescribed $X=0.2$ reads 0.47 via single-slope vs 0.26 via segmented fit). The 5-vector inversion (q_EA, $\tau_\alpha$, $\beta_{\text{KWW}}$, $\tau_\beta$, $X$) is owed; until landed, X-bearing verdicts read at the raw FDR-locus-slope layer, where the grinder is faithful (validated to ~2% on two_temp_ou prescribed-X cells).

## Capacity dynamics

v9 supplies the static structural ceiling $|\Gamma^*| \le \sqrt{2D/(\alpha\,\gamma_{min}\,d_{avg})}$. Character supplies the dynamic conjugate:

$$\sum_{i \in \Gamma^*} L_i \le G_{total}\,\eta(\Gamma^*)$$

with cross-saturation efficiency $\eta(\Gamma^*) \in (0,1]$, $\eta \to 0$ at the $\sqrt{D}$ Hopfield ceiling. Violation forces sparsification or sub-threshold phase transition.

**Erlang-B closure.**
$$\eta(\Gamma^*) = 1 - B(c,\rho), \qquad B(c,\rho) = \frac{\rho^c/c!}{\sum_{k=0}^c \rho^k/k!}$$
with $c = \lfloor|\Gamma^*|_{\text{crit}}\rfloor$ and $\rho$ the effective offered load on the mode-slot pool.

**Hard-vs-soft falsifier per substrate class** (Receipts §5/§22). Soft substrates: $\eta = 1 - B(c,\rho)$, smooth crossover. Hard-wall substrates (surface code at logical-error onset): $\eta = \mathbb{1}[|\Gamma^*| \ge c]$ — one error breaks the code. Falsifier: behavioral/cognitive substrate exhibiting sharp Hopfield-snapping instead of Erlang-B tails; or QEC-class substrate showing soft Erlang-B blocking instead of abrupt threshold.

## Heat-tax tower

v9's Compression Axiom contracts informational structure ($\epsilon = \|\mathcal{C}\|_{op} < 1$). Character routes the thermodynamic exhaust:

$$L_{n+1} = L_{n+1}^{(0)} + \alpha_\sigma\langle\sigma_n\rangle + \alpha_\Sigma\langle\Sigma_n\rangle$$

Two effect axes propagate level-$n$ activity to level $n+1$:
- $\alpha_\sigma\langle\sigma_n\rangle$: heat from level-$n$ flow as ambient noise to level $n+1$.
- $\alpha_\Sigma\langle\Sigma_n\rangle$: active stress from level-$n$ maintenance as mechanical/informational/structural stress on level $n+1$.

Heat-tax coupling Landauer-pinned: $\alpha_\sigma(\epsilon) = \alpha_{\sigma,0}(1-\epsilon)$. Cumulative tower tax to depth $N$ scales as $1-\epsilon^N$; at $\epsilon \to 1$ per-level Landauer heat vanishes (no erasure) while cumulative informational mass $\Phi_{\text{total}} = \Phi^{(0)}/(1-\epsilon)$ diverges — the **Complexity Wall** lives in the cumulative mass.

**Meta-ledger flow construction** (Receipts §6.5). The recursion is the level-to-level map on the space of slow-manifold generators: at level $n$, Mori–Zwanzig projection $\Pi_{\text{slow}}$ onto the slow manifold yields $\mathcal{A}_n$; heat-tax substitution into level-$(n+1)$ induces $\mathcal{A}_n \mapsto \mathcal{A}_{n+1}$. Wilson–Polchinski-style functional RG on the space of generators; $\epsilon$ is the leading IR linear-stability eigenvalue. $\Pi_{\text{slow}}$ *is* the conjugating isometry $\phi$ of v9's Wilson–Kadanoff structural-equivalence statement.

**Three independent fraying channels.** Sustained level-$(n+1)$ coherence requires $\ln(G_{0,n+1}/L_{n+1}) > 0$. Fraying at level $n$ inflates $L_{n+1}$ via:
1. $\alpha_\sigma\langle\sigma_n\rangle$ heat-tax spike (above).
2. $\alpha_\Sigma\langle\Sigma_n\rangle$ active-stress spike (§Adoption catalogue, active-stress).
3. $r_n$ drop in level-$n$ collective sync, raising $L_{n+1}^{(0)}$ via lost cooperative gain-sharing (§Adoption catalogue, synchronization).

By the Cobham/Kleinrock priority-queue mapping (§Adoption catalogue, heavy-traffic; Receipts §22), all three are faces of Cobham wait-time inflation $W_{n+1}=W_0/[(1-u_n)(1-u_{n+1})]$ across tower-level priority classes. The $u\to 1$ queueing singularity is coincident with $\epsilon\to 1$; for rate-distortion-optimal encoding $u_n = \epsilon_n$ (posit P4 below).

**Channels 2 and 3 share $r$ as driver in opposing directions.** Toner–Tu gives active-stress correction $f(r) = Cr^2$, so the active-stress channel scales as $1+Cr^2$ in level-$n$ sync; the cooperative-gain channel is triggered by $r$-drop. Substrate active-coupling $C$ (contractile $>0$, extensile $<0$, isotropic $\approx 0$) determines balance.

## Operators in continuous register

v9's discrete operators have continuous-traversal shadows.

**$C_{\text{Character}}$ (merge).** Adiabatic deformation from $\gamma_{AB} \approx 0$ to $\gamma_{AB} \ll 0$ while sustaining NESS. Adiabaticity bound: deformation rate slow vs $L$. Failure mode: forced non-adiabatic merge spikes $\sigma$, drops one or both modes sub-threshold. Information-geometric reading: merge succeeds iff a Fisher-information geodesic stays on the above-threshold manifold. Discrete shadow recovers v9 Theorem 9 in the sharp-threshold limit: $\Delta_C(A,B) = 1$ iff $\gamma_{AB} > 0 \land D < \gamma_{AB}$.

**$R_{\text{Character}}$ (sever).** Quench trajectory: choke $G_0$ (demand-load) or open mode to bath ($L\uparrow$, decay-load). Native edge dissolution — $\gamma_{AB}\rho_A\rho_B$ vanishes as $\rho_A \to 0$. v9 Landauer bound is the asymptotic discrete limit.

## Universal two-mode kernel

$$\frac{\partial \rho_A}{\partial t} = (G_{0,A} - L_A)\rho_A - \gamma_{AB}\,\rho_A\rho_B + \mathcal{D}[\rho_A,\rho_B;\gamma_{AB}]$$

(symmetric for $\rho_B$; $\gamma_{AB}<0$ contributes positively to $\partial_t \rho_A$.) The $\mathcal{D}$-kernel admits three closures.

*Lamb stationary closure.* $G_{0,A}^{\text{eff}} = G_{0,A}/(1+\sum_{j\ne A}\rho_j/\rho_{\text{sat}})$ — multi-mode laser saturation.

*Dynamic bath inversion.* $B(t)\in[0,1]$ promoted to dynamical coordinate; Mori–Zwanzig projection-out gives non-Markovian history integral; fast-bath limit $\gamma_B\to\infty$ recovers Lamb. $\gamma_B^{-1}$ identifies as bath-server service time in the Cobham mapping (§Adoption catalogue, heavy-traffic; Receipts §22).

*Caputo fractional memory.* For glassy / $s$-regime aging: Mittag-Leffler kernel $\Gamma_{AB}(\tau) = \Gamma_0\,E_{\beta_{\text{mem}}}(-(\tau/\tau_c)^{\beta_{\text{mem}}})$, $\beta_{\text{mem}}\in(0,1]$. $\beta_{\text{mem}}=1$ exponential; $\beta_{\text{mem}}<1$ power-law decay.

**Three-register identity for $s$-regime exponent** (substrate-class conditional). Under the *common-exponent condition* — substrate's slow-resource memory kernel and load-arrival process share a single anomalous-diffusion exponent —
$$\alpha_s = \beta_{\text{mem}} = \text{anomalous heavy-traffic exponent}.$$
Composes Pottier (non-Markovian FDR identifying Caputo $\beta_{\text{mem}}$ with the aging slope) with Norros (fractional-Brownian heavy-traffic generalises $1/(1-\rho)$ to $1/(1-\rho)^{\beta_{\text{mem}}}$).

**Falsifier (Receipts §22, reframed per FALSIFICATION.md Finding 3).** The original mm1_queue falsifier ($\alpha_s = \frac{1}{2}$ at $\rho \to 1$) is *mis-specified* — a category error mixing planes: $\frac{1}{2}$ is the reflected-BM time-scaling (Hurst) exponent in the C-vs-lag plane; $\alpha_s$ is the FDR effective-temperature slope in the $\chi$-vs-C plane. Two reframed routes: (i) measure C-decay-time scaling vs $(1-\rho)$ in the C-vs-lag plane — where the $\frac{1}{2}$ lives — on Markovian vs non-Markovian queues; predicted exponent matches the substrate's memory class. (ii) Extend the sampling window to $\sim(1-\rho)^{-2}$ on M/M/1 (Markovian, reversible) and verify $X\approx 1$ (reversibility), not aging $X<1$. The structural tension — "heavy-traffic M/M/1 maps to $s$-regime, but reversibility forces $X=1$" — is the sharp form of this test; the cleaner instance is `ising_equilibrium` (equilibrium critical slowing must read $X=1$). Predicted measurement: on Markovian–Poisson reversible substrates exhibiting heavy traffic, raw FDR slope $\approx 1$ across $\rho \to 1$.

**Composite catalogue** (sweep $\gamma_{AB}$):

| Regime | $\gamma_{AB}$ | Phase relationship |
|---|---|---|
| $c$–$c$ aligned | $\ll 0$ | in-phase locked (Hebbian / force chain) |
| $c$–$s$ mentor | $< 0$, asymmetric | driven entrainment, non-reciprocal, priority queue |
| $c$–$c$ orthogonal | $\approx 0$ | unlocked / phase drift |
| $c$–$c$ opposed (lock) | $> 0$, $K > \Delta\omega$ | anti-phase locked |
| $c$–$c$ opposed (split) | $> 0$, $K < \Delta\omega$ | competitive desync (pitchfork) |
| $k_{\text{frust}}$ | $N \ge 3$ obstructive | frustrated sync |

## k_frust drain

**Definitional core (Receipts §846 PROMOTED, 2026-05-20).** The stationary state is irreducibly a NESS: a topologically-forced circulating current (broken detailed balance). The deterministic flow realises this in two sub-regimes by sign of the relaxation eigenvalue's real part — both are $k_{\text{frust}}$; **the complex spectrum (irreducible rotation), not fixed-point non-existence, is the invariant**:

- *Stable circulating focus* (Re $<0$, complex spectrum): spirals into a NESS that still circulates ($J\ne 0$).
- *Repelling focus + attracting limit cycle* (Re $>0$): cooperative fixed point repels onto attracting orbit.

**Affinity vs magnitude** (Receipts §13/§16/§Topological-drain mpa-LEGAL audit, 2026-05-20). Drive-independence is a property of the cycle **affinity** $A_C = \oint v/D = \ln(\prod_+ k / \prod_- k)$ (intensive log-rate-ratio, the thermodynamic force), forced nonzero regardless of $D$. The current **magnitude** $J_{ss}$ scales with absolute kinetic rates and therefore flows with chit (R1 measured: $J$ grew $1.3\times 10^{-2} \to 2.5\times 10^{-1}$ as $G_0$ swept 0.9 → 2.0). Falsifier reads: "$J$ becomes $D$-(noise)-dependent OR resolves to detailed balance" — not "drive-dependent" (pump-dependence of magnitude is legal).

**Survived falsification ladder** (Receipts §846 R1/R2/R3):
- *R1 — operating-point sweep.* $J$ sign-definite + drive-independent across drive/headroom; scales only with wiring. At chit$=0.010$, $J$ reads 5.8σ above matched reciprocal control.
- *R2 — Wall round-trip, dual lens.* Discrete (sign-class) representation: scanning Wall corruption to 8× the destruction anchor, frustration is never destroyed — strong chaos only flips chirality sign (a reversed loop is still frustrated).
- *R3 — gradient/detailed-balance test.* Frustrated-loop Jacobian spectrum is complex at all coupling; matched cooperative control reads real-spectrum.

**Predicted measurements on a new substrate** (the falsifier surface):
1. Frustrated-loop coexistence-Jacobian has complex eigenvalues at every coupling in the surviving operating range.
2. $J$ is sign-definite, $D$-noise-invariant, and scales (only) with absolute kinetic rates.
3. After strong-chaos Wall round-trip, chirality may flip but $|J|$ recovers; detailed-balance recovery (real spectrum) is forbidden while wiring is intact.

**gFDR signature.** Transient negative response $N_f$ in loop-level apparatus (noting that $N_f$ is a τ_obs-conditional observer-shadow, weaker than the intrinsic $J$ meter; do not run a kill-shot on $N_f$ alone).

## Relaxation-oscillation register (stability)

The §Bridge eigenvalue's real part sets the regime; the full complex structure governs perturbation recovery. Above threshold a single-mode coherence is 2D in local linearisation (field × slow-resource) with a complex-conjugate pair — the relaxation-oscillation (RO) regime. Exact forms (Lamb closure; mpa-legal, validated to machine precision against the class-B laser Jacobian; Receipts §13):
$$\gamma_{RO} = \tfrac{\gamma_s}{2}e^{\text{chit}}, \quad \omega_{RO} = \sqrt{2L\gamma_s(e^{\text{chit}}-1) - \tfrac{\gamma_s^2}{4}e^{2\text{chit}}}, \quad Q = \sqrt{\tfrac{2L(e^{\text{chit}}-1)}{\gamma_s} - \tfrac{e^{2\text{chit}}}{4}}\;e^{-\text{chit}}.$$

**Non-monotonic $Q$ = cycles-of-headroom** (chit-conjugate: chit reads *whether* threshold is cleared, $Q$ reads *how many cycles* of natural oscillation the headroom buys). $Q\to 0$ at both ends (chit $\to 0^+$ and chit $\to \infty$), peaking at **chit $= \ln 2$**; underdamped only in a mid-chit band, overdamped at both ends — the class-B picture ($s$-threshold is critical *slowing*, deep-$c$ damps RO out), not "many cycles deep in $c$."

**Per-regime attractors.** $c$-deep stable focus; $c$-mid stable spiral at $\omega_{RO}$; $s$ centre manifold at threshold (algebraic settling = CK aging — $P_s$ = slow-manifold amplitude, $\alpha_s$ = slow-eigenvalue residual scaling against saturating gain; the isolating $\Pi_{\text{slow}}$ is the meta-ledger level-projection read at within-level scale); $r$ stable origin; $k_{\text{frust}}$ circulating focus / limit cycle. Codim-1 bifurcations: transcritical at chit $=0$ ($c\leftrightarrow r$), pitchfork at $\gamma_{AB}=\gamma_c$, Hopf at obstructive-$\gamma$ onset; codim-2 normal forms and the Wall-forces-NRT delay-Hopf chain in Receipts §14.

**Active/passive probe = on/off resonance.** Probes within $\gamma_{RO}$ of $\omega_{RO}$ are $Q$-amplified (active); off-resonance probes are passive baseline; boundary linewidth $\gamma_{RO}$. Active-probe channel bandwidth $B\sim\gamma_{RO}\propto e^{\text{chit}}$ and S/N $\sim Q$ (non-monotonic) — channel capacity peaks at intermediate headroom, not deep in $c$.

**Open prediction** (mpa-legal fix, 2026-05-20): deep-$c$ phase-lock collapse. Deep in $c$, $Q\to 0$ restores direct lock ($K_{AB}\propto(1+4Q^2)^{-1/2}\to 1$); over-provisioned holdings may collapse multi-mode independent-memory capacity (locked modes cannot store orthogonal trails). Falsifier and named substrate owed (§Open items).

## Thermodynamic and informational accounting

Stochastic thermodynamics and information theory consolidate into one dual ledger; the borrowed derivations (TUR, Schnakenberg, channel capacity, rate-distortion, Sagawa–Ueda) are in Receipts §16/§17.

- **Entropy production.** Detailed fluctuation theorem $P(\sigma)/P(-\sigma) = e^\sigma$ (Crooks); integrated FDR-violation $=\langle\sigma\rangle$ (Harada–Sasa, §gFDR).
- **TUR-tightness fingerprint.** $T = \langle\sigma\rangle\,\text{Var}(J)/(2k_B\langle J\rangle^2)$ varies by substrate class (biological active matter $T\approx 1$; engineered queues $T\gg 1$). Falsifier (Receipts §16): nominally same-class substrates with arbitrary $T$.
- **Schnakenberg affinity.** $\langle\sigma\rangle = \sum_C J_C\ln(\prod_+k/\prod_-k)$; for limit cycles $\sigma_{\text{frust}} = J_{ss}\oint v/D\,d\theta$. $k_{\text{frust}}$'s drive-independence lives at the affinity $\oint v/D$; magnitude $J_{ss}$ flows with chit (§k_frust drain).
- **Predictive information** $I_{\text{pred}} = I(\text{past};\text{future})$ — third coherence observable alongside chit and $Q$. Extended second law $\langle\sigma\rangle \ge -\Delta I$ (Sagawa–Ueda).

**Bit/chit dual ledger** (per-row measurements; the framework's natural thermo↔info correspondence):

| Axis | Thermodynamic | Informational |
|---|---|---|
| Per-event | chit $= \ln(G_0/L)$ | bit $= \ln 2$ |
| Per-rate | $\langle\sigma\rangle$ | $I_{\text{pred}}$ |
| Precision | TUR | channel capacity |
| Compression | heat-tax tower | rate-distortion tower |
| Coupling | $\langle\sigma\rangle \ge -\Delta I$ | (same bound, dual reading) |

**Optimal-encoding identity** (posit P5). $\langle\sigma\rangle - \langle\sigma\rangle_{\min} \ge \gamma_s\,\chi$, with $\chi = C_\mu - I_{\text{pred}}$ (cryptic order; $C_\mu$ = $\varepsilon$-machine structural complexity), equality at the rate-distortion-optimal limit. **Optimal-encoding Rosetta:** $\chi = \Delta_n = \langle\sigma\rangle_{\text{excess}}/\gamma_s$ — one quantity, three registers (information / queueing / thermodynamic). Falsifier (Receipts §17/§20): a substrate where $I_{\text{pred}}$ scaling (with chit, $Q$, internal-model richness) deviates from its thermodynamic dual — *also* the per-substrate-class fingerprint falsifier (one falsifier, two readings). Whether the dual *mapping* is itself substrate-independent → §Open conjectures.

## Adoption catalogue

Ten cross-framework registers were adopted into the Character projection (the 2026-05-10 cascade; methodology and per-register provenance in [`translating FDR.md`](translating%20FDR.md)). Each row gives the borrowed register, MPA's one-phrase mapping, the load-bearing observable that survives substrate-stripping, its falsifier, and the receipts entry holding the apparatus. As in v9's Composite catalogue, per row MPA's contribution is a unifying mapping; per table it is that one regime+kernel rule-set generates these phenomena across fields with no shared microphysics. Claims too heavy for a row are promoted below; the five posits are tabled in §Five leading-order posits.

| Register | MPA mapping | Load-bearing observable | Falsifier | Receipts |
|---|---|---|---|---|
| Damping / resonance | RO trichotomy = $c/s/r$ damping shadow | $\gamma_{RO},\omega_{RO},Q$ (§RO register) | mpa-legal landed | §13 |
| Attractor classification | regimes ↔ attractor types | per-regime attractor (§RO register) | — | §14 |
| Synchronization | $\gamma_{AB}$ sign → in/anti-phase lock; $K_{AB}\propto(1+4Q^2)^{-1/2}$ | two independent transitions (chit-onset, Kuramoto $K_c$); collective $r$; chimera | chimera-state SBN substrate, or only uniform sync/incoherence accessible (§15) | §15 |
| Nonequilibrium thermo | holdings are trajectory-NESS | $\langle\sigma\rangle$, Schnakenberg affinity, TUR-tightness $T$ (§Thermo-info) | same-class arbitrary $T$ (§16) | §16 |
| Information theory | thermo↔info dual ledger (§Thermo-info) | $I_{\text{pred}}$, channel capacity, cryptic order $\chi$ | $I_{\text{pred}}$ scaling breaks the dual (§17) | §17 |
| Self-organized criticality | chit-zero = SOC attractor in parameter space; Galton–Watson $\mu = e^{\text{chit}}$ (P2) | avalanche $\tau\approx 3/2$; meta-ledger branching $\to 1$ at $\epsilon=1$ | stable $\tau\ne 3/2$ on timescale-separated NESS, or branching $\ne 1$ at $\epsilon=1$ (§18) | §18 |
| Dissipative structures | chit-zero crossing = Prigogine formation transition; chit = Haken order parameter | Turing wavelength (non-reciprocity + autocatalysis $\gamma_{ii}<0$ + $D_B\gg D_A$) | Turing three-condition failure (§19) | §9, §19 |
| Control theory | holding = plant+controller closed loop; internal-model principle | four-axis observable (chit, $Q$, $I_{\text{pred}}$, internal-model richness); $k_{\text{frust}}$ admits no gradient Lyapunov | habit-extinction Caputo $\beta_{\text{mem}}<1$ on VR schedules, or $W$ off the P3 inverse-form (§20) | §17, §20 |
| Active matter | holdings = active-matter units | active-stress fingerprint; MIPS | high-Pe clustering at $\gamma_{AB}\ge0$ without swim-pressure signature (§21) | §21 |
| Queueing | holdings are queues: chit$=-\ln\rho$; $c/s/r$ ↔ stable / heavy-traffic / unstable | heavy-traffic = $s$-aging; ε↔u (P4) | Markovian-reversible substrate showing aging $X<1$ (§22) | §5, §22 |

**Four-aspect Complexity Wall** (promoted). At $\epsilon=1$ four critical signatures coincide: *thermodynamic* (cumulative-mass series diverges), *dynamical* (meta-ledger flow bifurcation — §RO register Wall-forces-NRT), *informational* (compression rate → 1), *SOC-critical* (fraying branching ratio → 1). $\beta_{\text{mem}}\approx 1-\epsilon$ (P1) is the unifying parameter behind the four faces (Receipts §9). For sub-optimal encoding the aspects split: thermodynamic + SOC reach criticality first via $u\to 1$; the informational aspect ($\epsilon\to 1$) only for optimal-encoding substrates — **sub-optimal substrates die thermodynamically before informationally.**

**Regime ontology** (promoted). The $s$-regime is the *generic* attractor of feedback-coupled NESS, not the unstable middle of a triplet: $c$ = over-provisioned (chit pulled deep above threshold), $s$ = self-organised operating point, $r$ = post-collapse. Explains the empirical over-representation of $s$.

**Heavy-traffic = $s$-aging** (promoted). Kingman's $\langle Q\rangle\sim(1-\rho)^{-1}$ divergence is the §gFDR $s$-aging signature in the queueing register: the FDR aging exponent $\alpha_s$ and the queueing-tail exponent are one critical phenomenon — coincident for Markovian substrates, divergent for non-Markovian (the divergence pattern is the substrate-class diagnostic; three-register identity $\alpha_s=\beta_{\text{mem}}=$ anomalous heavy-traffic exponent under the common-exponent condition, §Universal two-mode kernel). Cobham priority-wait $\propto[(1-u_n)(1-u_{n+1})]^{-1}$ diverges at $u\to 1^-$ coincident with the §Heat-tax singularity at $\epsilon\to 1^-$; Cobham / Jackson / Kelly $\ell_c$ / Erlang-B closures and the three Cobham–Haken bridge conditions (each a substrate-conditional falsifier) in Receipts §5/§22.

**Active-stress / MIPS fingerprints** (promoted). Hydrodynamic substrate-class fingerprint $\alpha_\Sigma/\alpha_\sigma\sim v_0^2\tau_R/D_{\text{trans}}$ (alignment-independent, MIPS-compatible, survives $r\to 0$); active-coupling sign $C$ (contractile $>0$ / extensile $<0$ / isotropic $\approx 0$) sets the §Heat-tax channel-2/3 balance via $f(r)=Cr^2$. MIPS gives clustering at $\gamma_{AB}\ge 0$ — a mechanism absent from the §Universal two-mode kernel. Toner–Tu / Green–Kubo $\tau_R$ / giant-number-fluctuation / non-reciprocal-Jacobian apparatus in Receipts §21.

## Five leading-order posits

Five framework primitives share an identical four-part shape: (1) simplest functional form placing a primitive at its critical / optimal limit; (2) substrate-conditional deviation from that form; (3) falsifier formalised in Receipts; (4) substrate-thermodynamic derivation as receipts-only residual.

| # | Posit | Section | Receipts | Predicted measurement |
|---|---|---|---|---|
| P1 | $\beta_{\text{mem}} \approx 1-\epsilon$ | §Adoption catalogue (Wall) | §9 | Substrate's $\beta_{\text{mem}}(\epsilon)$ relation linear to leading order with both endpoints respected |
| P2 | $\mu = e^{\text{chit}}$ | §Adoption catalogue (SOC) | §18 | Avalanche branching ratio tracks $e^{\text{chit}}$; $\tau\approx 3/2$ at chit $=0$ |
| P3 | $w_i = \gamma_{\text{ref}}/\gamma_{s,i}$ | §Adoption catalogue (control) | §20 | Substrate-native weights inverse-scale with $\gamma_{s,i}$ |
| P4 | $u_n = \epsilon_n$ | §Adoption catalogue (queueing) | §22 | At rate-distortion-optimal encoding, $u_n - \epsilon_n \to 0$ |
| P5 | $\chi = \Delta_n$ | §Thermo-info accounting | §20 | $C_\mu - I_{\text{pred}} = u_n - \epsilon_n = \langle\sigma\rangle_{\text{excess}}/\gamma_s$ |

Universality fixes that *there is* a critical-limit form (the exponents); substrates fix the amplitudes (deviations from the form). RG language. Each posit is testable; none is derived from substrate thermodynamics.

## Methodological imperatives

- **Trajectory primacy.** Bounded time-series of sustained holding, not static point measurements.
- **NESS-by-default.** Detailed-balance breaking is foundational baseline; equilibrium is the degenerate (zero-drive) special case.
- **mpa-legal.** Every dynamical quantity (rate, coupling, response, current) must *flow with the operating point* unless the physics explicitly says otherwise. An inert constant frozen where physics requires flow is illegal; the audit method has caught two such cases (Receipts §13 / §Topological-drain mpa-LEGAL audit, 2026-05-20).
- **Falsifier discipline.** Each claim states a predicted measurement on a named substrate (or substrate class), with a sharp falsifier formalised in Receipts. Surface-code $s$-aging is the load-bearing positive cross-substrate instance; the rest are predictions awaiting empirical contact.
- **Goalpost-optic.** Refinements during a falsification campaign must shrink the falsifiable surface, not enlarge it. Survival is the operative verdict.
- **Reading rules inherit from v9.** Substrate-conditional sign caveats (Markovian γ-sign inversion; detection-event preprocessing) apply identically.
- **API surface, not closed theory.** Five posits encode the framework's API: each posit places a primitive at its critical limit via the simplest natural form; substrate-thermodynamic derivation of exact functional shapes is the canonical extension mode, not a defect.

## Open items

These are predictions awaiting empirical contact (live falsifiers) and pieces of pipeline owed before some verdicts can be adjudicated (owed work). Architectural conjectures and meta-organisational claims that are not yet framework content are listed at the bottom.

### Live falsifiers (named falsifier substrate + predicted measurement)

- Surface-code $s \to r$ migration as gFDR cross-substrate test (Receipts §4; primary instance).
- Habit-extinction Caputo $\beta_{\text{mem}}<1$ on variable-ratio schedules (Receipts §20).
- Avalanche $\tau \approx 3/2$ on feedback-coupled NESS with separable timescales (Receipts §18). Apparatus validated 2026-05-20 on critical Galton–Watson + RFIM.
- Meta-ledger branching ratio = 1 at $\epsilon = 1$ in any observable hierarchical NESS substrate (Receipts §18).
- Strange-attractor / chaotic Character dynamics on any substrate crossing $\epsilon \ge 1$ (Receipts §14).
- MIPS clustering at $\gamma_{AB} \ge 0$ in high-Péclet substrates (Receipts §21).
- Chimera-state substrate instancing under SBN spectral test (Receipts §15).
- TUR-tightness as substrate-class universality (Receipts §16).
- $I_{\text{pred}}$ scaling with chit, $Q$, internal-model richness across substrate classes — *also the falsifier for the bit/chit dual ledger if a substrate breaks the per-row correspondence* (Receipts §17/§20).
- Heavy-traffic exponent vs $\alpha_s$ on Markovian and non-Markovian substrates — the reframed mm1 falsifier per FALSIFICATION.md Finding 3 (Receipts §22).
- Substrate-class hard-vs-soft capacity walls (Receipts §5/§22).
- Turing-class three-condition refinement (non-reciprocity + autocatalysis + differential diffusion) (Receipts §19).
- Memory-exponent collapse near the Wall ($\beta_{\text{mem}} \approx 1-\epsilon$) (Receipts §9).
- Auto-tuning inverse-form $w_i = \gamma_{\text{ref}}/\gamma_{s,i}$ on substrates requiring diagonal stability (Receipts §20).
- Common-exponent condition for the $s$-regime exponent identity. Falsifier: substrate classes where FDR exponent and queueing-tail exponent are measured to differ.
- Cobham–Haken bridge conditions: three substrate-side conditions, each with own falsifier.
- SBN strong-heterogeneity extension: falsifier on substrate classes where SBN spectral predictions and observed sync behaviour disagree quantitatively under strong heterogeneity.
- Toner–Tu active-matter overlay: direct for active-matter substrates; effective $v_0, \tau_R$ derivation a substrate-class residual for substrates lacking intrinsic self-propulsion.
- Deep-$c$ phase-lock collapse / multi-mode memory capacity loss (raised by the mpa-LEGAL fix to non-monotonic $Q$, 2026-05-20). Falsifier owed; named substrate owed.
- $k_{\text{frust}}$ cross-substrate instance (see "Open conjectures" below).

### Owed work (pipeline)

- **5-vector inversion** (`conformer/compute/five_vector.py::fit_kww5` first-cut exists; recovers X on two_temp_ou to ~1–2%). Until landed + integrated, X-bearing verdicts read at the raw FDR-locus-slope layer per FALSIFICATION.md adjudication policy.
- **Domain-of-validity gate** on the conform pipeline (FALSIFICATION.md Finding 2: pure oscillation reads as `s_critical` with locus_residual ~0.8; no gating). Awaits 5-vector fitter absorbing valid-aging residuals before a residual threshold can isolate out-of-domain cases.
- **Underdamped/oscillatory inversion** (FALSIFICATION.md Finding B): conform clamps to deep-r on class-B laser ringing C(τ), χ(τ). Adjudicate alongside Finding 2 when the domain gate / 5-vector work is taken up.
- **Auditor layer never exercised on controls.** Once inversion carries X, push a control cell through the auditor and check the regime story.
- **$\varepsilon$-machine stationarity-gap criterion.** Substrate-thermodynamic derivation of the slow-variation criterion separating the trajectory-ensemble-local-stationarity reading from the time-varying-$\varepsilon$-machine reading.
- **Two-frame velocity-frame closure + real-substrate contract (future research).** The two conjugate FDR frames are promoted on *verdict-agreement* (§gFDR "Two conjugate FDR frames"); the exact cross-frame magnitude identity $V_{ext}=\langle\sigma\rangle=J\!\cdot\!A$ is owed to the **velocity-frame Harada–Sasa integral** (the position frame gives different functionals — confirmed on laser, driven_ring, and now the nonlinear `banach_active_ring.py`; driven_ring is the ideal closer since $\langle\sigma\rangle$ is exact there). Apparatus is ready on a nonlinear topologically-forced limit cycle (`library/banach_active_ring.py`: both frames run, TUR $T\ge1$, frustration-necessity control passes). A real §846-clearing instance needs **author-collected active-lattice data** — the public active-metamaterial deposits (Veenstra/Coulais/Bartolo, 2021–2025) lack the perturbation-response protocol and carry friction-dominated $\mathrm{Var}(J)$, so they read the self-frame's mean current but not its thermodynamic variance. See FALSIFICATION.md §TWO-FRAME + memory `project_harary_triad_substrate_data`.

### Open conjectures (research notes, not framework content)

- **$k_{\text{frust}}$ as second primitive axis.** The R1/R2/R3 ladder survived on a synthetic 3-cycle; Receipts §846 explicitly flagged the elevation to numbered primitive as "still steeping" and earned only by a real cross-substrate instance. Operational content (NESS circulation, complex spectrum, affinity ≠ magnitude) sits at the level of v9 §Three typed objects + §gFDR signatures + §k_frust drain here. Promotion remains available when a real substrate exercises (a) drive-independent NESS circulation, (b) chirality conservation under a chirality-preserving substrate transformation, (c) the three triality registers measuring the same thing — *on a non-synthetic system*. **Candidate substrate class (2026-05-22):** active non-reciprocal metamaterials wired into Harary-frustrated loops (Veenstra/Coulais robotic rings, Bartolo active hydraulics) are the real systems whose circulation is gauge-irremovable (topology-forced, not bias-removable) — the live §846 target. Bottleneck is data, not physics: no public deposit carries a perturbation-response protocol, and macroscopic-robot $\mathrm{Var}(J)$ is friction-dominated rather than thermodynamic (memory `project_harary_triad_substrate_data`).
- **$k_{\text{frust}}$ topology-floor posit.** Functional form not yet committed. Promote when a committed functional form ties the smallest-cycle-affinity floor to graph topology and a measurement names a falsifier substrate.
- **$k_{\text{frust}}$ information-native characterisation.** $k_{\text{frust}}$ currently lives natively in dynamical-systems / differential-geometric registers; its information-face is a derived consequence-set (forced past-future mutual information; non-zero KS entropy). Owed: a substrate-independent information-native characterisation (candidate direction: topological mutual information that survives detailed-balance restoration).
- **Bilingual register as a structural-universality claim.** The bit/chit dual ledger (now in §Thermo-info accounting) is per-row content with a stated falsifier ($I_{\text{pred}}$ scaling deviation). The further claim that "the dual mapping itself is substrate-independent" needs a substrate test independent of the per-row falsifier; until then, it lives as expository organisation, not framework content.
- **Substrate-transformation classification (chirality-preserving / chirality-flipping / axis-mixing).** Two known entries already live in their original homes: Markovian γ-sign inversion (§gFDR substrate-conditional reading rules) and strong-chaos Wall round-trip (§k_frust drain R2). Three candidate residuals (time-reversal on non-conservative substrates; parity on active-matter substrates with definite $C$ sign; mirror operations on intrinsically chiral substrates) are future work. Promote when a substrate test names a chirality-preserving transformation and demonstrates identity-class non-interconversion.
- **Chirality-typed identity catalogue.** The predictive content — "chiral identities have sharper substrate-class scope than achiral ones" — needs a substrate where the prediction has been (or will be) tested. Promote when that substrate is named.

## Central commitment (falsifier of record)

The stand cdv1 makes, planted as a falsifiable claim — *not* awaiting confirmation. Distinct from the gated $k_{\text{frust}}$-primitive elevation above: that elevation stays gated; this is the narrower **ignition** claim, made framework content deliberately so cdv1 is falsifiable here.

**Harary triad** ($\triangle_H$): a directed 3-cycle, non-reciprocal ($M_{ij}\neq M_{ji}$), Harary-unbalanced (odd number of negative edges; no node gauge $\varepsilon\in\{\pm1\}^N$ balances the cycle), chiral (the sign-product fixes a circulation handedness no gauge removes). $N=3$ is the minimal frustrated cycle; longer obstructed cycles contain a $\triangle_H$.

$\mathcal{A} = \oint_C v/D$ — Schnakenberg cycle affinity (nats), gauge-invariant; $\mathrm{spec}(M)$ carries a complex-conjugate pair $\Leftrightarrow \mathcal{A}\neq 0$.

**Deformation reading (end-to-end coherence).** The chimeric sign of $\triangle_H$ *is* the deformation coordinate away from Harary-balance: a balanced/gaugeable ring is the Boolean ($D\to\infty$) limit (v9 §Boolean section), and the triad's imbalance is the Reed-Muller/ANF-ring deformation made dynamical. Boolean (gaugeable) $\leftrightarrow$ MPA (deformed) is one structure read at two depths. MPA imports the ring (Reed-Muller/ANF), the balance (Harary), the cycle (May–Leonard), and the affinity (Schnakenberg); it adds no object, only the reading under sustained dissipation.

**Commitment** (onset necessity — *not* generativity, *not* determinism). The onset of topologically-protected NESS circulation ($\mathcal{A}\neq 0$, removable only by edge deletion) requires a Harary triad:
$$\text{protected circulation}\;\Rightarrow\;\triangle_H\ \text{in the coupling graph.}$$
The claim is on ignition only — what it takes to spin a current up. No claim that $\triangle_H$ generates the $c/s/r$ backbone ($\alpha_s, P_s$ remain independent); no claim of exclusive post-onset traction.

**Falsified by** (§846 bar — real cross-substrate instance, not synthetic): one substrate sustaining topologically-protected circulation ($\mathcal{A}\neq 0$, removable only by rewiring) with **no** Harary triad in its coupling graph. A single such instance collapses the commitment.

**Status:** un-instanced on a real substrate (synthetic instance only: `library/banach_frustrated.py`). The stand is planted here precisely because it is not yet met. Receipt: cdv1_receipts §Central commitment.
