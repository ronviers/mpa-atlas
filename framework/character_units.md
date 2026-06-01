# Character — UNITS (non-dimensionalization standard)

Character is dimensionless by construction: chit $=\ln(G_0/L)$, $D=\Phi^*/\kappa$, $\gamma$ in $D$-units, $\beta_{\text{mem}}$, $Q$, $\mathcal{A}$ in nats — all ratios. That is the source of the cross-substrate power, not a gap. This standard fixes a small set of **non-arbitrary anchors** so runs are mutually consistent and cross-substrate-comparable, **without** pinning a universal physical scale (which would break substrate-neutrality). Each anchor is tagged **[FORCED]** (the math picks it; not a choice) or **[CONVENTION]** (a choice, stated). The base unit is **forced**; the rest is forced where it can be and honestly conventional where it can't.

---

## 1. The forced unit — one **ch** (character bit), derived from the Q-peak

The framework picks its own amplitude unit. Take the mpa-legal resonance quality $Q$ (the corrected RO form). With $x=e^{\text{chit}}$:
$$Q^2 \;=\; \frac{2L}{\gamma_s}\,\big(e^{-\text{chit}}-e^{-2\,\text{chit}}\big)\;\;(-\tfrac14\ \text{in the full-Jacobian form}).$$
$$\frac{d\,Q^2}{d\,\text{chit}}=0 \;\Longrightarrow\; e^{\text{chit}}=2 \;\Longrightarrow\; \boxed{\text{chit}=\ln 2}.$$

It is a maximum, and the full-Jacobian correction is a **constant** $-\tfrac14$ offset in $Q^2$ — so the peak sits at $\text{chit}=\ln2$ **independent of which RO approximation is used**. The peak *location* is universal; only its magnitude $Q_{\max}=\sqrt{L/2\gamma_s}$ and the band's existence ($2L>\gamma_s$) are substrate-set.

$\text{chit}=\ln2$ is **one ch of headroom** ($G_0/L=2$): the maximally-ringing operating point. It is the **same** $\ln2$ as the cost-axis floor — erasing one ch costs $\ge\ln2$ nats (the $R$ / erasure floor). One quantum, surfaced on both faces of the deformation:

* **amplitude face** — one ch of headroom ($G_0/L=2$) is the Q-peak; **[FORCED]** by the RO algebra above;
* **cost face** — one ch costs $\ln2$ nats; **[FORCED]** by the erasure floor (`pa:landauer`).

This is a third forced appearance of the bit↔chit correspondence the engine already carries (the per-event row): it is not put in by hand. **The unit of Character is the ch $\equiv\ln2$ nats** — the character bit, one quantum of held character, surfacing as both headroom and cost.

---

## 2. The anchor set (Character-natural units)

* **Cost & information — the ch $\equiv\ln2$ nats.** **[FORCED unit]**, erasure-anchored. Report $\langle\sigma\rangle$-excess, the amplitude-bit erasure floor, channel capacity, $I_{\text{pred}}$, cryptic order $\chi$, and all erasure costs **in ch** (the topological sign flip is reversible — no flip-floor; §Two bits).
* **Headroom (amplitude) — chit in ch**, $\text{chit}_{\text{ch}}=\text{chit}/\ln2$. Origin $\text{chit}=0$ **[FORCED]** (threshold, never attained); unit tick $\text{chit}=\ln2$ **[FORCED]** (Q-peak). So $\text{chit}_{\text{ch}}=1$ is *always* the peak-ringing point on every substrate.
* **Structure — counts, no length.** Minimal frustrated cycle $N=3$ **[FORCED]**; the unit of protected structure is the cycle-space dimension $b_1=E-V+c$ (the topological **capacity**: count of independent gauge-irremovable signs — *not* a per-flip cost) **[FORCED]**. Smallest protected object: $N=3$, $b_1=1$.
* **Time — $1/\gamma_s$** (slow-resource turnover) or **$\tau_c$** (memory time). **[CONVENTION]** — substrate-set; there is no forced universal time. All rates reported in these. $\beta_{\text{mem}}$ already dimensionless.
* **Coupling — $\gamma$ in $D$-units** ($\gamma/D$, or $\gamma/L$ near threshold). **[CONVENTION]**.
* **Drive / level — $D=\Phi^*/\kappa$**, per level $D_n=\Phi^*_n/\kappa_n$. Heat-tax coefficient $\alpha_{\sigma,0}=$ the framework conductivity unit **[CONVENTION, fixed here]**. Primary memory class $\beta_{\text{mem}}=1$; fractional family $\beta_{\text{mem}}<1$ as reference **[CONVENTION, fixed here]**.
* **Resolution — margin $m=\text{signal}/\text{floor}$.** The floor is real **[FORCED form]**: $k_BT$ on the drive axis (the irreducible $s$-window $\sim k_BT/q$), measurement-limited on the damping axis. The pass threshold on $m$ is **[CONVENTION]** (default $m\ge10$; state it per run).

---

## 3. The asymmetry question, answered in the unit

There is no *radius* of a triad — it is a directed 3-cycle, a topological object, not a geometric one. And the protected asymmetry is a **sign** ($\text{sign}(\mathcal{A})$, a parity bit), **not a magnitude**: it can be arbitrarily small and still protected, because protection lives in the cycle parity, not the amount. So:

