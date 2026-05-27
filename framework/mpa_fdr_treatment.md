# MPA — FDR, gFDR, and Two-Frame FDR (unified treatment)

**Scope.** How fluctuation–dissipation relations enter the MPA character projection: the discipline that adopts them, the generalized (NESS) form, the two conjugate frames the generalization splits into, and why those frames are the two faces of the Boolean→MPA deformation. Supersedes the three working notes (six-step process · two-frame math · Harary grounding).

**Provenance tags.** **[est.]** established literature · **[MPA]** framework's own move · **[num.]** program result (minimal models / one real substrate).

**Notation (harmonized).**

| symbol | meaning |
|---|---|
| $C(t,t')$ | correlation function $\langle x(t)x(t')\rangle$ |
| $R(t,t')$ | response (impulse) function $\delta\langle x(t)\rangle/\delta h(t')$ |
| $\chi$ | integrated susceptibility $\int R\,dt'$ |
| $X$ | external-frame violation factor (amplitude face) |
| $T,\ T_{\text{sub}}$ | bath temperature; substrate-equivalent decay-driving parameter |
| $T_{\text{eff}}=T/X$ | effective temperature (FD-plot slope) |
| $\alpha_s,\ P_s$ | aging slope, plateau (amplitude-face observables) |
| $\mathcal{A}$ | cycle affinity $\oint v/D_0=\ln(\prod_+k/\prod_-k)$, nats (sign-topological face) |
| $J\ (J_{ss})$ | circulating current (steady-state magnitude) |
| $\langle\sigma\rangle$ | entropy-production rate |
| $\mathcal{T}$ | TUR-tightness = self-frame violation factor |
| $\mathrm{SNR}_J$ | $\langle J\rangle^2/\mathrm{Var}(J)$ |
| $V_{ext}$ | integrated external FDR-violation |
| $\triangle_H,\ k_{\text{frust}}$ | Harary triad; topologically-forced NESS circulation |
| chit | $\ln(G_0/L)$ |
| $D$ vs $D_0$ | drive $\Phi^*/\kappa$ vs diffusion constant |
| $\omega_{RO},\ \gamma_{RO}$ | relaxation-oscillation frequency, linewidth (active-probe band) |

Two harmonizations: (i) the self-frame violation factor is the **TUR-tightness**, written $\mathcal{T}$ to avoid collision with temperature $T$ — the source-of-truth `mpav1_compressed` calls it $T$; (ii) the affinity integral $\oint v/D_0$ uses the **diffusion constant** $D_0$, distinct from the drive parameter $D=\Phi^*/\kappa$ (the source overloads $D$ for both).

---

## 1. The translation discipline (six steps) **[MPA method]**

FDR is adopted by the structural→character translation; each step guards one failure mode.
1. **Deep commonality** — what relation does the source actually formalize, substrate-stripped? *(guards forced analogies)*
2. **Audit hidden assumptions** — equilibrium baseline, fixed $T$, single observable, stationarity, linear response, passive probe, detailed balance. *(guards smuggled assumptions)*
3. **Filter each concept** — direct / modified / no-transfer against the character filter (objects exist only during sustained NESS traversal, finite budgets, fail by fraying, feedback-coupled). *(guards all-or-nothing)*
4. **Replace the no-transfer items** — the gaps are where character math is forced to do new work. *(guards hand-waving)*
5. **Import established machinery** for the replacements; resist local invention. *(guards reinvention)*
6. **Verify integration** under the filter; concept-by-concept transfer ≠ a coherent whole. *(guards false closure)*

The two-frame structure below is itself a product of this discipline: it appeared only when Step 5's Harada–Sasa import was pressed against the force–flux / TUR machinery and checked for integration (Step 6). *Working the translation updated the framework.*

## 2. The structural object and its NESS generalization **[est.]**

