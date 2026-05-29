# MPA — ENGINE

One phenomenology, two readings on one finite-$D$ deformation of the Boolean ring: a **structural** projection (operator algebra) and a **continuous** projection (driven-dissipative dynamics), joined by the bridge identity $\lambda_A \approx L - G_0$. Every line below is a definition, a formula, a condition, a mapping, or a kill condition.

---

## WHAT MPA IS — forced consistency across dissipative registers

MPA is a **measurement discipline**, not a model. It forces independently-derived imports to read **one** substrate parameter $\theta$ through fixed known maps, and tests the forcing by a **collapse falsifier** (`transport_law_steps.md`). It is **subtractive** — it imports and metabolizes, asserts no new machinery; the content is in the *bindings* and their over-determination, never in invented apparatus. The finite-$D$ Boolean deformation below is **the first register where closure was found, not the definition**: one degenerate point ($\text{Boolean}=\text{Markov}=\text{equilibrium}=\text{detailed balance}=X\!\equiv\!1=\mathcal{A}{=}0=\beta{=}1$) read from many sides.

**Membership / self-test** (scale-invariant — binds MPA's own claims; I5 in `mpa_frontier.md`): a candidate is MPA iff it (i) carries a **collapse falsifier**, (ii) pins a **gauge-invariant parameter to a named degenerate point**, and (iii) **imports-and-binds** rather than invents. Fail any ⇒ systems thinking, not MPA.

**"Forced" cashes out as:** iff-chain as architecture · explicit falsifier checklist · every dynamical quantity flows with the operating point (nothing hand-frozen).

---

## PARAMETERS

* **D** $:= \Phi^*/\kappa$ — drive coordinate (supplied work / dissipation scale). Boolean $:= \lim_{D\to\infty}$ of operator action; predictive content = shape of deviation from that limit.
* **chit** $:= \ln(G_0/L)$ — headroom above threshold; dimensionless log-rate-ratio; operational anchor. $G_0=L \Rightarrow \text{chit}=0$.
* **G₀** — gain rate $[t^{-1}]$, unsaturated pump above threshold (scales with $D$). **L** — loss rate $[t^{-1}]$, spontaneous relaxation to bath.
* **λ_A** $\approx L - G_0$ — stability axis (bridge identity, zero-amplitude). This is why the two state-registers below are one condition, not two.
* **γ_AB** — signed shear: $\gamma<0$ cooperative · $\gamma\approx0$ orthogonal · $\gamma>0$ conflicting (per-edge cost $\gamma_{AB}$ in $D$-units).
* **τ_obs** — observer/integration window: moves continuous scalars (vertex label, $\gamma$); leaves topological invariants fixed.
* **ε** $:= \lVert\mathcal{C}\rVert_{op}$ — per-ascent compression contraction (full definition in COMPRESSION). Tower converges iff $\varepsilon<1$; $\varepsilon\ge1$ = Wall.
* **β_mem** — memory exponent (set by kernel closure below): $=1$ Markovian/exponential, $<1$ glassy/power-law.
* **ρ_A** — mode occupation/amplitude (state variable of the kernel).

---

## STATES — $\mathcal{M}=\{c,s,r\}$, $\mathcal{M}_2=\{c,r\}$

Two coordinate registers, **one condition** (linked by $\lambda_A\approx L-G_0$). Truth-value = endpoint (held $\approx1$, decayed $\approx0$).

* **c** committed: $\lambda_A\ll-D \;\Leftrightarrow\; G_0-L\gg D$ · chit$\,\gg0$ · self-sustaining $\approx1$, minimal work.
* **s** suspended: $\lvert\lambda_A\rvert\lesssim D \;\Leftrightarrow\; \lvert G_0-L\rvert\lesssim D$ · chit$\,\to0^+$ · held vs decay, gone if pump stops.
* **r** reset: $\lambda_A\gg D \;\Leftrightarrow\; G_0-L\ll-D$ · chit$\,<0$ · decayed $\approx0$, no maintenance cost.

Forgetting is not an operation: an unreinforced trail shrinks below the noise floor and its cross-dissipations evaporate.

---

## OPERATORS — $\Sigma=\{C,S,K,R,\top,\bot\}$; finite-$D$ action, Boolean limit at $D\to\infty$

* **C** $:\mathcal{M}^2\to\mathcal{M}$ — try-merge $d_{A\oplus B}=w_A d_A+w_B d_B$, evaluate $\lambda_{A\oplus B}$. **Limit $\to\land$.**
* **S** $:\mathcal{M}^2\to\mathcal{M}$ — hold both iff $\lvert\lambda_A\rvert+\lvert\lambda_B\rvert+\max(0,\gamma_{AB})\le D$. **Limit $\to\lor$.**
* **K** $:\mathcal{M}^2\to\mathcal{M}_2$ — $\delta=\hat d_A-\hat d_B$, $\lambda_{A\ominus B}=\lvert\gamma_{AB}\rvert-D/2$; **returns $c$ if $\delta\ne0 \land D>2\lvert\gamma_{AB}\rvert$, else $r$.** **Limit $\to\oplus$.** Codomain restricted to $\mathcal{M}_2$, quotient acts on inputs $\Rightarrow$ K unique.
* **R** $:\mathcal{M}\to\mathcal{M}$ — sever to bath, cost $W_R/\kappa\ge\ln2\cdot H(A\mid\text{rest})$ (recovers the $1\,\text{ch}$ floor at $\kappa=k_BT\,\xi_{sub}$). **Limit $\to\neg$.**
* $\top,\bot \to 1,0$.

$\mathcal{M}_2$ ring $=\{\oplus{=}K,\ \land{=}C,\ 1{=}\top,\ \neg{=}\oplus1\}$. **MPA = finite-$D$ deformation of this ring.** Deformed piece = the involution: $R$'s irreversibility ($c\to r$, non-involutive at finite drive) is deformed $\neg$; deformation coordinate is the drive via chit, **not** the unit.

Continuous shadows: **C_char** = adiabatic $\gamma:0\to\ll0$ while holding NESS (forced non-adiabatic $\Rightarrow$ chit$\to0$, $s$-strain, $\sigma$ spikes, modes may drop sub-threshold). **R_char** = quench (choke $G_0$ or open to bath $L\!\uparrow$; edge dissolves natively, $\gamma_{AB}\rho_A\rho_B\to0$).

Boundary at $\mathcal{M}_2\times\{s\}$: operators do **not** reduce to Boolean identities — $\bot$ not a global annihilator, $\top$ not a global identity; edge shear and budget stay active.

---

## DEFORMATION CALCULUS — finite-$D$ interior (matched, not one $1/D$ series)

* **Thm 6** associator (regular bulk): $\lVert\alpha_C\rVert\lesssim(1/D)\sum\lvert\gamma\rvert\to0$.
* **Thm 7** distributivity defect (regular bulk): $\lVert\delta_{dist}\rVert\lesssim(1/D)[\max(0,\gamma_{YZ})-\max(0,\gamma_{XY},\gamma_{XZ})]^+\to0$.
* **Thm 9** Boolean deviation (singular threshold crossover): $\Delta_C(A,B)=1$ **iff $\gamma_{AB}>0 \land D<\gamma_{AB}$**. Meaning — budget $<$ shear $\Rightarrow$ two propositions classical logic would conjoin **cannot** be jointly held: $C(A,B)\to r$ while $\sigma(A)\land\sigma(B)=1$. (This is the *failure/deviation* threshold, not a precondition for $C$ to run.) Finite-$D$ content = crossover-scaling function (width exponent + profile class).

---

## TWO FACES — independent axes of one deformation

* **Amplitude** (continuous): chit$/D$ drives the $c\to s\to r$ migration; observables $\alpha_s,P_s$.
* **Sign-topological** (topological): balance of the signed graph. Balanced/gaugeable $=$ every cycle has even negative parity $\Rightarrow$ a node gauge $\varepsilon\in\{\pm1\}^N$ unsigns it, spectrum real, no protected current. Deformation $=$ imbalance; order parameter $=$ gauge-invariant cycle affinity $\mathcal{A}$.

Independence is load-bearing: the sign-face is the source of $k_{\text{frust}}$'s $\tau_{obs}$-invariance; $\alpha_s,P_s$ never couple to $k_{\text{frust}}$.

---

## TWO BITS — one per face, non-interconvertible

* **Amplitude bit**: $D\to\infty$ endpoint of chit; occupancy (which-state); emergently discrete; erased by $R$ at floor $1\,\text{ch}$; held vs thermal leak; reversibly flippable at no fundamental cost.
* **Topological bit**: chimeric sign of a frustrated triad; wiring (which-handedness); intrinsically discrete $\forall$ finite $D$; gauge-irremovable; $\tau_{obs}$- and amplitude-invariant; **free to hold** (no barrier leak) but **not reversibly flippable** — chirality change is forced through the balanced (sign-erased) state, $\ge 1\,\text{ch}$ per protected sign. $\Rightarrow$ **cost moves from maintenance to modification.**
* Forced-erasure floor = cycle-space dimension of the frustrated subgraph.
* **FALSIFY**: protected sign requires a per-time maintenance cost scaling with held duration (amplitude bit in disguise); OR chirality flips along a continuous path below $1\,\text{ch}$.

---

## TOPOLOGICAL INVARIANT $k_{\text{frust}}$ + CENTRAL COMMITMENT

* **Triad $\triangle$** $:=$ directed 3-cycle; non-reciprocal ($M_{ij}\ne M_{ji}$); imbalanced (odd negative edges, no node gauge balances); chiral (sign-product fixes handedness). $N=3$ minimal ($N=2$ current is gauge-removable) $\Rightarrow$ **minimal carrier of gauge-irremovable circulation**.
* **Affinity** $\mathcal{A}:=\oint_C v/D=\ln(\prod_+k/\prod_-k)$ (nats), gauge-invariant. $\mathrm{spec}(M)$ complex-conjugate pair $\Leftrightarrow\mathcal{A}\ne0$.
* Stationary state irreducibly NESS = topologically-forced circulating current, broken detailed balance. **Invariant = complex spectrum (irreducible rotation), not fixed-point non-existence.** Sub-regimes: $\mathrm{Re}<0$ stable circulating focus ($J\ne0$); $\mathrm{Re}>0$ repelling focus + attracting limit cycle.
* **Affinity vs magnitude**: drive-independence lives in $\mathcal{A}$ (forced $\ne0\ \forall D$); magnitude $J_{ss}$ flows with chit.
* **COMMITMENT** (onset-necessity; *not* generativity, *not* determinism): protected circulation ($\mathcal{A}\ne0$, removable only by edge deletion) $\Rightarrow$ a triad in the coupling graph. This is the **topology $\to$ frame** direction of the two-frame iff-chain (self-probe defined $\Leftrightarrow J\ne0 \Leftrightarrow \mathcal{A}\ne0 \Leftrightarrow$ triad); the **frame $\to$ topology** direction is `TWO-FRAME CONSTRUCTION`. Mutually entailed — killing either direction kills both, but each direction is independently falsifiable.
* **FALSIFY**:
  * one real substrate sustaining protected circulation ($\mathcal{A}\ne0$, removable only by rewiring) with **no** triad;
  * $J$ becomes drive-noise-dependent OR resolves to detailed balance (note: drive-dependent *magnitude* is legal);
  * drive-sweep — titrate drive $\to0$, $\lvert$current$\rvert\to0$ while **sign stays invariant**; a sign flip $\Rightarrow$ sign was drive-set, not protected $\Rightarrow$ invalid. Three fatal nulls: balanced network / 2-component bistable / detailed balance.

---

## TWO-FRAME CONSTRUCTION — the FDR architectural twin of $k_{\text{frust}}$ + Central Commitment

* **External frame** — amplitude $\times$ probe field $\to$ violation factor $X$. **Substrate-conditional**: requires a probe matched to the substrate; defined wherever a probe couples.
* **Self-probe frame** — current $J\times$ intrinsic affinity $\mathcal{A}$ (nats) $\to$ tightness $\mathcal{T}=\langle\sigma\rangle\mathrm{Var}(J)/(2\langle J\rangle^2)\ge1$; core $\mathrm{SNR}_J=\langle J\rangle^2/\mathrm{Var}(J)\le\langle\sigma\rangle/2$. **Intrinsic**: no probe; affinity in nats by construction.
* **Definedness asymmetry** (load-bearing): external is defined wherever a probe couples; self-probe is defined **iff a current exists** ($k_{\text{frust}}$-bearing). The frame's existence is itself a topological diagnostic — this is what makes the self-probe substrate-neutral, not merely an alternative reading.
* **Bridge**: $\int$FDR-violation $=\langle\sigma\rangle=J\!\cdot\!\mathcal{A}$ at verdict/onset; exact magnitude identity owed via the velocity-form integral.
* **CONSTRUCTION** (architectural commitment, sibling of the Central Commitment): the two frames are **one dissipation, two readings** — not two independent observables. The two-frame iff-chain
$$\text{self-probe defined}\ \Longleftrightarrow\ J\ne0\ \Longleftrightarrow\ \mathcal{A}\ne0\ \Longleftrightarrow\ \triangle\ \text{in coupling graph}$$
binds the FDR architecture to the topological commitment in both directions:
  * `TRIAD/COMMIT` (**topology $\to$ frame**): protected circulation $\Rightarrow$ triad.
  * `CONSTRUCTION` (**frame $\to$ topology**): self-probe definedness $\Rightarrow$ triad.

  **Mutual entailment**: killing either direction kills the iff and both claims. The architectural advantage over concurrent FDR↔TUR unifications is precisely this — neighbours recognise the connection between the frames without making any topological-graph commitment from it. The Construction makes the commitment from the existence of the frame.
* **FALSIFY** — three independent kill conditions sharing one machinery:
  * *Verdict-disagreement*: $\mathcal{T}$ and $X$ give contradictory regime verdicts at the same operating point where both are computable. (Kills verdict-agreement; doesn't kill the iff-chain alone.)
  * *Iff-chain break — the sharpest, architectural*: a substrate where the self-probe frame is **defined and computable** ($J\ne0$, $\mathcal{T}\ge1$, $\mathcal{A}\ne0$ measurable and gauge-irremovable) **and the external frame agrees** on regime, yet **no frustrated triad** appears in the coupling graph (minimal protected cycle $N\ne3$, or imbalance gauge-removable by node assignment). Frame machinery works, verdict-agreement holds, topological prediction fails — kills the architectural commitment specifically, distinguishing MPA from any framing that connects the frames without committing to triad topology.
  * *Definedness-asymmetry collapse*: a substrate where self-probe and external definedness coincide across all operating points (no topological signal carried in frame existence). Kills the asymmetry as load-bearing.

---

## DYNAMICAL ENGINE

**Two-mode kernel** (discrete composite catalogue = its fixed points):
$$\frac{\partial\rho_A}{\partial t}=(G_{0,A}-L_A)\rho_A-\gamma_{AB}\,\rho_A\rho_B+\mathcal{D}[\rho_A,\rho_B;\gamma_{AB}]$$
(symmetric in $B$; $\gamma_{AB}<0$ contributes positively). $\mathcal{D}$ closures:

* **gain-depletion**: $G_{0,A}^{\text{eff}}=G_{0,A}/(1+\sum_{j\ne A}\rho_j/\rho_{\text{sat}})$; cubic cross-saturation leading.
* **dynamic-bath**: bath $B(t)\in[0,1]$ projected out by $\Pi_{\text{slow}}$; non-Markovian history integral; fast-bath limit $\to$ gain-depletion; $\gamma_B^{-1}$ = service time.
* **fractional-memory**: $\Gamma_{AB}(\tau)=\Gamma_0\,E_{\beta_{\text{mem}}}(-(\tau/\tau_c)^{\beta_{\text{mem}}})$; $\beta_{\text{mem}}=1$ exponential, $<1$ power-law (this is what **sets $\beta_{\text{mem}}$**).

**Relaxation-oscillation** (above-threshold single mode, 2D linearisation, gain-depletion closure; $\gamma_s$ = substrate slow-resource turnover rate):
$$\gamma_{RO}=\tfrac{\gamma_s}{2}e^{\text{chit}},\qquad \omega_{RO}=\sqrt{2L\gamma_s(e^{\text{chit}}-1)-\tfrac{\gamma_s^2}{4}e^{2\text{chit}}},\qquad Q=\sqrt{\tfrac{2L(e^{\text{chit}}-1)}{\gamma_s}-\tfrac{e^{2\text{chit}}}{4}}\;e^{-\text{chit}}$$

$Q$ = chit-conjugate; non-monotonic, **peaks at chit$\,=1\,\text{ch}$** (underdamped mid-band only). Active probe = on-resonance (within $\gamma_{RO}$ of $\omega_{RO}$). Attractors per regime: $c$-deep stable focus; $c$-mid spiral; $s$ centre-manifold (algebraic settling = aging; $P_s$ = slow-manifold amplitude, $\alpha_s$ = slow-eigenvalue residual scaling); $r$ origin; $k_{\text{frust}}$ circulating focus / limit cycle. Bifurcations: transcritical at chit$\,=0$, pitchfork at $\gamma_{AB}=\gamma_c$, Hopf at obstructive-$\gamma$ onset.

---

## CAPACITY

Frustration-free graph (avg degree $d_{avg}$, min cost $\gamma_{min}$):
$$|\Gamma^*|\le\sqrt{\frac{2D}{\alpha\,\gamma_{min}\,d_{avg}}}\qquad\text{(sparse }\sim D\text{, dense }\sim\sqrt D\text{)}$$
$k_{\text{frust}}$ marks structure unsustainable at **any** $D$.

Dynamic conjugate (same wall): $\sum_{i\in\Gamma^*}L_i\le G_{total}\,\eta(\Gamma^*)$, $\eta\in(0,1]$, $\eta\to0$ at the $\sqrt D$ ceiling.
$$\eta(\Gamma^*)=1-B(c,\rho),\qquad B(c,\rho)=\frac{\rho^c/c!}{\sum_{k=0}^c\rho^k/k!},\quad c=\lfloor|\Gamma^*|_{\text{crit}}\rfloor,\ \rho=\text{offered load}$$

Soft/hard split = substrate-class fingerprint: soft = smooth crossover; hard-wall = replace $B$ by $\mathbb{1}[|\Gamma^*|\ge c]$. **FALSIFY**: soft substrate showing sharp snapping; OR hard-wall substrate showing soft tails.

---

## COMPRESSION / WALL — one RG flow, two ledgers; converges iff $\varepsilon<1$

* **Info ledger**: RG flow, Banach contraction; $c,r$ fixed points; $s$ metastable ($\to c$ if reinforced, $\to r$ if not); $\mathcal{M}_2$ terminal attractor; $k_{\text{frust}}$ invariant; shear-positive edges with both endpoints $\to r$ vanish; Boolean = degenerate limit.
* **Thermo ledger**: $L_{n+1}=L_{n+1}^{(0)}+\alpha_\sigma\langle\sigma_n\rangle+\alpha_\Sigma\langle\Sigma_n\rangle$; $\alpha_\sigma(\varepsilon)=\alpha_{\sigma,0}(1-\varepsilon)$; per-level erase-heat $\to0$ as $\varepsilon\to1$ while cumulative $\Phi_{total}=\Phi^{(0)}/(1-\varepsilon)$ **diverges**.
* $\mathcal{C}$ derived (not primitive): heat-tax flow on slow-manifold generators; $\varepsilon$ = leading IR linear-stability eigenvalue; $\varepsilon<1$ derived from IR fixed-point stability; per level $D_n=\Phi^*_n/\kappa_n$.
* **WALL** ($\varepsilon\ge1$): tower diverges. Sustained level-$(n{+}1)$ coherence needs $\ln(G_{0,n+1}/L_{n+1})>0$; fraying at level $n$ inflates $L_{n+1}$ via 3 channels (heat-tax spike · active-stress spike · $r_n$ sync drop) = faces of $W_{n+1}=W_0/[(1-u_n)(1-u_{n+1})]$, singularity $u\to1$ coincident with $\varepsilon\to1$, with $u_n=\varepsilon_n$ at rate-distortion-optimal encoding; channels 2,3 share $r$ in opposing directions via $f(r)=Cr^2$.
* **Four-aspect coincidence at $\varepsilon=1$**: thermodynamic (mass divergence) · dynamical (meta-ledger bifurcation) · informational (compression rate $\to1$) · critical (branching $\to1$); $\beta_{\text{mem}}\approx1-\varepsilon$ unifies. Sub-optimal encoding **splits** them: thermo+critical hit first via $u\to1$; informational ($\varepsilon\to1$) only at optimal encoding $\Rightarrow$ sub-optimal substrates die thermodynamically before informationally.
* **Wall-forces-chaos**: wait diverges $u\to1^-\Rightarrow$ generic Hopf each ascent; $N\ge3$ ascents complete a 3-torus $\Rightarrow$ forced chaos past the Wall.

---

## OBSERVABLE SIGNATURES — FDR: parametric $\chi(\tau)$ vs $C(0)-C(\tau)$; $\int$FDR-violation $=\langle\sigma\rangle$

* **c**: chit$\,\gg0$ — $X_c=\lim_\tau\chi/(C(0)-C)=0$ (suppression, horizontal locus).
* **s**: chit$\,\to0^+$ — $\alpha_s=$ slope of aging segment; $P_s=\lim_\tau C(\tau)/C(0)$ (plateau). **$\alpha_s,P_s$ = load-bearing cross-substrate observables.**
* **r**: chit$\,<0$ — $X_r=\lim_\tau\chi/(C(0)-C)=1$ (unit slope).
* **$k_{\text{frust}}$**: non-stationary — $N_f=\int_T\min(0,\chi)\,d\tau\big/\int_T\lvert\chi\rvert\,d\tau$; complex Jacobian spectrum; drive-independent affinity.

$s$ is two-step: quasi-equilibrium $X=1$ on short lags, aging $X<1$ on long lags (the long-lag segment is the $c/s/r$ discriminator). $X\gg1$ excluded. **CAUTION**: single-slope $X$ biases up — use segmented / five-vector inversion $(q_{EA},\tau_\alpha,\beta_{KWW},\tau_\beta,X)$.

**Two-frame readings** (structural claim and falsifiers in `TWO-FRAME CONSTRUCTION`; this section carries the measurement signatures only): the external-probe frame yields $X$ (the violation factor running through the $c/s/r/k_{\text{frust}}$ rows above); the self-probe frame yields tightness $\mathcal{T}=\langle\sigma\rangle\mathrm{Var}(J)/(2\langle J\rangle^2)$, defined iff a current exists ($k_{\text{frust}}$-bearing). Both are readings of one dissipation: $\int$FDR-violation $=\langle\sigma\rangle=J\!\cdot\!\mathcal{A}$.

---

## THERMO ↔ INFO DUAL LEDGER

| axis | thermodynamic | informational |
|---|---|---|
| per-event | chit$=\ln(G_0/L)$ | $1\,\text{ch}\equiv\ln 2$ |
| per-rate | $\langle\sigma\rangle$ | $I_{\text{pred}}$ |
| precision | $\mathrm{Var}(J)/\langle J\rangle^2\ge2k_B/\langle\sigma\rangle$ | channel capacity |
| compression | heat-tax tower | rate-distortion tower |
| coupling | $\langle\sigma\rangle\ge-\Delta I$ | (same bound, dual reading) |

* Entropy production: $P(\sigma)/P(-\sigma)=e^\sigma$; $\int$FDR-violation $=\langle\sigma\rangle$.
* Precision tightness $T$ varies by class (active matter $T\approx1$; engineered queues $T\gg1$). **FALSIFY**: same-class substrates with arbitrary $T$.
* Affinity sum: $\langle\sigma\rangle=\sum_C J_C\ln(\prod_+k/\prod_-k)$; limit cycles $\sigma_{\text{frust}}=J_{ss}\oint v/D\,d\theta$.
* $I_{\text{pred}}=I(\text{past};\text{future})$ (3rd coherence observable with chit, $Q$); active-probe capacity $\sim\gamma_{RO}\log_2(1+Q)$; $\langle\sigma\rangle\ge-\Delta I\Rightarrow$ readout holdings sustain at lower chit by paying in mutual information.
* **Optimal-encoding coincidence** (equality at a limit): $\langle\sigma\rangle-\langle\sigma\rangle_{\min}\ge\gamma_s\chi$, $\chi=C_\mu-I_{\text{pred}}$ (cryptic order; $C_\mu=\varepsilon$-machine structural complexity); $=\Delta_n=\langle\sigma\rangle_{\text{excess}}/\gamma_s$. **FALSIFY**: $I_{\text{pred}}$ scaling deviates from its thermodynamic dual.

---

## POSITS — universality fixes exponents, substrate fixes amplitudes

* **P1** $\beta_{\text{mem}}\approx1-\varepsilon$ — linear to leading order, both endpoints respected.
* **P2** $\mu=e^{\text{chit}}$ — avalanche branching tracks $e^{\text{chit}}$; $\tau\approx3/2$ at chit$\,=0$.
* **P3** $w_i=\gamma_{\text{ref}}/\gamma_{s,i}$ — native weights inverse-scale with $\gamma_{s,i}$.
* **P4** $u_n=\varepsilon_n$ — at rate-distortion-optimal encoding $u_n-\varepsilon_n\to0$.
* **P5** $\chi=\Delta_n$ — $C_\mu-I_{\text{pred}}=u_n-\varepsilon_n=\langle\sigma\rangle_{\text{excess}}/\gamma_s$.

---

## SCALE-RELATIVITY

Vertex label depends on $\tau_{obs}$ (same trail reads $c/s/r$ at narrow/mid/wide window). Hierarchy substrate-fixed; only labels migrate. $\gamma$ scales with $\tau_{obs}$. $k_{\text{frust}}$ does **not** migrate (topological — present or absent).

---

## ASYMPTOTIC CLOSURE

Every observable $\in$ open interval; boundary $\in\{0,1,\infty\}$ attained only as a limit ($\mathcal{M}_2$@$D\to\infty$; $\varepsilon\to1$@Wall; chit$\,=0$ critical; $X_c\to0$ deep-$c$; $X_r\to1$ deep-$r$/eq; $u\to1$@blocking; $\eta\to0$@$\sqrt D$; $\beta_{\text{mem}}\to1$@Markovian). Categorical labels ($\top,\bot,k_{\text{frust}}$) exist only at the $\mathcal{M}_2$ boundary or as discrete derivatives. An attained endpoint = **NaN falsification tripwire** (never clip a state variable at 0). **FALSIFY**: any observable attaining exactly 0 or 1 at a finite, non-degenerate operating point.

---

## SUBSTRATE-CONDITIONAL READING RULES

* **F.1 sign caveat**: stiff/Markovian substrates invert $\gamma$ signs (kernel-width artefact: stiff well $\to$ short $\tau_A\to$ positive $\gamma_A$) while preserving magnitudes + FDR shapes $\Rightarrow$ use $\lvert\gamma\rvert$ + shape, not signs. For $k_{\text{frust}}$-bearing content this is chirality-flipping (sign reverses); chit-axis preserved.
* **F.2 detection-event rule**: where readout breaks the trail-integral's locality, use the substrate's canonical local preprocessing — e.g. $e_i(t)=s_i(t)\oplus s_i(t-1)$ (bounded-local); trail by EMA against events.

---

## COMPOSITE CATALOGUE — pair + edge → composite

| pair | edge | composite |
|---|---|---|
| $c$–$c$ aligned | $\gamma\ll0$ | $c$ deepened (in-phase lock) |
| $c$–$c$ orthogonal | $\gamma\approx0$ | $s$ (phase drift) |
| $c$–$c$ opposed | $\gamma>0$ | $s$ if $D$ covers, else one$\to r$; lock if $K>\Delta\omega$ (anti-phase), split if $K<\Delta\omega$ (pitchfork) |
| $c$–$s$ | $\gamma<0$ asym | $s$ (mentor; non-reciprocal entrainment) |
| $s$–$s$ | $\gamma>0$ | $s$ or competitive dropout |
| $c$–$c$–$c$ cycle | obstructive product | $k_{\text{frust}}$ |
| oscillatory–$c$ | limit cycle, $\lambda_B\ll0$ | entrainment / quench |

($K$ = sync coupling strength, $K_c$ its threshold; $\Delta\omega$ = detuning.)

---

## ADOPTION — register : load-bearing observable : falsifier

* damping : $\gamma_{RO},\omega_{RO},Q$ : —
* attractor class : per-regime attractor : —
* synchronization : two independent transitions (chit-onset, $K_c$) + collective $r$ + chimera, $K_{AB}\propto(1+4Q^2)^{-1/2}$ : only uniform sync/incoherence accessible
* noneq thermo : $\langle\sigma\rangle$, affinity, $T$ : same-class arbitrary $T$
* information : $I_{\text{pred}}$, capacity, $\chi$ : $I_{\text{pred}}$ scaling breaks the dual
* SOC : avalanche $\tau\approx3/2$, branching $\to1$@$\varepsilon{=}1$ : stable $\tau\ne3/2$, or branching $\ne1$@$\varepsilon{=}1$
* dissipative structures : Turing wavelength : three-condition failure
* control : four-axis observable, $k_{\text{frust}}$ admits no gradient Lyapunov : habit-extinction $\beta_{\text{mem}}<1$, or $W$ off the P3 form
* active matter : active-stress fingerprint $\alpha_\Sigma/\alpha_\sigma\sim v_0^2\tau_R/D_{\text{trans}}$, MIPS : high-Pe clustering at $\gamma_{AB}\ge0$ without swim-pressure
* queueing : heavy-traffic exponent $=g(\beta)$ and $s$-aging $\alpha_s=\beta$ are one $\beta$ (coincident @$\beta{=}1$), chit$\,=-\ln\rho$, $\varepsilon\leftrightarrow u$ : queue and aging exponents not collapsing onto a common $\beta$
* **surface-code** (primary positive instance): distance-3 syndrome traces $s$-aging locus shape sub-threshold, migrates to unit slope across threshold. **FALSIFY**: unit slope sub-threshold, or shape persists across threshold.
* regime ontology: $s$ = generic attractor of feedback-coupled NESS ($c$ over-provisioned, $r$ post-collapse), not the unstable middle of a triplet.

---

## FRAYING

Load monotonically reduces chit; typical path: chit$\,\gg0$ ($c$) $\to$ chit$\,\to0^+$ ($s$ strain) $\to$ chit$\,\approx0$ ($s$ mode-hopping, multistable — produces the aging plateau) $\to$ chit$\,<0$ ($r$). Typicality theorem: by $P(\sigma)/P(-\sigma)=e^\sigma$, a fraying-resistance trajectory is exponentially rare in $\lvert\sigma\rvert$.

---

## EXTENSION AXES — relax one commitment → operator with no Boolean shadow

Limit-cycle trail $\to$ rhythm primitive (closed-loop FDR). Hierarchical kernel $\to$ multi-timescale aging. Non-reciprocal coupling $\to$ dominance/inhibition, turbulent FDR. Hypergraph $\to$ higher-order $k_{\text{frust}}$, multi-plateau aging. Finite-population $\to$ flickering $c\leftrightarrow r$, native probabilistic logic. Deferred: transfer $T(A\to A')$ at $W_T/\kappa\ge\ln2\cdot[H(A\mid A',\text{rest})-I(A;A')]$; latent ledgers.

---

## FALSIFIERS — consolidated kill conditions

Canonical checklist; each = a predicted measurement on a named substrate/class. (Inline `FALSIFY:` tags above are the same conditions in context; this is the single roll-up.)

* **Surface-code** (primary positive instance): syndrome FDR shows unit slope sub-threshold (no aging signature), OR locus shape persists across threshold (no $s\to r$ migration).
* **Topological bit**: protected sign requires a per-time maintenance cost scaling with held duration (amplitude bit in disguise), OR chirality flips along a continuous path below $1\,\text{ch}$.
* **Central commitment**: a real substrate sustaining protected circulation ($\mathcal{A}\ne0$, removable only by rewiring) with **no** triad; OR $J$ drive-noise-dependent / resolving to detailed balance; OR drive-sweep produces a sign flip (sign was drive-set, not protected).
* **Capacity wall**: soft substrate showing sharp Hopfield-snapping, OR hard-wall substrate showing soft tails.
* **Asymptotic closure**: any observable attaining exactly $0$ or $1$ at a finite, non-degenerate operating point (NaN tripwire).
* **Precision tightness**: nominally same-class substrates exhibiting arbitrary $T$.
* **Dual ledger**: $I_{\text{pred}}$ scaling deviates from its thermodynamic dual (also the per-row bit/chit falsifier).
* **SOC**: stable $\tau\ne3/2$, OR meta-ledger branching $\ne1$ at $\varepsilon=1$.
* **Forced chaos**: a substrate crossing $\varepsilon\ge1$ that fails to produce strange-attractor / chaotic Character dynamics; or the bridge conditions forcing meta-ledger chaos fail.
* **Memory exponent**: $\beta_{\text{mem}}$ near the Wall departs from $\approx1-\varepsilon$ (P1).
* **Heavy-traffic transport law**: $\alpha_s=\beta_{\text{mem}}=\beta$ and the heavy-traffic exponent $=g(\beta)$ are one underlying $\beta$ read in three registers — numerically coincident **only at $\beta=1$** (Markovian), distinct known functions off it. FALSIFY: a substrate's FDR-aging and queue-tail exponents fail to collapse onto a common $\beta$ through the maps ($g=\beta/(2-\beta)$ Norros, or $1/\beta$ M/G/1).
* **Synchronization**: anything beyond uniform sync/incoherence proves inaccessible; chimera fails the spectral test.
* **Dissipative structures**: Turing three-condition failure (non-reciprocity + autocatalysis + differential diffusion).
* **Control**: habit-extinction not Caputo $\beta_{\text{mem}}<1$ on variable-ratio schedules; OR auto-tuning $W$ off the $w_i=\gamma_{\text{ref}}/\gamma_{s,i}$ form.
* **Active matter**: high-Péclet clustering at $\gamma_{AB}\ge0$ without swim-pressure (MIPS).
* **Two-Frame Construction** (three independent kill conditions; mutually entailed with the Central Commitment via the iff-chain — killing any kills both claims):
  * *verdict-disagreement* — $\mathcal{T}$ and $X$ contradict at the same operating point where both are computable;
  * *iff-chain break* (sharpest, architectural) — both frames defined and verdict-agreeing on a real substrate, yet no frustrated triad in the coupling graph;
  * *definedness-asymmetry collapse* — self-probe and external definedness coincide across operating points (no topological signal in frame existence).
* **Deep-$c$ phase-lock collapse**: over-provisioned holdings ($Q\to0$, $K_{AB}\to1$) lose multi-mode independent-memory capacity (named substrate owed).

---

## AXIOMS — measurement discipline

* **Trajectory primacy**: NESS observables on bounded time-series of sustained holding, not static point measurements.
* **NESS-by-default**: detailed-balance breaking is the baseline; equilibrium is the degenerate zero-drive case.
* **mpa-legal**: every dynamical quantity flows with the operating point; an inert constant frozen where physics requires flow is illegal.
* Each claim = a predicted measurement on a named substrate/class with a formal kill condition.
* Reading rules inherit identically across both projections.
