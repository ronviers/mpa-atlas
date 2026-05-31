# MPA — FDR, gFDR, and the Two-Frame Structure

**Scope.** How fluctuation–dissipation relations enter the character projection: the translation discipline that adopts them, the NESS-general form, the two conjugate frames it splits into, why those frames are the two faces of the Boolean→MPA deformation — with the **Central Commitment derived as the iff-chain's falsifiable direction** rather than asserted.

**Notation.**

| symbol | meaning |
|---|---|
| $C(t,t')$ | correlation $\langle x(t)x(t')\rangle$ |
| $R(t,t')$ | response $\delta\langle x(t)\rangle/\delta h(t')$ |
| $\chi$ | integrated susceptibility $\int R\,dt'$ |
| $X$ | external-frame violation factor (amplitude face) |
| $T,\ T_{\text{sub}}$ | bath temperature; substrate-equivalent decay-driving parameter |
| $T_{\text{eff}}=T/X$ | effective temperature (FD-plot slope) |
| $\alpha_s,\ P_s$ | aging slope, plateau (amplitude-face observables) |
| $\mathcal{A}$ | cycle affinity $\oint v/D_0=\ln(\prod_+k/\prod_-k)$ in nats (sign-topological face) |
| $J\ (J_{ss})$ | circulating current (steady-state magnitude) |
| $\langle\sigma\rangle$ | entropy-production rate |
| $\mathcal{T}$ | tightness — self-frame violation factor (engine `FRAMES` calls this $T$; we write $\mathcal{T}$ here to disambiguate from bath temperature) |
| $\mathrm{SNR}_J$ | $\langle J\rangle^2/\mathrm{Var}(J)$ |
| $V_{\text{ext}}$ | integrated external FDR-violation |
| $\triangle$ | frustrated triad (gauge-imbalanced 3-cycle; `pa:signed-balance`); $k_{\text{frust}}$ its dynamical consequence |
| chit | $\ln(G_0/L)$, measured in **ch** ($1\,\text{ch}\equiv\ln 2$ nats) |
| $D$ vs $D_0$ | drive $\Phi^*/\kappa$ vs diffusion constant; the affinity integral uses $D_0$ |

Eponym attribution: every borrowed result resolves to `mpa_prior_art.md` by its `pa:` key. The framework's own reading is identified by `(MPA)` only where the contrast would otherwise be ambiguous; otherwise the residual rule applies — what is not pointed at the ledger is owned.

---

## 1. The translation discipline

FDR enters by the structural→character translation; each step guards one failure mode.

1. **Deep commonality** — what the source actually formalizes, substrate-stripped (guards forced analogies).
2. **Audit hidden assumptions** — equilibrium baseline, fixed $T$, single observable, stationarity, linear response, passive probe, detailed balance (guards smuggled assumptions).
3. **Filter each concept** — direct / modified / no-transfer against the character filter (objects exist only during sustained NESS traversal, finite budgets, fail by fraying, feedback-coupled). Guards all-or-nothing.
4. **Replace the no-transfer items** — gaps are where character math is forced to do new work (guards hand-waving).
5. **Import established machinery** for the replacements; resist local invention (guards reinvention; every import resolves to a `pa:` key).
6. **Verify integration** under the filter; concept-by-concept transfer ≠ a coherent whole (guards false closure).

The two-frame structure below is itself a product of this discipline: it appeared when Step 5's velocity-form FDR-violation identity (`pa:harada-sasa`) was pressed against the force–flux / precision machinery (`pa:tur`) and checked for integration. *Working the translation updated the framework.*

## 2. The structural object and its NESS generalization

