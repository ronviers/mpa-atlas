# The Translation Process — Six Steps (math)

FDR worked example. Each step guards against one failure mode. Provenance tags: **[est.]** = established literature, **[MPA]** = bespoke to this framework.

> **Inbound twin:** `transport_law_steps.md`. This recipe brings an import *into* the framework (translation); that one gets predictions *out* of imports already adopted (transport laws).

**Step 1 — deep commonality.** Two observables of a stochastic process and the relation between them: **[est.]**
$$C(t,t')=\langle x(t)\,x(t')\rangle,\qquad \chi(t,t')=\frac{\delta\langle x(t)\rangle}{\delta h(t')}$$
Equilibrium ties them through one constant $1/T$; the NESS-general (Cugliandolo–Kurchan) form inserts a violation factor $X$ (response $R=\partial_t\chi$; sign convention on the derivative varies by author):
$$R(t,t')=\frac{X(t,t')}{T}\,\frac{\partial C(t,t')}{\partial t'}\,\theta(t-t'),\qquad X\equiv 1\ \text{at equilibrium.}$$

**Step 2 — hidden assumptions.** Each is a constraint the equations silently carry: $T=\text{const}$; time-translation invariance $C(t,t')=C(t-t')$; linearity; Gaussian/Markovian; detailed balance $\Leftrightarrow X\equiv 1$. Character domain breaks essentially all of them. **[est. assumptions; MPA audit]**

**Step 3 — filter into buckets.** Classification rides on the FD (parametric) plot of integrated response $\chi$ vs $1-C/C(0)$, whose local slope sets the effective temperature: **[est.]**
$$\text{slope}=-\frac{X}{T}\equiv-\frac{1}{T_{\text{eff}}},\qquad T_{\text{eff}}=\frac{T}{X}.$$
**Direct:** $C,\ \chi,\ X$, the plot, aging diagonal, plateau $C\to q_{EA}$. **Modified:** $T_{\text{eff}}$. **No transfer:** single-window readout, linear response, passive probe, detailed-balance default. **[MPA sort]**

**Step 4 — replacements for the "no transfer" items.** **[MPA]**
$$T\;\longrightarrow\;T_{\text{sub}}\ (\text{mode-, history-dependent}),\qquad X(t,t')\;\longrightarrow\;X(t,t',\tau_{obs}),$$
passive $\to$ active probe (response now includes feedback through the maintenance dynamics); equilibrium demoted to the degenerate $X\equiv 1$ (zero-drive) special case.

**Step 5 — import machinery.** Harada–Sasa: integrated FDR-violation **is** the dissipation rate, no absolute $T$ needed (velocity form, $k_B=1$): **[est. — exact prefactors per PRL 95, 130602]**
$$J=\gamma\left[\langle v\rangle^2+\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}\Big(\underbrace{\tilde C(\omega)-2T\,\tilde R'(\omega)}_{\text{FDR violation}}\Big)\right],$$
$\tilde C$ = velocity-autocorrelation spectrum, $\tilde R'$ = real part of the response spectrum; at equilibrium $\tilde C=2T\tilde R'$ and the integrand vanishes. Plus Cugliandolo–Kurchan ($X$-apparatus) and time–bandwidth bounds $\Delta\omega\,\Delta t\gtrsim 1$ for the multi-window reading.

**Step 6 — verify integration.** The chit acquires a thermodynamic derivation as the per-event rate-ratio; the same dissipation reads as current × affinity (Schnakenberg **[est.]**), bounded by the TUR (Barato–Seifert; $\Sigma$ = total entropy production **[est.]**):
$$\text{chit}=\ln\frac{G_0}{L}\;\overset{\text{[MPA]}}{=}\;\langle\sigma\rangle_{\text{event}},\qquad \langle\sigma\rangle=\sum_\rho J_\rho\,\mathcal{A}_\rho,\qquad \frac{\mathrm{Var}(J)}{\langle J\rangle^{2}}\,\Sigma\ge 2.$$
Active-probe band set by the relaxation-oscillation resonance: $|\omega-\omega_{RO}|\lesssim\gamma_{RO}$. **[MPA]**

> Note: working out the translation *itself updates the framework* — it is part of development, not downstream presentation.

---
*Provenance:* equations are the established closed forms (Tier 1) behind the source document's verbal statements; the document names these quantities but does not write most of them out. Prefactors verified against primary sources where marked. **[MPA]** items are the framework's own constructions, reported as its claims rather than established physics.