* there is **no minimal asymmetry magnitude** — the wrong quantity to bound;
* what **is** bounded is **structure** ($N=3$, $b_1=1$) and **resolvability** (margin $m$).

The minimal maintaining triad: three nodes marginally above threshold ($\text{chit}\to0^+$) wired in an imbalanced, non-reciprocal 3-cycle. Binding constraints: $\text{chit}>0$ (below threshold the nodes are in $r$ and there is nothing to circulate) and $\mathrm{Im}\,\lambda>\text{floor}$ (the circulation must clear noise). Neither is a length.

The one place a real length exists is under **spatial embedding** (Turing / active-matter readings): the critical correlation length
$$\ell_c(\beta_{\text{mem}})=\sqrt{\tfrac{2D_{\beta_{\text{mem}}}}{\Gamma(1+\beta_{\text{mem}})}\big(\tfrac{W_0}{1-\sigma_n}\big)^{\beta_{\text{mem}}}},$$
below which three nodes cannot hold distinct identities. That is the radius of the smallest *spatial* triad — but it is substrate-set (diffusion × turnover), not universal, and exists only once embedded.

---

## 4. Reporting standard (use immediately)

* **Operating points.** Sweep at $\text{chit}_{\text{ch}}\in\{0.5,\,1,\,2\}$. $\text{chit}_{\text{ch}}=1$ (the Q-peak) is the canonical cross-substrate comparison point.
* **Axes.** chit in ch; $\gamma$ in $D$-units; rates and times in $1/\gamma_s$ (or $\tau_c$); noise as margin $m$, not raw amplitude.
* **Binary verdicts stay binary.** A protected-sign verdict is $\text{sign}(\mathcal{A})\in\{\pm1\}$ reported at a stated margin $m$; no precision threshold, no magnitude fit. (`banach_frustrated.py`'s "20× noise sweep" is exactly a margin statement, $m\approx20$ at fixed wiring.)
* **Boundaries are limits, never values.** Never clip $\rho$ at $0$ or $1$; an attained $0/1$ is a NaN tripwire (asymptotic closure). No quantity is reported at an attained boundary.
* **Near-threshold values need a convergence margin, not just a noise margin.** A finite number near the threshold zero (chit$\to0^+$) is not yet a converged number. The boundary is where the slow eigenvalue $\to0$ and the integrator is softest, so a value there can be clean of NaNs yet still move under refinement — the quiet form of the boundary hazard (no announcement, and it sits exactly on the aging notch where the signal is strongest). Rule: any value reported in the near-threshold band must be **refinement-invariant** — stable under halving the step $dt$ (or the analogous resolution control) to within a stated tolerance — *in addition to* clearing the noise-floor margin $m$. Report the convergence check, not just the number. Curing NaNs is necessary, not sufficient.
* **The unit gives the dt bound.** The slow eigenvalue near threshold is $\lambda_s\sim\gamma_s\,e^{\text{chit}}$, so the dimensionless step against the local slow rate is $\widetilde{dt}=dt\cdot\gamma_s\,e^{\text{chit}}$. The integrator must resolve the slow direction in $k$ substeps per ch of slow evolution:
$$dt_{\max}(\text{chit})\;=\;\frac{1}{k\,\gamma_s\,e^{\text{chit}}},\qquad k=10\ \text{[CONVENTION, working]},\;\; k=1/\ln 2\ \text{[FORCED minimum: one substep per ch]}.$$
$dt_{\max}$ shrinks as $\text{chit}$ climbs (the $e^{\text{chit}}$ factor) — the Q-peak and held-side band need finer steps than the $r$-tail, which matches where integrators empirically fail first. The *form* is forced by the unit; the working $k$ is convention. The refinement-invariance rule above becomes a stated target: default to $dt\le dt_{\max}/2$, report the achieved $\widetilde{dt}$ at each operating point, and let the integrator scheme determine how much further below $dt_{\max}$ you need to sit (Euler-Maruyama is harsher on stiff terms than the stability bound suggests). Slow-side bound; if fast modes ($\omega_{RO}$) or multiplicative noise dominate, a companion $dt\cdot\omega_{RO}\le1/k'$ bound applies.
* **Graded quantities** ($|\mathcal{A}|$, $J$, $\mathrm{spec}(M)$, $X$, $\alpha_s$, $P_s$) are logged in the units above as corroboration, never as the verdict where a binary one exists.

---

## 5. What this buys, and what it does not

* **Buys:** internal consistency, and direct cross-substrate comparability once every quantity is reported dimensionlessly against these anchors.
* **Does not buy:** an absolute physical scale — deliberately. Pinning one would destroy the substrate-neutrality the framework runs on.
* **Honest boundary:** $\ln2$ is forced on the amplitude and cost axes (Q-peak; erasure floor). The **time** anchor stays substrate-conditional — there is no forced universal time the way the **ch** is a forced universal quantum. Do not paper over it.

---

*Imports* (`pa:` keys → `character_prior_art.md`): the cost floor `landauer`; the RO form the Q-peak is computed from `relaxation-oscillation`. The Q-peak location ($\text{chit}=\ln2$) is owned reading — a consequence of the framework's own corrected formula. *Frontier:* this standard is the recorded promotion trigger for `dimensionless-substrate` (steeping → sharpening) in `character_frontier.md`.