FDR ties two observables of a stochastic process:
$$C(t,t')=\langle x(t)x(t')\rangle,\qquad R(t,t')=\frac{\delta\langle x(t)\rangle}{\delta h(t')}.$$
Equilibrium ties them by $1/T$; the NESS-general form (`pa:ck-aging`) inserts a violation factor $X$:
$$R(t,t')=\frac{X(t,t')}{T}\,\frac{\partial C(t,t')}{\partial t'}\,\theta(t-t'),\qquad X\equiv1\ \text{at equilibrium}.$$
On the FD plot ($\chi$ vs $1-C/C(0)$) the local slope sets the effective temperature: $T_{\text{eff}}=T/X$.

Direct transfers (Steps 1–3): $C, R, X$, the FD plot, the aging diagonal, the plateau $C\to q_{EA}$. Modified: $T\to T_{\text{eff}}$.

## 3. What the character filter forces

No-transfer items (Step 4) and their imports (Step 5):

- $T\to T_{\text{sub}}$ — mode- and history-dependent (no fixed reservoir temperature outside equilibrium). (MPA)
- $X(t,t')\to X(t,t',\tau_{\text{obs}})$ — window-dependent (substrate-conditional reading rule F.2). (MPA)
- passive → active probe — response feeds back through the maintenance dynamics; active band $|\omega-\omega_{RO}|\lesssim\gamma_{RO}$. (MPA)
- equilibrium → degenerate $X\equiv1$ case.

The decisive import is the velocity-form FDR-violation identity (`pa:harada-sasa`):
$$J_{\text{diss}}=\gamma\left[\langle v\rangle^2+\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}\Big(\tilde C(\omega)-2T\tilde R'(\omega)\Big)\right],$$
where the integrand vanishes at equilibrium. **The integrated FDR-violation is the dissipation rate** — no absolute $T$ needed. This is the hinge that unlocks §4.

## 4. The two conjugate frames

Step 6 surfaces that the fluctuation–response relation has two conjugate frames — *one dissipation, two readings* (the recognition that FDR-violation and precision-cost are connected readings of one dissipation is a concurrent move in the field; `pa:fdr-tur-unification`):

$$\underbrace{(\text{amplitude}\times h)\to X}_{\textbf{external frame}}\qquad\qquad\underbrace{(J\times\mathcal{A})\to\mathcal{T}}_{\textbf{self-probe frame}}$$

- **External** — observables $\alpha_s, P_s$, factor $X$. **Substrate-conditional**: needs a probe matched to the substrate.
- **Self-probe** — the system's own topologically-forced circulation is the reference (`pa:tur`):
$$\mathcal{T}=\langle\sigma\rangle\,\frac{\mathrm{Var}(J)}{2\langle J\rangle^{2}}\ge1,\qquad \mathrm{SNR}_J=\frac{\langle J\rangle^{2}}{\mathrm{Var}(J)}\le\frac{\langle\sigma\rangle}{2}.$$
  Dimensionless (affinity in nats). **Defined iff a current exists.**

**Definedness asymmetry — the load-bearing fact (MPA).** The external frame is defined wherever a probe couples; the self-probe is defined iff a current exists ($k_{\text{frust}}$-bearing). This is what makes the self-probe **intrinsic** — no external probe, no substrate-matching — and the frame's *existence* is itself a topological diagnostic. The two frames are not parallel by construction; they coincide only on the subset of substrates where the self-probe is defined.

**Bridge** (`pa:harada-sasa`): $\;V_{\text{ext}}=\langle\sigma\rangle=J\cdot\mathcal{A}.\;$ Holds at **verdict / onset**; the exact magnitude identity owes the velocity-form integral (open numerical-identity refinement).

**Derivation — the Central Commitment, recovered (MPA).** From the definedness asymmetry plus standard machinery:
$$\text{self-probe defined}\;\Longleftrightarrow\;J\ne0\;\Longleftrightarrow\;\mathcal{A}\ne0\;\Longleftrightarrow\;\triangle\ \text{in coupling graph}.$$
- $J\ne0\Leftrightarrow\mathcal{A}\ne0$ by detailed-balance reversibility (`pa:kolmogorov-reversibility`); $\mathcal{A}=0$ is the gauge-balanced, real-spectrum case (`pa:signed-balance`).
- $\mathcal{A}\ne0$ gauge-irremovable $\Leftrightarrow\triangle$ in the coupling graph: $N=2$ currents are gauge-removable; the minimal protected carrier is the imbalanced, non-reciprocal, chiral 3-cycle (MPA def; `pa:may-leonard` cyclic dynamics).

The **Central Commitment** — *protected circulation ⇒ triad* — is the falsifiable direction of this iff-chain, **not an independent axiom**. The commitment is what the two-frame structure says about the world; the frame structure is what the iff-chain says about MPA. (Engine `TRIAD/COMMIT` and receipts §Central commitment carry the chain; this section is its derivation.)

## 5. Why these are the frames — the deformation's two faces

The two frames are not parallel by accident: they are the two **independent faces** of the Boolean→MPA deformation, read as fluctuation–response.

- **Amplitude face** — $\text{chit}/D$ drives $c\to s\to r$; observables $\alpha_s,P_s$ → external frame.
- **Sign-topological face** — balance of the signed coupling graph (`pa:signed-balance`); order parameter $\mathcal{A}$ → self-probe frame.

Boolean ($D\to\infty$) is the **balanced / gaugeable ring**: every signed cycle has even negative parity, a node gauge $\varepsilon\in\{\pm1\}^N$ unsigns it, the spectrum is real, **no protected current**. Detailed balance is this degeneracy.

The minimal departure is the frustrated triad $\triangle$ — directed, non-reciprocal ($M_{ij}\ne M_{ji}$), gauge-imbalanced, chiral — emitting the self-frame pair (`pa:cycle-affinity`):
$$\mathcal{A}=\oint_C\frac{v}{D_0}=\ln\frac{\prod_+k}{\prod_-k}\ \text{(nats, gauge-invariant)},\qquad \mathrm{spec}(M)\ \text{complex pair}\ \Leftrightarrow\ \mathcal{A}\ne0.$$
Dynamical consequence: $k_{\text{frust}}$ — stationary state irreducibly NESS, $J\ne0$ topologically-forced; the complex spectrum (irreducible rotation) is the invariant, not fixed-point absence.

**Affinity vs magnitude** — the split that makes the self-probe reference *intrinsic*: $\mathcal{A}$ is intensive, drive-independent, topology-forced; $J_{ss}$ is extensive, scales with absolute kinetic rates, flows with chit. The **gain coefficient** (the $\mathrm{Re}$ eigenvalue / amplitude self-amplification rate) is neither — it is external-frame and stays an external constant (the pump/coupling $\mu+2\kappa$, $\delta$-flat); only $\mathcal{A}$ (and $J$'s magnitude) flow. So *continuous-amplitude autonomy is external-frame of necessity* — supplied, not minted — while chirality/topology mints legally (receipts §amplitude-autonomy, derived via the definedness asymmetry below). Three consequences lock in together:

- *Entropy production* — Schnakenberg with the imbalanced-triad affinity, $\langle\sigma\rangle=\sum_C J_C\mathcal{A}_C$; limit cycle $\sigma_{\text{frust}}=J_{ss}\oint v/D_0\,d\theta$ (`pa:cycle-affinity`).
- *Chit grounding* — the chit log is the Markovian specialization of orbit affinity, $\text{chit}_{\text{orbit}}=\oint v(\theta)/D_0(\theta)\,d\theta$, with $\text{chit}=\ln(G_0/L)$ the per-transition entropy production (`pa:crooks-ft`). One ch ($\equiv\ln 2$ nats) of headroom is one bit's worth of held character — the framework's quantum showing up on the thermo face.
- *Frame-disagreement falsifier* — independence of the two faces ⇔ two distinct functionals on the same dissipation ⇔ their **disagreement** is the falsifier.

## 6. Meters, verdict, status, falsifier

**Meters.** $\langle\sigma\rangle$ from the binned probability-current $\langle\sigma\rangle=\int P\,|v_{\text{curr}}|^2/D_0$, $v_{\text{curr}}=A-D_0\nabla\ln P$ (Fokker–Planck steady-state EP); external $X$ from the perturbed $(\Delta C,\chi)$ locus. Rotational-OU tare for both ($\langle\sigma\rangle=2\omega^2/\kappa$; $V_{\text{ext}}=\omega^2/[\kappa(\kappa^2+\omega^2)]$).

**Verdict** (receipts §gFDR two-frame `proven`): *same regime verdict wherever both frames are computable.* Numerical corroboration: one real substrate (class-B laser — both flag NESS) and one synthetic positive control (`driven_ring`, closing $\langle\sigma\rangle=J\cdot\mathcal{A}$ to verification precision); $\mathcal{T}\ge1$ wherever a current exists, near-saturated on limit cycles, loose on foci.

**Open**:
- *τ-window reconciliation* — `mpa_frontier.md` `τ-window-reconciliation` `[sharpening]`. Two formulations of $\mathcal{T}$ in working notes (τ-absorbed canonical vs τ-explicit handoff) must agree on one form.
- *Exact magnitude identity* — the velocity-form Harada–Sasa integral closing $V_{\text{ext}}=\langle\sigma\rangle=J\cdot\mathcal{A}$ numerically. (Refinement, not a gate; the verdict-level claim is already promoted.)
- *Self-probe payoff instance* — a real substrate where $\mathcal{T}$ recovers a verdict the external frame cannot, demonstrating the intrinsic-reference advantage.

**Falsifier**: a substrate where, both probes feasible at the same operating point, $\mathcal{T}$ and $X$ give *contradictory* regime verdicts (engine `TWO-FRAME CONSTRUCTION`; receipts §gFDR verdict-agreement). The architectural commitment carries a sharper, dual falsifier — the *iff-chain break*: frame machinery works and verdict-agreement holds, yet no frustrated triad in the coupling graph (engine `TWO-FRAME CONSTRUCTION` § FALSIFY; receipts §Two-Frame Construction; promoted to the core 2026-05-30 via `battery:sign-interior` RV1 on RPS — receipts §commit-line crossing).

**Named prediction** (homochirality — receipts §Homochirality, `proven` 2026-05-30, real-instanced on `homochiral_triad.py`): biological homochirality is the gauge-irremovable chimeric sign of a $\triangle$ in the chirality-maintenance network — a single handedness held against racemization. Decisive test = drive-sweep: titrate metabolic drive $\to0$ and current magnitude $|J|$ collapses toward racemic ($r$-quench) while the *sign* ($\mathrm{sign}(\mathcal{A})$ = which hand) stays invariant. A handedness flip under drive titration falsifies — the affinity-vs-magnitude split (§5) turned into a kill condition.

---

*Imports* (all `pa:` keys → `mpa_prior_art.md`): `ck-aging`, `harada-sasa`, `tur`, `signed-balance`, `cycle-affinity`, `kolmogorov-reversibility`, `may-leonard`, `crooks-ft`. Everything else — the iff-chain derivation, the two-faces identification, $\triangle$ as minimal carrier, $k_{\text{frust}}$, the affinity-vs-magnitude split, the homochirality stake — is the residual MPA owns by the prior-art ledger's exclusion rule.