FDR ties two observables of a stochastic process:
$$C(t,t')=\langle x(t)x(t')\rangle,\qquad R(t,t')=\frac{\delta\langle x(t)\rangle}{\delta h(t')}.$$
Equilibrium ties them by $1/T$; the NESS-general Cugliandolo–Kurchan form inserts a violation factor $X$ (sign convention on the derivative varies by author):
$$R(t,t')=\frac{X(t,t')}{T}\,\frac{\partial C(t,t')}{\partial t'}\,\theta(t-t'),\qquad X\equiv1\ \text{at equilibrium}.$$
On the FD plot — integrated susceptibility $\chi$ vs $1-C/C(0)$ — the local slope sets the effective temperature:
$$\text{slope}=-\frac{X}{T}\equiv-\frac{1}{T_{\text{eff}}},\qquad T_{\text{eff}}=\frac{T}{X}.$$
Direct transfers (Steps 1–3): $C,R,X$, the plot, aging diagonal, plateau $C\to q_{EA}$. Modified: $T_{\text{eff}}$.

## 3. What character domain forces **[MPA replacements; est. imports]**

No-transfer items (Step 4) and their imported machinery (Step 5):
$$T\to T_{\text{sub}}\ (\text{mode-, history-dependent}),\qquad X(t,t')\to X(t,t',\tau_{obs})\ (\text{window-dependent}),$$
passive → active probe (response feeds back through the maintenance dynamics; band $|\omega-\omega_{RO}|\lesssim\gamma_{RO}$); equilibrium demoted to the degenerate $X\equiv1$ case. The decisive import is the **Harada–Sasa equality** (velocity form, $k_B=1$; prefactors verified vs PRL **95** 130602):
$$J_{diss}=\gamma\left[\langle v\rangle^2+\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}\Big(\underbrace{\tilde C(\omega)-2T\,\tilde R'(\omega)}_{\text{FDR violation}}\Big)\right],$$
$\tilde R'$ = real part of the response spectrum; at equilibrium $\tilde C=2T\tilde R'$ and the integrand vanishes. The **integrated violation is the dissipation rate** — no absolute $T$ needed. This is the hinge into §4.

## 4. The two conjugate frames (Step-6 output) **[MPA structure]**

Verifying integration surfaces that the fluctuation–response relation has **two conjugate frames** — one dissipation read two ways:
$$\underbrace{(\text{amplitude}\times h)\to X}_{\textbf{external frame}}\qquad\qquad\underbrace{(J\times\mathcal{A})\to\mathcal{T}}_{\textbf{self-probe frame}}$$

- **External** — standard $c/s/r$ story; observables $\alpha_s,P_s$, factor $X$. Needs an external probe; substrate-conditional. **[est. apparatus]**
- **Self-probe** — the system's own topologically-forced circulation is the reference. Dimensionless (affinity in nats); **defined iff a current exists**. **[est. TUR / MPA framing]**
$$\mathcal{T}=\langle\sigma\rangle\,\frac{\mathrm{Var}(J)}{2\langle J\rangle^{2}}\ge1,\qquad \mathrm{SNR}_J=\frac{\langle J\rangle^{2}}{\mathrm{Var}(J)}\le\frac{\langle\sigma\rangle}{2}.$$
  (Dimensional consistency requires $J$ and $\langle\sigma\rangle$ on a matched window $\tau$; the 2026-05-21 handoff carried $\tau$ explicitly, the source-of-truth form absorbs it — a discrepancy to reconcile.)
- **Bridge (Harada–Sasa):** $\;V_{ext}=\langle\sigma\rangle=J\cdot\mathcal{A}.\;$ Holds at **verdict/onset**, not as numerical identity — exact magnitude equality is owed to the velocity-frame Harada–Sasa integral. **[est. bridge / MPA identification]**

## 5. Why those are the frames — the deformation's two faces **(the tie)**

The two frames are not parallel by accident: they are the two **independent faces** of the Boolean→MPA deformation, read as fluctuation-response.
- **Amplitude face** — $\text{chit}/D$ drives $c\!\to\!s\!\to\!r$; observables $\alpha_s,P_s$ → external frame. **[MPA]**
- **Sign-topological face** — Harary balance of the signed coupling graph; order parameter $\mathcal{A}$ → self-probe frame. **[MPA]**

Boolean ($D\!\to\!\infty$) is the *balanced / gaugeable* ring: every signed cycle has even negative parity, gaugeable to real spectrum, **no protected current** — detailed balance is this degeneracy. **[MPA reading of est. Harary balance]**

The minimal departure is the **Harary triad** $\triangle_H$ — a directed, non-reciprocal ($M_{ij}\ne M_{ji}$), Harary-unbalanced (odd negative-edge parity; no node gauge balances), chiral 3-cycle: the minimal carrier of gauge-irremovable circulation. It emits exactly the self-frame pair: **[MPA def; est. Schnakenberg]**
$$\mathcal{A}=\oint_C\frac{v}{D_0}=\ln\frac{\prod_+k}{\prod_-k}\ (\text{nats, gauge-invariant}),\qquad \mathrm{spec}(M)\ \text{complex pair}\ \Leftrightarrow\ \mathcal{A}\ne0.$$
Its dynamical consequence is $k_{\text{frust}}$: the stationary state is irreducibly a NESS, a topologically-forced current $J\ne0$ (the complex spectrum — irreducible rotation — is the invariant, not fixed-point absence). **[MPA; survived R1/R2/R3]**

**Affinity vs magnitude** — the split that makes the self-probe reference *intrinsic*: $\mathcal{A}$ is intensive, drive-independent, topology-forced; $J_{ss}$ is extensive, scales with kinetic rates, flows with chit. Hence three things lock in:
- *Definedness:* "defined iff a current exists ($k_{\text{frust}}$-bearing)" $=$ iff $\mathcal{A}\ne0$ $=$ iff $\triangle_H$ present — the **Central commitment**, $\text{protected circulation}\Rightarrow\triangle_H$. **[MPA]**
- *Entropy production:* Schnakenberg with the Harary affinity, $\langle\sigma\rangle=\sum_C J_C\,\mathcal{A}_C$; limit cycle $\sigma_{\text{frust}}=J_{ss}\oint v/D_0\,d\theta$. **[est.]**
- *Chit:* the chit log is the Markovian specialisation of the same orbit affinity, $\text{chit}_{\text{orbit}}=\oint v/D_0\,d\theta$, with $\text{chit}=\ln(G_0/L)$ the per-transition Crooks entropy production. **[MPA / est. Crooks]**

Independence of the two faces $\Leftrightarrow$ the two frames are different functionals $\Leftrightarrow$ their **disagreement** is the falsifier.

## 6. Meters, verdict, status, falsifier

**Meters [num.].** $\langle\sigma\rangle$ from the binned probability-current $\langle\sigma\rangle=\int P\,|v_{\text{curr}}|^2/D_0$, $v_{\text{curr}}=A-D_0\nabla\ln P$ **[est. Fokker–Planck steady-state EP]**, tared on rotational OU ($\langle\sigma\rangle=2\omega^2/\kappa$); external $X$ from the perturbed $(\Delta C,\chi)$ locus, tared on $C_{xx}=(D_0/\kappa)e^{-\kappa\tau}\cos\omega\tau$ and $V_{ext}=\omega^2/[\kappa(\kappa^2+\omega^2)]$ **[est., exact for the model]**.

**Verdict (promoted, the weaker claim).** *Same regime verdict wherever both frames are computable.* Confirmed on a real substrate (class-B laser — both flag NESS) and closed exactly on `driven_ring` ($\langle\sigma\rangle=J\cdot\mathcal{A}$). Tightness: $\mathcal{T}\ge1$ wherever a current exists (limit cycle $\mu=1$ nearly saturates, $\mathcal{T}\approx1.2$; foci loose, $\mathcal{T}\sim15$–$32$); $\langle\sigma\rangle$ meter ~13% (2% at high $\sigma$), external tare 5–7%. **[num.]**

**Open gate.** Exact cross-frame magnitude identity (velocity-frame Harada–Sasa); plus a real-substrate §846 clear — either $\mathcal{T}$-vs-$X$ agreement, or the payoff: a self-probe-only reading where $\mathcal{T}$ recovers a verdict the external frame cannot. **Falsifier:** a substrate where, both probes feasible, $\mathcal{T}$ and $X$ give *contradictory* regime verdicts.

**Named prediction — biological homochirality [MPA, un-instanced].** A single handedness held against racemization is the gauge-irremovable chimeric sign of a $\triangle_H$. Drive-sweep: ATP/GTP $\to0$ collapses $|J|$ toward racemic while the *sign* ($\mathcal{A}$'s sign = which hand) stays invariant. A handedness flip falsifies — the affinity-vs-magnitude split (§5) turned into a kill condition.

---
*Provenance.* **Established:** $C,R$; CK gFDR + $X$ + $T_{\text{eff}}$; Harada–Sasa (prefactors verified); Schnakenberg $\mathcal{A}$ and $\langle\sigma\rangle=\sum J\mathcal{A}$; TUR; Harary balance; FP steady-state EP; rotation $\leftrightarrow$ broken detailed balance. **Framework's own:** $T_{\text{sub}}$, window-dependent $X$, active-probe band, the conjugate-frame structure, the two-faces identification, $\triangle_H$ as minimal carrier, $k_{\text{frust}}$, affinity-vs-magnitude, chit grounding, homochirality. **Program (models / one real substrate):** R1/R2/R3, laser + `driven_ring`, tightness and meter figures — full gate open.
