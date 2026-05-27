# MPA (operational source of truth)

**Status:** Live. The operational source of truth for MPA — every protocol revision and dev workflow reads from this file. The full claim set at v9-style resolution: one phenomenology, two readings — a **STRUCTURAL** projection (discrete operator algebra, the finite-$D$ interior) and a **CHARACTER** projection (the continuous driven-dissipative dynamics that traverse it) — joined at a shared spine. Both apply to any substrate (glass, QEC, brain, behavioral, future).

**Companions:**
- [`mpav1_unabridged.md`](mpav1_unabridged.md) — public-facing prose-and-prior-art version (spine + two wings + references). Rebuilt from this file (+ receipts) periodically; allowed to lag. Do not lean on it for operational lookups.
- [`mpav1_receipts.md`](mpav1_receipts.md) — line-keyed justifications, derivations, and falsifier formalisations. Append-only during prove-as-you-go work; the file that makes unabridged reconstruction tractable.
- [`FALSIFICATION.md`](../FALSIFICATION.md) — the open attack front. Read it when asking *what are we trying to break?*

If this file disagrees with the unabridged, this file wins. If this file disagrees with receipts, treat as a bug. The structural and Character readings are complementary, not competing; a disagreement between them on a shared primitive is a bug.

Every claim states a predicted measurement on a named substrate (or substrate class) and is **mpa-legal** (dynamical quantities flow with the operating point; no inert constants where the physics requires flow).

---

# SPINE — the Boolean→MPA deformation

One organising fact: MPA *is* the finite-$D$ deformation of the Boolean ($D\to\infty$) ring. The reading runs **topology → asymptote** — from the signed coupling graph and Harary balance, to the open-interval boundaries the framework's observables approach but never attain at the Boolean ceiling. The deformation has **two independent faces** (amplitude, sign-topological); every spine section is a beat in that argument. One phenomenology, two complementary readings: a **STRUCTURAL** projection (discrete operator algebra, the finite-$D$ interior) and a **CHARACTER** projection (the continuous driven-dissipative dynamics that traverse it). Both apply to any substrate (glass, QEC, brain, behavioral, future). MPA adds no object: it imports the Reed–Muller/ANF ring, Harary balance, the May–Leonard cycle, Schnakenberg affinity, Cugliandolo–Kurchan aging, Wilson–Kadanoff RG, and Landauer-grounded stochastic thermodynamics, and reads each under sustained dissipation — the framework's content is the reading, the falsifiable transfer.

## Setting & primitives
$D = \Phi^*/\kappa$ (supplied work / dissipation scale) is the working parameter. Boolean structure is the $D\to\infty$ limit of operator action; at finite $D$ operators are dynamical actions on trail structure, and the predictive content is the *shape of the deviation* from that limit. Maintaining a proposition costs work; cut the work, structure dissolves. Substrate classes = the $(\Phi^*,\kappa)$ envelopes their realizers produce, intersected with the $D$ values the spec asks for.

Same setting, continuous register: a **coherence** is a macroscopic pattern of continuation maintained against natural dissolution; a **holding** is the continuous entropy-extraction / work-application that maintains it as a NESS. (Surface-code syndrome stream, glassy cage maintenance, Lotka–Volterra carrying-capacity adjustment, Rescorla–Wagner reinforcement loop — all holdings on one axis.)

**Primitives (unioned).**
- *Structural:* **trail vector** (kernel-weighted history while a proposition is active); drive $D$; observer kernel $\tau_{obs}$. Conflicting trails push the system in incompatible directions — destructive interference is the physical substrate of logical contradiction.
- *Substrate (Character):* gain rate $G_0$ (unsaturated pump rate above threshold, scales with $D$; laser small-signal gain), loss rate $L$ (spontaneous relaxation to bath; cavity loss), signed edge structure $\gamma_{AB}$. $G_0,L$ are both rates ($[\text{time}^{-1}]$; fixed by $(G_0-L)\rho$ and $\lambda_A\approx L-G_0$), so $\mathrm{chit}=\ln(G_0/L)$ is a dimensionless log-ratio of rates.
- *Derived primitive (operational anchor):* $\mathrm{chit}=\ln(G_0/L)$ — headroom above threshold. The framework's operational content keys to chit (full treatment §The chit unit).
- *Topological invariant:* $k_{\text{frust}}$ — cycle of $c$-edges with obstructive shear product, not resolvable by drive. Derived (heteroclinic-cycle consequence of the universal kernel + Harary balance); operational content — *the stationary state is irreducibly a NESS, a topologically forced circulating current* — survived the R1/R2/R3 ladder (Receipts §846; FALSIFICATION Finding 4). Elevation to a numbered primitive awaits a real cross-substrate instance (§Open items); the operational content stands without it.

## The deformation & its two faces

**Boolean section $\mathcal{M}_2$.** $\mathcal{M}=\{c,s,r\}$, $\mathcal{M}_2=\{c,r\}$. Three characterisations of the same two-cell set: codomain of $K$; fixed-point set of coarse-graining flow ($s$ metastable, migrates to $c$/$r$); section on which the limit-equivalence quotient $q:\mathcal{M}(\infty)\to\mathbb{B}$ is bijective. Restricting $\Sigma=\{C,S,K,R,\top,\bot\}$ to $\mathcal{M}_2$ gives $(\mathbb{B},\land,\lor,\oplus,\neg)$. Closure holds at the $\sigma$-shadow level, not the regime label: with $\mathcal{M}_2$-inputs $C$ can still produce $s$ (orthogonal/drive-covered merge) while $\sigma(s)=1=\sigma(c)\land\sigma(c)$ — homomorphism preserved even when the label strays.

**Reed–Muller / ANF, and what deforms.** $\mathcal{M}_2$ is the $\{\oplus,\land,1\}$ Reed–Muller / algebraic-normal-form ring ($\oplus=K$, $\land=C$, $1=\top$, $\neg=\oplus\,1$) — not a classical prejudice grafted on, but the algebraic ceiling the deformation runs toward. MPA is its finite-$D$ deformation. The deformed piece is the involution: $R$'s irreversibility ($c\to r$, non-involutive at finite drive) is the deformed Boolean negation; the drive $G_0$ (via the chit register $\ln(G_0/L)$) is the deformation coordinate, not the ring's unit $1$. This is the binding that tethers MPA to a known structure. (The deformation is a *matched* structure, not one global $1/D$ series: a regular $1/D$ expansion in the bulk and a **singular crossover** at the drive-threshold and switching seams — established home singular-perturbation / crossover-scaling, not Moyal-type regular deformation. §Deformation calculus, §Owed work.)

**Two faces.** The deformation carries two independent coordinates.
- **Amplitude face** (continuous): $\mathrm{chit}/D$ drives the $c\to s\to r$ migration; cross-substrate observables are the aging slope $\alpha_s$ and plateau $P_s$ (§FDR signatures). The Character projection traverses this face.
- **Sign-topological face** (topological): Harary balance of the signed coupling graph. Boolean is the *balanced/gaugeable* ring — every signed cycle has even negative parity, so a node gauge $\varepsilon\in\{\pm1\}^N$ renders it unsigned, spectrum real, no current protected. The deformation's sign-face is **Harary-imbalance**: the chimeric sign of a Harary triad (§Central commitment) *is* the coordinate away from balance — the ANF-ring deformation made dynamical — order parameter the gauge-invariant cycle affinity $\mathcal{A}$.

The two faces are coordinates of one deformation but **independent axes**. The sign-topological face is topological, not amplitude — it is the source of $k_{\text{frust}}$'s $\tau_{obs}$-invariance (§Scale-relativity), and organising the spine around the deformation does **not** couple $\alpha_s,P_s$ to $k_{\text{frust}}$. This independence is load-bearing and preserved throughout.

**Two bits, one per face.** The deformation carries a distinct bit on each face; their non-interconvertibility is the sharpest expression of the faces' independence.
- *Amplitude bit:* the $D\to\infty$ endpoint of the chit axis — a which-state (occupancy) distinction, *emergently* discrete (continuous until the limit). Erased by $R$ at the Landauer floor $W/\kappa\ge\ln 2$, must be *held* against thermal leak, flippable reversibly at no fundamental cost.
- *Topological bit:* the chimeric sign of a Harary triad — a which-wiring distinction, *intrinsically* discrete at every finite $D$ (cycle parity is binary, no limit to approach), gauge-irremovable, invariant under $\tau_{obs}$ and continuous amplitude variation. *Free to hold* (topological protection, no barrier leak) but not reversibly flippable: protection forbids a continuous CW↔CCW path, so any chirality change is forced through the balanced (sign-erased) state, paying $\ge\ln 2$ per protected sign. **Cost moves from maintenance to modification.** Reference class: topological quantum memory (Kitaev 2003).

Orthogonality is measurable: chit, $Q$, and the full FDR locus sweep continuously while the topological bit stays locked — a decoupling impossible in a two-level memory (where energetic and informational DoF are the same object). Forced-erasure floor counts the independent protected signs (cycle-space dimension of the frustrated subgraph) — a quasistatically saturated bound, not a quantisation. **Operational falsifier:** the framework fails if the protected sign cannot be held without a per-time maintenance cost scaling with held duration (an amplitude bit in disguise), or if the chirality flips along a continuous path below $\ln 2$. (Receipts §Two bits / topological-Landauer.)

**bit/chit correspondence** — the framework's natural thermo↔info bridge, the discrete↔continuous hinge: the chit is the continuous instance whose $D\to\infty$ Boolean endpoint is the bit.

| Axis | Thermodynamic | Informational |
|---|---|---|
| Per-event | $\mathrm{chit}=\ln(G_0/L)$ | $\mathrm{bit}=\ln 2$ |
| Per-rate | $\langle\sigma\rangle$ | $I_{\text{pred}}$ |
| Precision | TUR | channel capacity |
| Compression | heat-tax tower | rate-distortion tower |
| Coupling | $\langle\sigma\rangle\ge-\Delta I$ | (same bound, dual reading) |

Apparatus per row in §Thermo-info accounting (Character wing). The per-event row is solid; whether the dual *mapping itself* is substrate-independent stays expository, not framework content (§Open conjectures).

### Central commitment (the falsifier of record)
The stand on the sign-topological face, planted as falsifiable — *not* awaiting confirmation. The narrower **ignition** claim, distinct from and not dependent on the gated $k_{\text{frust}}$-primitive elevation (§Open items).

A **Harary triad** $\triangle_H$: a directed 3-cycle, non-reciprocal ($M_{ij}\ne M_{ji}$), Harary-unbalanced (odd number of negative edges; no node gauge balances it), chiral (sign-product fixes a circulation handedness no gauge removes). $N=3$ is the minimal frustrated cycle: a non-reciprocal two-mode current circulates but is gauge-removable (not protected), so **the triad is the minimal carrier of gauge-irremovable circulation**. Cycle affinity $\mathcal{A}=\oint_C v/D$ = Schnakenberg log-rate-ratio (nats), gauge-invariant; $\mathrm{spec}(M)$ carries a complex-conjugate pair $\Leftrightarrow\mathcal{A}\ne 0$.

> **Commitment** (onset necessity — *not* generativity, *not* determinism). Onset of topologically-protected NESS circulation ($\mathcal{A}\ne 0$, removable only by edge deletion) requires a Harary triad:
> $$\text{protected circulation}\;\Rightarrow\;\triangle_H\ \text{in the coupling graph.}$$

Claim is on ignition only — what it takes to spin a current up. No claim $\triangle_H$ generates the $c/s/r$ backbone ($\alpha_s,P_s$ stay independent); no exclusive post-onset traction. Scoping is exact: ignition-necessity, not generativity, not determinism.

**Falsified by** (real cross-substrate instance, not synthetic): one substrate sustaining protected circulation ($\mathcal{A}\ne 0$, removable only by rewiring) with **no** Harary triad in its coupling graph. **Status:** un-instanced on a real substrate (synthetic only: `library/banach_frustrated.py`); planted precisely because not yet met. Receipt: §Central commitment.

**Named prediction — biological homochirality (staked, un-instanced).** Homochirality is not a frozen accident but an *actively maintained* coherence whose single handedness is the gauge-irremovable chimeric sign of a Harary triad. Life sustains one chirality against racemization through dissipative proofreading (the holding); the framework predicts that maintenance network carries a protected circulating current ($\mathcal{A}\ne 0$, complex-conjugate Jacobian pair, broken detailed balance) whose sign — *which hand* — is removable only by rewiring. *Probe:* instrument the chiral proofreading/editing system; measure (i) steady-state cyclic fluxes among chiral states, (ii) Jacobian spectrum of the linearised maintenance dynamics. **Decisive test = drive-sweep:** titrate metabolic drive (ATP/GTP) toward zero — current *magnitude* must collapse toward racemic while *sign* stays invariant. A handedness flip means the sign was drive-set, not topology-protected, and the framework is invalid here. Three structurally-equivalent nulls each fatal: gauge-balanced network (no frustrated cycle), two-component bistable mechanism (no 3-cycle), detailed balance at steady state (no current). Framework specifies signature + kill conditions precisely, the subsystem approximately; does not derive molecular identity (substrate biochemistry imported, not generated). Receipt: §Homochirality.

**Boundary rules and terminal attractor.** At $\mathcal{M}_2\times\{s\}$ operators do not reduce to Boolean identities — edge shear and drive budget remain active: $\bot$ not a global annihilator, $\top$ not a global identity. $C(\top,s)$ tracks edge/budget; $C(\bot,s),S(\bot,s)$ pass through; $S(\top,s)\to s$ or competitive dropout; $K(\top,s)$ uses residual non-parallelism. Dynamical rules, not equations — operator-level shadow of the mentor pairing (§Composite catalogue). Under compression flow, $\mathcal{M}_2$ is the **terminal attractor**: repeated compression contracts every proposition toward $c$/$r$ geometrically; $\epsilon$ measures residual information mass outside $\mathcal{M}_2$ per step. $\mathcal{M}_2$ is the fixed-point set of the framework's own RG flow, the codomain restriction making $K$ unique, and the terminal object making the compression tower converge.

## Typed objects & the bridge
Three objects of distinct type on a coupling graph; the typing is load-bearing (each answers to a different layer of the deformation). Truth values are endpoints (maintained $\approx 1$, decayed $\approx 0$).

**Vertex regime** (single trail, stability axis $\lambda_A$):
- $c$ committed: $\lambda_A\ll-D$ — self-sustaining, $\approx 1$ at minimal work
- $s$ suspended: $|\lambda_A|\lesssim D$ — true-while-pumped; marginal, held against decay, gone if pump stops
- $r$ reset: $\lambda_A\gg D$ — decayed, $\approx 0$, no maintenance cost

Three-regime threshold = cooperativity pattern of driven open quantum systems (Sieberer–Buchhold–Diehl 2016) and laser threshold (Haken 1985). Forgetting is not a separate operation — an unreinforced trail shrinks below the noise floor and its cross-dissipations evaporate.

**Edge** (signed shear $\gamma_{AB}$): $\gamma<0$ cooperative · $\gamma\approx 0$ orthogonal · $\gamma>0$ conflicting (per-edge cost $\gamma_{AB}$ in $D$-units). **Subgraph** ($k_{\text{frust}}$): cycle of $c$-edges with obstructive shear product, admitting no resolving drive — topological invariant of the coupling graph (Mézard–Parisi–Virasoro 1987). Vertex substrate-neutrality and subgraph substrate-specificity are the same fact at two layers. One thermodynamic distinction survives scale-relativity: self-sustaining (closed-coupling) structure is energetically distinct from drive-pumped regardless of $\tau_{obs}$; the mentor pairing turns on this.

**The bridge.** At zero amplitude $\lambda_A\approx L-G_0$ (laser linearisation; Haken 1983), and regime conditions translate to Character coordinates:

| regime | $\lambda_A$ vs $D$ | $G_0$ vs $L$ | reading |
|---|---|---|---|
| $c$ | $\lambda_A\ll-D$ | $G_0-L\gg D$ | deeply above threshold; saturation-clamped |
| $s$ | $\lvert\lambda_A\rvert\lesssim D$ | $\lvert G_0-L\rvert\lesssim D$ | near threshold; Schawlow–Townes broadening + CK aging coexist |
| $r$ | $\lambda_A\gg D$ | $G_0-L\ll-D$ | sub-threshold; spontaneous emission only |

$G_0/L$ and $\lambda_A/D$ are different coordinates on one regime structure — the hinge: *two coordinates, one regime structure*. Substrate-conditional reading rules inherit across the bridge without modification.

## Operators
$\mathcal{M}=\{c,s,r\}$, $\mathcal{M}_2=\{c,r\}$. Each operator is a constructive protocol whose $D\to\infty$ limit is a Boolean connective; at finite drive a dynamical action on trail structure, with a continuous-traversal shadow.

| Op | Signature | Action | $D\to\infty$ | Continuous shadow |
|---|---|---|---|---|
| $C$ | $\mathcal{M}^2\to\mathcal{M}$ | try-merge: $d_{A\oplus B}=w_Ad_A+w_Bd_B$, evaluate $\lambda_{A\oplus B}$ | $\land$ | $C_{\text{Character}}$ |
| $S$ | $\mathcal{M}^2\to\mathcal{M}$ | hold both: $\lvert\lambda_A\rvert+\lvert\lambda_B\rvert+\max(0,\gamma_{AB})\le D$ | $\lor$ | — |
| $K$ | $\mathcal{M}^2\to\mathcal{M}_2$ | $\delta(A,B)=\hat d_A-\hat d_B$, $\lambda_{A\ominus B}=\lvert\gamma_{AB}\rvert-D/2$; $c$ if $\delta\ne 0\land D>2\lvert\gamma_{AB}\rvert$, else $r$ | $\oplus$ | — |
| $R$ | $\mathcal{M}\to\mathcal{M}$ | sever to bath: $W_R/\kappa\ge\ln 2\cdot H(A\mid\text{rest})$; recovers Landauer at $\kappa=k_BT\cdot\xi_{sub}$ | $\neg$ | $R_{\text{Character}}$ |

$C\in\Sigma$ (try-merge) is a distinct object from the compression operator $\mathcal{C}$ (§Compression) — different category (operator on trails vs. ledger tower); typographical distinction preserved throughout. $K$ is unique: codomain restricted to $\mathcal{M}_2$, quotient acts on its *inputs* (coordinate-free expression of where $s$ sits). Over $\mathbb{F}_2$, $K$ is the parity-check object distinguishing XOR-SAT from $k$-SAT (Mézard–Ricci-Tersenghi–Zecchina 2003).

**$C_{\text{Character}}$ (merge):** adiabatic deformation $\gamma_{AB}\approx 0\to\gamma_{AB}\ll 0$ while sustaining NESS, rate slow vs $L$. Forced non-adiabatically, chit$\to 0$, system enters $s$-strain, Harada–Sasa $\sigma$ spikes; if drive can't cover the transient, one/both modes drop sub-threshold. Info-geometric: merge succeeds iff a Fisher-information geodesic stays on the above-threshold manifold (Amari–Nagaoka 2000). Sampled at fixed $D$, recovers Theorem 9 in the sharp-threshold limit ($\Delta_C=1$ iff $\gamma_{AB}>0\land D<\gamma_{AB}$) — the Boolean step is the sharp limit of a continuous survivability function. **$R_{\text{Character}}$ (sever):** quench — choke $G_0$ (demand-load) or open to bath ($L\uparrow$, decay-load); edge dissolves natively ($\gamma_{AB}\rho_A\rho_B\to 0$ as $\rho_A\to 0$); discrete Landauer bound is the integrated quench cost.

## Scale-relativity
Vertex label depends on $\tau_{obs}$ (same trail reads $c$/$s$/$r$ at narrow/mid/wide window; substrate timescales fix where each dominates). Hierarchy itself substrate-fixed; only labels migrate. $\gamma$ scales with $\tau_{obs}$ (cross-correlation depends on integration window). $k_{\text{frust}}$ does **not** migrate — topological property of the graph, not the kernel; present or absent. The amplitude face moves under the camera; the sign-topological face does not.

## Composite catalogue (molecular layer)
Two propositions in specified regimes under a specified edge occupy a composite regime — two faces of one rule-set.

| Pair | Edge | Composite | Field-name |
|---|---|---|---|
| $c$–$c$ aligned | $\gamma<0$ | $c$ deepened | Hebbian; force chains |
| $c$–$c$ orthogonal | $\gamma\approx 0$ | $s$ | independent memory |
| $c$–$c$ opposed | $\gamma>0$ | $s$ if $D$ covers, else one→$r$ | competing hypotheses |
| $c$–$s$ | $\gamma<0$ | $s$ (mentor) | synaptic tagging; pilot-light |
| $s$–$s$ | $\gamma>0$ | $s$ or competitive dropout | Lotka–Volterra |
| $c$–$c$–$c$ cycle | obstructive product | $k_{\text{frust}}$ | gridlock; UNSAT |
| oscillatory–$c$ | limit cycle, $\lambda_B\ll 0$ | entrainment / quench | Kuramoto; circadian |

| Regime | $\gamma_{AB}$ | Phase relationship |
|---|---|---|
| $c$–$c$ aligned | $\ll 0$ | in-phase locked (Hebbian / force chain) |
| $c$–$s$ mentor | $<0$, asymmetric | driven entrainment, non-reciprocal, priority queue |
| $c$–$c$ orthogonal | $\approx 0$ | unlocked / phase drift |
| $c$–$c$ opposed (lock) | $>0$, $K>\Delta\omega$ | anti-phase locked |
| $c$–$c$ opposed (split) | $>0$, $K<\Delta\omega$ | competitive desync (pitchfork) |
| $k_{\text{frust}}$ | $N\ge 3$ obstructive | frustrated sync |

Per row, MPA supplies a unifying mapping (the field already has the phenomenon). Per table, the contribution is sharper: one vertex+edge rule-set generates phenomena with no shared microphysics across neuroscience, ecology, statistical mechanics, combustion, organisational dynamics. The cycle/$k_{\text{frust}}$ row sits at a different type (subgraph, not pair). The Character-wing Adoption catalogue inherits this per-row / per-table reading.

## Capacity
Classically consistent (frustration-free) graph, average degree $d_{avg}$, min cost $\gamma_{min}$: max sustainable subgraph $\Gamma^*$ has a static structural ceiling
$$|\Gamma^*|\le\sqrt{\frac{2D}{\alpha\,\gamma_{min}\,d_{avg}}}.$$
Sparse $\sim D$; dense $\sim\sqrt D$ — the Hopfield ceiling (Amit–Gutfreund–Sompolinsky 1985); sharp threshold under constraint pressure (random $k$-SAT; Mézard–Parisi–Zecchina 2002). Predicts (not postdicts) modular sparsification — organelles, cortical segregation, clonal selection are the $\sqrt D$ shadow. $k_{\text{frust}}$ marks where structure is unsustainable at any $D$; **Complexity Wall** = spectral analogue at the meta-ledger layer.

Character supplies the dynamic conjugate (same wall, dynamic side): $\sum_{i\in\Gamma^*}L_i\le G_{total}\,\eta(\Gamma^*)$, cross-saturation efficiency $\eta\in(0,1]$, $\eta\to 0$ at the $\sqrt D$ ceiling. Closure = Erlang's loss formula (Erlang 1917):
$$\eta(\Gamma^*)=1-B(c,\rho),\qquad B(c,\rho)=\frac{\rho^c/c!}{\sum_{k=0}^c\rho^k/k!},$$
$c=\lfloor|\Gamma^*|_{\text{crit}}\rfloor$, $\rho$ the offered load on the mode-slot pool. **Soft/hard split is a substrate-class fingerprint:** soft substrates cross over smoothly; hard-wall (surface code at logical-error onset, one error breaks the code) replace $B$ by $\mathbb{1}[|\Gamma^*|\ge c]$. Falsifier: behavioral/cognitive substrate showing sharp Hopfield-snapping instead of Erlang-B tails, or QEC-class showing soft Erlang-B instead of abrupt threshold (Receipts §5/§22). Violation forces sparsification (vertices→$r$) or a sub-threshold phase transition, regardless of local chit margin.

## FDR signatures
Coherences are path-dependent NESS; equilibrium FDR fails. Apparatus reads spontaneous $C(\tau)$ vs response $\chi(\tau)$ in the parametric plot $\chi(\tau)$ vs $C(0)-C(\tau)$; Harada–Sasa (2005): integrated FDR-violation $=\langle\sigma\rangle$ (steady-state entropy production — the true cost of holding without arresting).

| Regime | Chit | Invariant | Reading |
|---|---|---|---|
| $c$ | $\gg 0$ | $X_c=\lim_\tau\chi/(C(0)-C)=0$ | suppression / narrow horizontal locus |
| $s$ | $\to 0^+$ | $\alpha_s=$ slope of aging segment in $\chi$ vs $(C(0)-C)$ | Cugliandolo–Kurchan ratio |
| $s$ | $\to 0^+$ | $P_s=\lim_\tau C(\tau)/C(0)$ | plateau height |
| $r$ | $<0$ | $X_r=\lim_\tau\chi/(C(0)-C)=1$ | unit-slope FDR |
| $k_{\text{frust}}$ | non-stationary | $N_f=\int_T\min(0,\chi)\,d\tau\big/\int_T\lvert\chi\rvert\,d\tau$; drive-independent affinity; complex Jacobian spectrum | transient-negative fraction; spin-glass loop (§k_frust drain) |

$\alpha_s,P_s$ are the load-bearing cross-substrate observables; the rest are within-class structural identifiers. $X\gg 1$ excluded by dissipative dynamics (unstable amplifier, not a sustained representation).

**$s$-regime is two-step:** quasi-equilibrium ($X=1$) on short lags, FDR-violated aging ($X<1$, slope $\alpha_s$) on long lags — a short-lag $X=1$ alone does not place a substrate in $r$; the long-lag aging segment is the $c/s/r$ discriminator. (Driven-critical RFIM reads $X=0.118$ via self-overlap + staggered-field estimator — not collective magnetisation, which is soft-mode-dominated near criticality and gives unstable $X$. FALSIFICATION Finding 2 closed 2026-05-21.)

**Two conjugate FDR frames** (Receipts §gFDR/§16; promoted 2026-05-22). *External-probe:* (amplitude × external field) → violation factor $X$ ($\alpha_s,P_s$ aging observables); needs a probe. *Self-probe:* (current $J$ × intrinsic affinity $\mathcal{A}$, nats) → violation factor = TUR-tightness $T=\langle\sigma\rangle\,\mathrm{Var}(J)/(2\langle J\rangle^2)$, measurable core $\mathrm{SNR}_J=\langle J\rangle^2/\mathrm{Var}(J)\le\langle\sigma\rangle/2$ — dimensionless by construction, defined iff a current exists ($k_{\text{frust}}$-bearing). Harada–Sasa bridges them in principle ($\int$FDR-violation $=\langle\sigma\rangle=J\!\cdot\!\mathcal{A}$). Operational claim is the weaker one — *same regime verdict wherever both frames are computable* — confirmed on a real substrate (class-B laser: both flag NESS) and closed exactly on `driven_ring` ($\langle\sigma\rangle=J\!\cdot\!\mathcal{A}$). Frames are different functionals; their *disagreement* is the falsifier. Exact cross-frame magnitude identity is a refinement owed to the velocity-frame Harada–Sasa integral, not a gate (§Owed work).

**Surface-code identification** (load-bearing positive instance). Distance-3 rotated memory-Z syndrome streams (Kitaev 2003; Fowler et al. 2012) trace a clean $s$-aging *locus shape* at sub-threshold operation, placing QEC in the Cugliandolo–Kurchan universality class; the locus migrates toward unit slope as the physical-error rate crosses threshold. The $s\to r$ migration is the framework's primary cross-substrate test. ($X$-magnitude recovery is owed — read at locus-shape, not absolute $X$, until the inversion lands.) Frustration negative-FDR not present here, and the absence is structural: uncorrelated depolarising drives $s\to r$ (vertex migration), not toward closed frustrated loops on the syndrome graph — the frustration test tightens to a noise model that closes such a loop. **Falsifier (Receipts §4):** syndrome FDR shows unit slope sub-threshold (no CK signature), or shape persists unchanged across threshold (no migration). Scale-relativity second prediction on the same data: sweeping $\tau_{obs}$ at fixed substrate walks the locus $c\to s\to r$ while $k_{\text{frust}}$ does not migrate.

**Measurement caution** (FALSIFICATION). Do not infer $X$ from a single linear slope on an aging locus — it biases up (prescribed $X=0.2$ reads 0.47 single-slope, 0.26 segmented). The five-vector inversion ($q_{EA},\tau_\alpha,\beta_{\text{KWW}},\tau_\beta,X$) is owed (§Owed work); until then $X$-bearing verdicts read at the raw FDR-locus-slope layer, faithful to ~2% on prescribed-$X$ cells.

## Compression / heat-tax — one RG flow, two ledgers
The ledger tracks the substrate; who tracks the ledger? The meta-ledger tower converges only under the **Compression Axiom**: each ascent strictly contracts under the compression operator $\mathcal{C}$ (distinct from $C\in\Sigma$), $\epsilon=\|\mathcal{C}\|_{op}<1$. One RG fixed point, two coupled ledgers.

**Informational ledger** = Wilson–Kadanoff flow with Banach contraction (Wilson 1975; Kadanoff 1966; Cardy 1996): $c,r$ fixed points, $s$ metastable (→$c$ if reinforced, →$r$ if not), $\mathcal{M}_2$ terminal attractor, $k_{\text{frust}}$ invariant on substrates carrying it; edges follow endpoints, shear-positive edges with both endpoints→$r$ vanish; Boolean = degenerate limit (every level collapses to identity). Trail vectors = equivalence classes under the flow ($\mathcal{M}_2$ = cavity-method *frozen core*, $s$ = *free* region; Krzakala et al. 2007).

**Thermodynamic ledger** routes the heat: $L_{n+1}=L_{n+1}^{(0)}+\alpha_\sigma\langle\sigma_n\rangle+\alpha_\Sigma\langle\Sigma_n\rangle$ — $\alpha_\sigma\langle\sigma_n\rangle$ carries level-$n$ flow as ambient noise, $\alpha_\Sigma\langle\Sigma_n\rangle$ carries level-$n$ maintenance as active stress. Conductivity Landauer-pinned: $\alpha_\sigma(\epsilon)=\alpha_{\sigma,0}(1-\epsilon)$ — per-level Landauer heat vanishes as $\epsilon\to 1$ (nothing erased) while cumulative mass $\Phi_{\text{total}}=\Phi^{(0)}/(1-\epsilon)$ diverges. The Wall's thermodynamic content sits in cumulative mass, not per-level heat.

**One flow, two sides** (Receipts §6.5). $\mathcal{C}$ is not primitive: it is the heat-tax tower flow re-presented on the space of slow-manifold generators — the level-to-level map induced by Mori–Zwanzig projection $\Pi_{\text{slow}}$ of the universal two-mode kernel, $\epsilon$ the leading IR linear-stability eigenvalue, Landauer-pinned to the substrate's thermal conductivity. Banach contraction $\epsilon<1$ is *derived* (IR fixed-point stability), not an axiom; $\Pi_{\text{slow}}$ *is* the conjugating isometry $\phi$ of the Wilson–Kadanoff structural-equivalence statement. Each level carries its own $D_n=\Phi^*_n/\kappa_n$; contraction bounds $D_{n+1}$ vs $D_n$ — a compressed ledger tracking a richer substrate does so with proportionally less informational mass.

**Complexity Wall.** $\epsilon\ge 1$ (insufficient spectral gap/modularity): tower diverges — thermodynamic impossibility theorem on resource-bounded inference for maximally-entangled substrates, living in cumulative mass. Sustained level-$(n+1)$ coherence needs $\ln(G_{0,n+1}/L_{n+1})>0$; fraying at level $n$ inflates $L_{n+1}$ via three channels — heat-tax spike, active-stress spike, and $r_n$ drop in collective sync (lost cooperative gain-sharing). The three are registers of one queueing law: by Cobham–Kleinrock priority-queue mapping (Cobham 1954; Kleinrock 1976) they are faces of $W_{n+1}=W_0/[(1-u_n)(1-u_{n+1})]$, singularity at $u\to 1$ coincident with $\epsilon\to 1$ (and $u_n=\epsilon_n$ at rate-distortion-optimal encoding, P4). Channels 2,3 share $r$ in opposing directions — Toner–Tu (1995) gives active-stress correction $f(r)=Cr^2$; active-coupling sign $C$ sets the balance.

Operationally $\epsilon<1$ is sufficient for every theorem above; structurally $\mathcal{C}$'s identification with Wilson–Kadanoff block-averaging is a type-identity, proven in the Markovian / spectral-gap regime and extended to non-Markovian Caputo memory ($\beta_{\text{mem}}<1$) by fractional RG with the same construction. Cross-substrate transfer of $\alpha_s,P_s$ universality (§FDR signatures) is the strongest evidence the programme is well-posed.

## k_frust drain (the sign-topological face, full treatment)
**Definitional core** (Receipts §846 PROMOTED). The stationary state of a frustrated cycle is irreducibly a NESS — a topologically forced circulating current, broken detailed balance. The deterministic flow realises it in two sub-regimes by sign of the relaxation eigenvalue's real part — both are $k_{\text{frust}}$; **the complex spectrum (irreducible rotation), not fixed-point non-existence, is the invariant**:
- *Stable circulating focus* (Re$<0$): spirals into a NESS that still circulates ($J\ne 0$).
- *Repelling focus + attracting limit cycle* (Re$>0$).

**Affinity vs magnitude.** Drive-independence belongs to the cycle *affinity* $\mathcal{A}=\oint v/D=\ln(\prod_+k/\prod_-k)$ (intensive log-rate-ratio, forced nonzero regardless of $D$), not the current *magnitude* $J_{ss}$ (scales with absolute kinetic rates, flows with chit; R1: $J$ grew $1.3\times10^{-2}\to2.5\times10^{-1}$ as $G_0$ swept $0.9\to2.0$). Falsifier reads "$J$ becomes drive-noise-dependent OR resolves to detailed balance" — *not* "drive-dependent" (pump-dependence of magnitude is legal).

**Survived falsification ladder** (Receipts §846 R1/R2/R3):
- *R1 operating-point sweep:* $J$ sign-definite + drive-independent; scales only with wiring; $5.8\sigma$ above matched reciprocal control at chit$=0.010$.
- *R2 Wall round-trip:* scanning Wall corruption to 8× the destruction anchor, frustration never destroyed — strong chaos only flips chirality (reversed loop still frustrated).
- *R3 gradient/detailed-balance:* frustrated-loop Jacobian spectrum complex at all coupling; matched cooperative control reads real-spectrum.

**Predicted measurements on a new substrate** (falsifier surface): (1) coexistence Jacobian has complex eigenvalues at every coupling in the surviving range; (2) $J$ sign-definite, drive-noise-invariant, scales only with absolute kinetic rates; (3) after strong-chaos Wall round-trip chirality may flip but $|J|$ recovers — detailed-balance recovery (real spectrum) forbidden while wiring intact. **gFDR signature:** transient-negative $N_f$ in loop-level apparatus — but $N_f$ is a $\tau_{obs}$-conditional observer-shadow, weaker than the intrinsic $J$ meter; no kill-shot on $N_f$ alone.

## Asymptotic closure
Every framework-prediction observable takes values in an open interval whose boundaries are $0$, $1$, or $\infty$; none attains its boundary at any non-asymptotic operating point. Boundaries exist only as limits: $\mathcal{M}_2$ at $D\to\infty$; $\varepsilon\to 1$ at the Wall; chit$=0$ as critical limit; $X_c\to 0$ deep $c$; $X_r\to 1$ deep $r$ (and at equilibrium); $u_n\to 1$ at Cobham blocking; $\eta\to 0$ at the Hopfield ceiling; $\beta_{\text{mem}}\to 1$ at the Markovian limit. Categorical labels ($\top,\bot,k_{\text{frust}}$) exist only at the $\mathcal{M}_2$ boundary or as discrete derivatives of continuous parameters. The structural commitment that boundaries are asymptotic-only is what makes the framework continuous *across* observables, not merely within one. An *attained* endpoint has left the domain → surfaces as a **NaN falsification tripwire**, not a fillable value (a state variable is never clipped at $0$ — clipping manufactures excluded zeros). **Falsifier:** any observable shown to attain exactly $0$ or $1$ at a finite, non-degenerate operating point.

## Substrate-conditional reading rules
Primitives are substrate-invariant; *signs* and *natural preprocessing* of certain observables are not. Two rules inherit identically across both projections.
- **Markovian sign caveat (F.1):** stiff/Markovian substrates (overdamped Langevin with stiff wells, conditionally-independent syndrome streams) invert $\gamma$ signs while preserving magnitudes and FDR shapes (kernel-width artefact — stiff well → short $\tau_A$ → positive $\gamma_A$). Use $|\gamma|$ + FDR shape jointly, not signs. For $k_{\text{frust}}$-bearing content this is chirality-flipping (sign reverses); chit-axis content preserved.
- **Detection-event rule (F.2):** where readout violates the locality the trail integral requires (one physical error flips every future measurement of an adjacent stabiliser), use the substrate's canonical local preprocessing — for surface codes $e_i(t)=s_i(t)\oplus s_i(t-1)$ (bounded-local: an error at $t$ triggers exactly two events); trail by EMA against detection events.

New rules are earned by application work, not posited.

---

# STRUCTURAL WING (v9 projection — the discrete operator algebra and its finite-$D$ interior)

The spine treats the deformation as one object with two faces; this wing develops the discrete face at resolution. $\mathcal{M}_2$ is an exact algebra; the finite-$D$ interior is its deformation, where closure/associativity/distributivity hold up to the quantified defects below.

## Deformation calculus (the finite-$D$ interior)
The Boolean section is exact; the interior is quantified — but **not as one $1/D$ series.** It is a *matched* structure: Thms 6–7 are regular small-parameter ($1/D$) expansions in the bulk; Thm 9 is a **singular threshold crossover**, not an analytic $1/D$ series. Each is a candidate observable where $D$, $\gamma$, operator action are independently measurable:

| Theorem | Bound | Limit |
|---|---|---|
| 6 (associator) | $\lVert\alpha_C\rVert\lesssim(1/D)\sum\lvert\gamma\rvert$ | $\to 0$ |
| 7 (distributivity defect) | $\lVert\delta_{dist}\rVert\lesssim(1/D)[\max(0,\gamma_{YZ})-\max(0,\gamma_{XY},\gamma_{XZ})]^+$ | $\to 0$ |
| 9 (Boolean deviation) | $\Delta_C(A,B)=1$ iff $\gamma_{AB}>0\land D<\gamma_{AB}$ | sharp threshold |

Theorems 6,7 give associator and distributivity defect a $1/D$ falloff — each breaks only in proportion to pairwise shear and decays smoothly. Theorem 9 is the framework's most direct quantitative criterion: a **resource-induced instability** — two propositions classical logic would conjoin cannot be jointly maintained because the budget doesn't cover the shear ($C(A,B)\to r$ while $\sigma(A)\land\sigma(B)=1$). Threshold $D<\gamma_{AB}$ is the cavity-QED / laser cooperativity threshold; a substrate's $\gamma$ profile at operating $D$ determines exactly which pairs admit joint commitment. This is where the section docks the interior — boundary rules exact where the calculus is asymptotic. **Two regimes, not one series:** Thms 6/7 carry leading $O(1/D)$ operator bounds in the bulk (a regular deformation); Thm 9's sharp threshold is the $D\to\infty$ limit of a finite-width **crossover** — read in the Character wing as the $s$-aging locus (§FDR signatures), so its finite-$D$ content is a *crossover-scaling function* (scaling collapse: width exponent + profile class), an established singular-perturbation object, **not** an analytic $1/D$ coefficient series. (Leading bounds + defect definitions receipted as `recovered-from-chat`; the bulk series beyond leading order and the seam scaling-collapse are owed — §Owed work; working notes `docs/deformation_calculus_sharpening_notes.md`.)

## Extension axes
Each vertex regime is exhaustive only for current commitments — scalar trail, single kernel, reciprocal pairwise coupling, continuous time. Relaxing any one opens a region with its own candidate operator, none with a Boolean shadow:
- **Limit-cycle trail** → rhythm primitive (irreducibly temporal), closed-loop FDR; oscillatory–$c$ composite is its simplest pairing.
- **Hierarchical kernel** → multi-timescale holdings, fragile-here-stable-there, multi-scale aging FDR; parametrises the kernel-width axis and carries the coarse-graining flow itself.
- **Non-reciprocal coupling** → dominance/inhibition, no symmetric truth-table shadow, turbulent FDR (Fruchart–Hanai–Littlewood–Vitelli 2021).
- **Higher-order frustration** (hypergraph) → graph-dimension generalisation of $k_{\text{frust}}$; full glassy taxonomy with multi-plateau aging.
- **Finite-population discreteness** → flickering $c\leftrightarrow r$, native probabilistic logic.

Two further operators deferred without elaboration: **transfer operator** $T(A\to A')$ at $W_T/\kappa\ge\ln 2\cdot[H(A\mid A',\text{rest})-\mathcal{I}(A;A')]$ (irreducible cost minus salvage credit); **latent ledgers** (encoded structure at near-zero ongoing cost, decompression-on-demand).

## Falloff profile (three faces)
- **Longitudinal** (along $D$, fixed else): polynomial-in-$1/D$ (the Theorem 6–7 form) / critical-scaling / exponential-with-power-law-correction — distinguishable by FDR curves on a denser operating-point grid.
- **Lateral** (other commitments): is the Boolean point regular or singular? Smooth → extension-axis operators are perturbative ghosts; cusps/non-analytic boundaries → those operators inhabit phases unreachable from classical logic by smooth deformation.
- **Scale** ($\tau_{obs}$): walks a vertex $c\to s\to r$; $k_{\text{frust}}$ stays put.

Stake: Boolean is a codimension-$N$ singular point in the parameter landscape, $N$ = commitment axes whose relaxation produces non-perturbative structure (longitudinal = codim-1 slice). Mathematics on hand: bifurcation/catastrophe (Thom 1972; Arnold 1992), spin-glass landscape theory (Mézard–Parisi–Virasoro; Cugliandolo–Kurchan; Wolynes–Onuchic–Thirumalai), non-reciprocal active matter (Fruchart–Vitelli) — the most directly aligned formalism for operators with no Boolean shadow.

---

# CHARACTER WING (cdv1 projection — the continuous dynamical engine)

The structural wing develops the discrete face; this wing develops the continuous economics of *being* a coherence on the graph against a bath — what it costs to hold, the dynamics that carry a substrate through the $c/s/r$ migration. The amplitude coordinate is the chit, introduced on the spine and given its full treatment here.

## The chit unit
$$\mathrm{chit}=\ln(G_0/L).$$
The logarithm is forced: for forward rate $\sim G_0$, backward $\sim L$, $\ln(G_0/L)$ is the Crooks per-transition entropy production (Crooks 1999; Seifert 2012); threshold symmetry ($G_0=L\Rightarrow$ chit$=0$), additivity across gain stages, and $\ln 2$-alignment with Landauer all collapse to faces of one rate-ratio structure. The rate-ratio reading is the Markovian specialisation of a per-orbit one, $\mathrm{chit}_{\text{orbit}}=\oint v(\theta)/D(\theta)\,d\theta$ (continuous-orbit Schnakenberg affinity; Schnakenberg 1976; Qian 2001) — the two agree at $\beta_{\text{mem}}=1$, orbit form canonical for non-Markovian substrates.

In sustained NESS, saturated gain clamps to loss ($G_{\text{sat}}=L$); chit measures the *unsaturated* excess — headroom, not operating point. Threshold: chit$\gg 0\Rightarrow c$; chit$\to 0^+\Rightarrow s$; chit$<0\Rightarrow r$. chit$=0$ is a critical limit, not an attainable state (§Asymptotic closure); $s$ is a finite window around it whose width resolves on a substrate split — drive-axis substrates carry an irreducible thermodynamic floor ($kT/q$ of a diode, Schawlow–Townes broadening), damping-axis carry a measurement-limited width vanishing in the deterministic limit (RLC testbed reads exactly zero at $Q=0.5$).

## Fraying sequence
Load monotonically reduces the chit; the typical trajectory is one sequence:
> saturated holding (chit$\gg 0$, $c$, resilient) → visible strain (chit$\to 0^+$, $s$) → mode-hopping (chit$\approx 0$, $s$ multistability) → sub-threshold collapse (chit$<0$, $r$).

Mode-hopping is the laser-physics name for the multistable substructure producing the aging plateau in the CK-class FDR signature. That this is *typical* is a theorem: by Crooks $P(\sigma)/P(-\sigma)=e^\sigma$, an anomalous fraying-resistance trajectory is exponentially rare in $|\sigma|$.

## Universal two-mode kernel
The discrete composite catalogue is recovered as the fixed points of one continuous field equation:
$$\frac{\partial\rho_A}{\partial t}=(G_{0,A}-L_A)\rho_A-\gamma_{AB}\,\rho_A\rho_B+\mathcal{D}[\rho_A,\rho_B;\gamma_{AB}]$$
(symmetric for $\rho_B$; $\gamma_{AB}<0$ contributes positively, matching the structural sign convention). $\mathcal{D}$ admits three closures:
- *Lamb stationary* — multi-mode laser gain depletion (Lamb 1964; Haken 1983): $G_{0,A}^{\text{eff}}=G_{0,A}/(1+\sum_{j\ne A}\rho_j/\rho_{\text{sat}})$, cubic cross-saturation the leading expansion.
- *Dynamic bath inversion* — bath promoted to $B(t)\in[0,1]$, projected out by Mori–Zwanzig (Mori 1965; Zwanzig 1973): non-Markovian history integral; fast-bath limit recovers Lamb; $\gamma_B^{-1}$ = service time in the queueing mapping.
- *Caputo fractional memory* — Mittag-Leffler kernel $\Gamma_{AB}(\tau)=\Gamma_0\,E_{\beta_{\text{mem}}}(-(\tau/\tau_c)^{\beta_{\text{mem}}})$ (Caputo 1967; Podlubny 1999; Metzler–Klafter 2000), $\beta_{\text{mem}}=1$ exponential, $<1$ power-law (glassy).

**Three-register coincidence for the $s$-exponent** (substrate-class conditional, *not* a definitional identity). Under the **common-exponent condition** (substrate's slow-resource memory kernel and load-arrival process share one anomalous-diffusion exponent):
$$\alpha_s=\beta_{\text{mem}}=\text{anomalous heavy-traffic exponent.}$$
Composes Pottier (1985; non-Markovian FDR identifying Caputo $\beta_{\text{mem}}$ with the aging slope) with Norros (1994; fractional-Brownian heavy-traffic generalising $1/(1-\rho)$ to $1/(1-\rho)^{\beta_{\text{mem}}}$) — distinct substrate-side processes coinciding only under the shared exponent. **Falsifier** (reframed per FALSIFICATION Finding 3): the original mm1 falsifier ($\alpha_s=\tfrac12$ at $\rho\to 1$) was mis-specified — $\tfrac12$ is a reflected-BM Hurst exponent in the $C$-vs-lag plane, $\alpha_s$ the FDR slope in the $\chi$-vs-$C$ plane. Reframed: a Markovian, reversible heavy-traffic substrate reads raw FDR slope $\approx 1$ across $\rho\to 1$ (clean instance: equilibrium critical slowing, which must read $X=1$); a Markovian substrate showing aging $X<1$, or a non-Markovian one showing Markovian Kingman scaling, falsifies it.

## Relaxation-oscillation register (stability)
The bridge eigenvalue's real part sets the regime; its full complex structure governs perturbation recovery. Above threshold a single-mode coherence is 2D in local linearisation (field × slow-resource), complex-conjugate pair — the relaxation-oscillation (RO) regime. Exact forms (Lamb closure; mpa-legal, validated to machine precision against the class-B laser Jacobian; Receipts §13):
$$\gamma_{RO}=\tfrac{\gamma_s}{2}e^{\text{chit}},\quad\omega_{RO}=\sqrt{2L\gamma_s(e^{\text{chit}}-1)-\tfrac{\gamma_s^2}{4}e^{2\text{chit}}},\quad Q=\sqrt{\tfrac{2L(e^{\text{chit}}-1)}{\gamma_s}-\tfrac{e^{2\text{chit}}}{4}}\;e^{-\text{chit}},$$
$\gamma_s$ the substrate's slow-resource turnover rate. **$Q$ is the chit-conjugate** (chit reads *whether* threshold is cleared; $Q$ reads *how many cycles* the headroom buys), non-monotonic: $Q\to 0$ at both chit$\to 0^+$ and chit$\to\infty$, peaking at **chit$=\ln 2$** — underdamped only in a mid-chit band, overdamped at both ends. The class-B picture ($s$-threshold is critical *slowing*, deep-$c$ damps RO out), not "many cycles deep in $c$". **Active/passive probe = on/off resonance:** probes within $\gamma_{RO}$ of $\omega_{RO}$ are $Q$-amplified (active), off-resonance passive; active-probe channel capacity peaks at intermediate headroom, not deep in $c$. Codim-1 bifurcations: transcritical at chit$=0$ ($c\leftrightarrow r$), pitchfork at $\gamma_{AB}=\gamma_c$, Hopf at obstructive-$\gamma$ onset; codim-2 normal forms (Bogdanov–Takens, cusp, Bautin) Receipts §14. Per-regime attractors: $c$-deep stable focus; $c$-mid stable spiral at $\omega_{RO}$; $s$ centre manifold at threshold (algebraic settling = CK aging — $P_s$ = slow-manifold amplitude, $\alpha_s$ = slow-eigenvalue residual scaling against saturating gain); $r$ stable origin; $k_{\text{frust}}$ circulating focus / limit cycle.

**Open prediction** (mpa-legal fix, 2026-05-20): deep-$c$ phase-lock collapse. Deep in $c$, $Q\to 0$ restores direct lock ($K_{AB}\propto(1+4Q^2)^{-1/2}\to 1$); over-provisioned holdings may collapse multi-mode independent-memory capacity (locked modes cannot store orthogonal trails). Falsifier and named substrate owed (§Open items).

## Thermodynamic and informational accounting
Stochastic thermodynamics and information theory consolidate into one dual ledger; the chit's $\ln$ sits inside both. Borrowed derivations (TUR, Schnakenberg, channel capacity, rate-distortion, Sagawa–Ueda) in Receipts §16/§17.
- **Entropy production.** Crooks DFT $P(\sigma)/P(-\sigma)=e^\sigma$; integrated FDR-violation $=\langle\sigma\rangle$ (Harada–Sasa).
- **TUR.** $\mathrm{Var}(J)/\langle J\rangle^2\ge 2k_B/\langle\sigma\rangle$ (Barato–Seifert 2015; Horowitz–Gingrich 2020) — the first explicit precision–cost constraint. TUR-tightness $T=\langle\sigma\rangle\,\mathrm{Var}(J)/(2k_B\langle J\rangle^2)$ varies by substrate class (biological active matter $T\approx 1$; engineered queues $T\gg 1$). Falsifier: nominally same-class substrates with arbitrary $T$ (Receipts §16).
- **Schnakenberg affinity.** $\langle\sigma\rangle=\sum_C J_C\ln(\prod_+k/\prod_-k)$; for limit cycles $\sigma_{\text{frust}}=J_{ss}\oint v/D\,d\theta$. $k_{\text{frust}}$'s drive-independence lives at the affinity; magnitude $J_{ss}$ flows with chit (§k_frust drain).
- **Predictive information** $I_{\text{pred}}=I(\text{past};\text{future})$ (Bialek–Nemenman–Tishby 2001) — third coherence observable beside chit and $Q$; active-probe channel capacity $C\sim\gamma_{RO}\log_2(1+Q)$. Extended second law $\langle\sigma\rangle\ge-\Delta I$ (Sagawa–Ueda 2010) — bit-readout holdings sustain at lower chit by paying in mutual information.

**Optimal-encoding coincidence** (posit P5; an equality *at a limit*, not an identity). Still bound (Still–Sivak–Bell–Crooks 2012): $\langle\sigma\rangle-\langle\sigma\rangle_{\min}\ge\gamma_s\,\chi$, $\chi=C_\mu-I_{\text{pred}}$ (cryptic order; $C_\mu$ = $\varepsilon$-machine structural complexity; Crutchfield 1989; Shalizi–Crutchfield 2001), equality at the rate-distortion-optimal limit. The same $\chi$ surfaces as encoding overhead and dissipation excess: $\chi=\Delta_n=\langle\sigma\rangle_{\text{excess}}/\gamma_s$ — one quantity, three registers, only at that limit. Falsifier (Receipts §17/§20): a substrate whose $I_{\text{pred}}$ scaling deviates from its thermodynamic dual — *also* the per-substrate-class fingerprint falsifier. Whether the dual *mapping* is substrate-independent → §Open conjectures.

## Adoption catalogue
Ten cross-framework registers adopted into the Character projection (the 2026-05-10 cascade; provenance in [`translating FDR.md`](translating%20FDR.md)). Per row: borrowed register, one-phrase MPA mapping, the observable surviving substrate-stripping, its falsifier, the receipts entry. Per row MPA supplies a unifying mapping; per table, one regime+kernel rule-set generates these across fields with no shared microphysics.

| Register | MPA mapping | Load-bearing observable | Falsifier | Receipts |
|---|---|---|---|---|
| Damping / resonance | RO trichotomy = $c/s/r$ damping shadow | $\gamma_{RO},\omega_{RO},Q$ | mpa-legal landed | §13 |
| Attractor classification | regimes ↔ attractor types | per-regime attractor | — | §14 |
| Synchronization | $\gamma_{AB}$ sign → in/anti-phase lock; $K_{AB}\propto(1+4Q^2)^{-1/2}$ | two independent transitions (chit-onset, Kuramoto $K_c$); collective $r$; chimera | only uniform sync/incoherence accessible | §15 |
| Nonequilibrium thermo | holdings are trajectory-NESS | $\langle\sigma\rangle$, Schnakenberg affinity, TUR-tightness $T$ | same-class arbitrary $T$ | §16 |
| Information theory | thermo↔info dual ledger | $I_{\text{pred}}$, channel capacity, cryptic order $\chi$ | $I_{\text{pred}}$ scaling breaks the dual | §17 |
| Self-organized criticality | chit-zero = SOC attractor; Galton–Watson $\mu=e^{\text{chit}}$ | avalanche $\tau\approx 3/2$; branching $\to 1$ at $\epsilon=1$ | stable $\tau\ne 3/2$, or branching $\ne 1$ at $\epsilon=1$ | §18 |
| Dissipative structures | chit-zero crossing = Prigogine formation; chit = Haken order parameter | Turing wavelength | Turing three-condition failure | §9, §19 |
| Control theory | holding = plant+controller loop; internal-model principle | four-axis observable; $k_{\text{frust}}$ admits no gradient Lyapunov | habit-extinction Caputo $\beta_{\text{mem}}<1$, or $W$ off the P3 form | §17, §20 |
| Active matter | holdings = active-matter units | active-stress fingerprint; MIPS | high-Pe clustering at $\gamma_{AB}\ge 0$ without swim-pressure | §21 |
| Queueing | holdings are queues: chit$=-\ln\rho$; $c/s/r$ ↔ stable / heavy-traffic / unstable | heavy-traffic $=s$-aging; $\epsilon\leftrightarrow u$ | Markovian-reversible substrate showing aging $X<1$ | §5, §22 |

Four claims too heavy for a row:
- **Four-aspect Complexity Wall.** At $\epsilon=1$ four signatures coincide: thermodynamic (cumulative-mass divergence), dynamical (meta-ledger flow bifurcation), informational (compression rate→1), SOC-critical (branching→1), with $\beta_{\text{mem}}\approx 1-\epsilon$ (P1) the unifying parameter. Sub-optimal encoding splits the aspects: thermodynamic+SOC reach criticality first via $u\to 1$; informational ($\epsilon\to 1$) only for optimal-encoding substrates — **sub-optimal substrates die thermodynamically before informationally.**
- **Regime ontology.** $s$ is the *generic* attractor of feedback-coupled NESS, not the unstable middle of a triplet ($c$ over-provisioned, $r$ post-collapse) — explains the empirical over-representation of $s$.
- **Heavy-traffic $=s$-aging.** Kingman's $\langle Q\rangle\sim(1-\rho)^{-1}$ divergence is the $s$-aging signature in the queueing register; the FDR aging exponent and queue-tail exponent are one phenomenon — coincident for Markovian, divergent for non-Markovian (the divergence itself the substrate-class diagnostic).
- **Active-stress / MIPS fingerprint.** $\alpha_\Sigma/\alpha_\sigma\sim v_0^2\tau_R/D_{\text{trans}}$ (alignment-independent, MIPS-compatible, survives $r\to 0$); active-coupling sign $C$ (contractile $>0$ / extensile $<0$ / isotropic $\approx 0$) sets the §Heat-tax channel-2/3 balance via $f(r)=Cr^2$; MIPS gives clustering at $\gamma_{AB}\ge 0$ — a mechanism absent from the two-mode kernel.

## Five leading-order posits
Five primitives share one four-part shape: (1) simplest functional form placing a primitive at its critical/optimal limit; (2) substrate-conditional deviation; (3) falsifier in Receipts; (4) substrate-thermodynamic derivation as receipts-only residual. Universality fixes the form (exponents); substrates fix the amplitudes (deviations) — RG language. Each is testable; none derived from substrate thermodynamics; closing the derivation per substrate class is the canonical extension mode, not a defect.

| # | Posit | Carried by | Receipts | Predicted measurement |
|---|---|---|---|---|
| P1 | $\beta_{\text{mem}}\approx 1-\epsilon$ | §Adoption (Wall) | §9 | $\beta_{\text{mem}}(\epsilon)$ linear to leading order, both endpoints respected |
| P2 | $\mu=e^{\text{chit}}$ | §Adoption (SOC) | §18 | avalanche branching tracks $e^{\text{chit}}$; $\tau\approx 3/2$ at chit$=0$ |
| P3 | $w_i=\gamma_{\text{ref}}/\gamma_{s,i}$ | §Adoption (control) | §20 | substrate-native weights inverse-scale with $\gamma_{s,i}$ |
| P4 | $u_n=\epsilon_n$ | §Adoption (queueing) | §22 | at rate-distortion-optimal encoding, $u_n-\epsilon_n\to 0$ |
| P5 | $\chi=\Delta_n$ | §Thermo-info | §20 | $C_\mu-I_{\text{pred}}=u_n-\epsilon_n=\langle\sigma\rangle_{\text{excess}}/\gamma_s$ |

## Cross-register structure
The same primitives surface across registers; the relationships sort into three kinds, and the discipline is to state the *epistemic status* of each — the easy error is reading a coincidence-under-a-condition or equality-at-a-limit as an ontological identity. Posits thread through: each link that *is* or *follows from* a posit names it.

**Correspondences** (one quantity/structure in several registers, binding condition stated).
- *Parameter coincidences* (one scalar, several protocols, equal under a stated condition or at a limit — not by definition): the **$\beta_{\text{mem}}$ coincidence** (posit P1) — aging slope = Caputo exponent = anomalous heavy-traffic exponent under the common-exponent condition (Pottier∘Norros, falsified where the exponents differ), propagating through seven registers (memory tail, Green–Kubo $\tau_R$, swim-pressure fingerprint, Kelly product-form breakdown, Wall-coupling posit, variable-ratio extinction tail, traffic-to-frozen-topological via $\ell_c$); the **optimal-encoding coincidence** (posit P5 riding $u_n=\epsilon_n$) — cryptic order, encoding overhead, dissipation excess coincide *at the rate-distortion-optimal limit*, sub-optimal substrates split them (and split the four-aspect Wall).
- *Structural correspondences* (one structure realised as genuinely distinct objects; the framework maps the shared structure, not the realizations): **mentor-row dual face** — one non-reciprocal coupling as temporal limit cycle ($\omega_{\text{pq}}$) or spatial Turing pattern ($k_c$), substrate spatial structure selecting; **$k_{\text{frust}}$ topological correspondence** — one topological excision (no $P_{ss}$) with three co-implied consequences (dynamical: no fixed point; info-geometric: homotopy obstruction; thermodynamic: forced Schnakenberg current), equivalent abstractly, distinct measurement protocols; **plant–controller correspondence** — one closed loop read as active probe, SOC self-tuning, Haken slaving.
- *Universality coincidence:* **Galton–Watson dual register** (posit P2) — one mean-field class ($\tau=3/2$) at two framework limits, horizontal ($\mu\to 1$ at chit$=0$) and vertical (tower branching $\to 1$ at $\epsilon=1$), substrate-graph dimensionality fixing the empirical exponent.

**Relations** (forcings/couplings between distinct objects). **Wall-forces-NRT** (consequence of P4): Cobham wait diverges at $u_n\to 1^-$, forcing a generic Hopf at every ascent; $N\ge 3$ ascents complete the 3-torus for Newhouse–Ruelle–Takens chaos — meta-ledger chaos past the Wall is *forced*, not merely allowed (contingent on $r$-collapse not preceding, and the Cobham–Haken bridge conditions). **$r$-coupling of heat-tax channels 2,3**: share $r$ in opposing directions (channel 2 as $1+Cr^2$, channel 3 as $r$-drop sync degradation), active-coupling sign $C$ setting the balance.

**Decompositions** (irreducible independence — the opposite of a correspondence). **Three spatial mechanisms**: Turing reaction–diffusion, Kelly queueing-congestion, frozen-topological at $\beta_{\text{mem}}\to 0$ have distinct prerequisites and do not reduce to one another (a substrate may carry one, two, or all three at different scales). **Four-channel pattern selection**: $N\ge 3$ emergence routes through four independent tests — frustration, spectral sync (generalised master-stability, mild-heterogeneity scope), non-reciprocity, active-matter overlay — the operating system for $N\ge 3$ structure.

Two parameter trialities (optimal-encoding, $\beta_{\text{mem}}$) and two structural trialities ($k_{\text{frust}}$, plant–controller) share a "one thing, three readings" shape; the rhyme is presentational, not a further claim. The auto-tuning posit $w_i=\gamma_{\text{ref}}/\gamma_{s,i}$ (P3) has no coincidence partner.

---

# Open items

Predictions awaiting empirical contact, pipeline owed before some verdicts can be adjudicated, and architectural conjectures not yet framework content. (Structural-projection conjectures — the codim-$N$ Boolean-singularity question, the deferred transfer-operator and latent-ledger operators — live in the structural wing.)

## Live falsifiers
- **Surface-code $s\to r$ migration** as the gFDR cross-substrate test — primary positive instance (Receipts §4).
- **Habit-extinction** Caputo $\beta_{\text{mem}}<1$ on variable-ratio schedules (Receipts §20).
- **Avalanche $\tau\approx 3/2$** on feedback-coupled NESS with separable timescales — apparatus validated 2026-05-20 on critical Galton–Watson + RFIM (Receipts §18).
- **Meta-ledger branching ratio $=1$ at $\epsilon=1$** in any observable hierarchical NESS substrate (Receipts §18).
- **Strange-attractor / chaotic Character dynamics** on any substrate crossing $\epsilon\ge 1$ (Receipts §14).
- **MIPS clustering at $\gamma_{AB}\ge 0$** in high-Péclet substrates (Receipts §21).
- **Chimera-state instancing** under the spectral (SBN) test (Receipts §15).
- **TUR-tightness as a substrate-class universality** (Receipts §16).
- **$I_{\text{pred}}$ scaling** with chit, $Q$, internal-model richness across substrate classes — also the bit/chit dual-ledger falsifier if a substrate breaks the per-row correspondence (Receipts §17/§20).
- **Heavy-traffic exponent vs $\alpha_s$** on Markovian and non-Markovian substrates — reframed mm1 falsifier (Receipts §22).
- **Substrate-class hard-vs-soft capacity walls** (Receipts §5/§22).
- **Turing three-condition refinement** — non-reciprocity + autocatalysis + differential diffusion (Receipts §19).
- **Memory-exponent collapse near the Wall**, $\beta_{\text{mem}}\approx 1-\epsilon$ (Receipts §9).
- **Auto-tuning inverse-form** $w_i=\gamma_{\text{ref}}/\gamma_{s,i}$ on substrates requiring diagonal stability (Receipts §20).
- **Common-exponent condition** for the $s$-exponent coincidence — falsified where FDR and queue-tail exponents are measured to differ.
- **Cobham–Haken bridge conditions** — three substrate-side conditions, each with its own falsifier.
- **Deep-$c$ phase-lock collapse** / multi-mode memory-capacity loss (raised by the mpa-legal fix to non-monotonic $Q$); falsifier and named substrate owed.

## Owed work (pipeline)
No result traversing the conform/inversion pipeline is carried as valid evidence until these land — the trustworthy layer is pre-conform direct simulation against exact analytical forms (two-frame gFDR bricks, rotational-OU, class-B-laser Jacobian).
- **Five-vector inversion** ($q_{EA},\tau_\alpha,\beta_{\text{KWW}},\tau_\beta,X$): first-cut fitter (`conformer/compute/five_vector.py::fit_kww5`) recovers $X$ on `two_temp_ou` to ~1–2%; until landed + integrated, $X$-bearing verdicts read at the raw FDR-locus-slope layer.
- **Domain-of-validity gate** on the conform pipeline: pure oscillation reads as `s_critical` with no gating; awaits the five-vector fitter absorbing valid-aging residuals before a residual threshold can isolate out-of-domain cases.
- **Underdamped/oscillatory inversion**: conform clamps to deep-$r$ on class-B laser ringing; adjudicate alongside the domain gate.
- **Auditor layer never exercised on controls**: once inversion carries $X$, push a control cell through the auditor and check the regime story.
- **$\varepsilon$-machine stationarity-gap criterion**: substrate-thermodynamic derivation separating the trajectory-ensemble-local-stationarity reading from the time-varying-$\varepsilon$-machine reading.
- **Two-frame velocity-frame closure + real-substrate contract**: the two conjugate FDR frames rest on verdict-agreement; the exact cross-frame identity $V_{ext}=\langle\sigma\rangle=J\!\cdot\!\mathcal{A}$ is owed to the velocity-frame Harada–Sasa integral. Apparatus runs on a nonlinear topologically-forced limit cycle (`library/banach_active_ring.py`: both frames run, TUR $T\ge 1$, frustration-necessity control passes); a real §846-clearing instance needs author-collected active-lattice data (public deposits — Veenstra/Coulais/Bartolo — lack the perturbation-response protocol and carry friction-dominated $\mathrm{Var}(J)$). See FALSIFICATION §TWO-FRAME + memory `project_harary_triad_substrate_data`.
- **Deformation calculus — bulk series + seam scaling-collapse** (two owed objects, not one): (i) the bulk $1/D$ operator expansion beyond leading bounds (Thm 6, Thm 7 off-seam); (ii) the threshold/seam **crossover-scaling** (Thm 9) — width exponent $w(D)\sim D^\alpha$ + profile universality class, the honest replacement for "recover the $1/D$ series." Leading bounds + defect definitions receipted (`recovered-from-chat`). A normal-form sandbox (`mpa-central/library/deformation_crossover_collapse.py`) shows a clean within-closure scaling collapse but a *closure-fitted* exponent; a forced $\alpha$ needs the noise law derived from a substrate's FDR (not done). Working notes: `docs/deformation_calculus_sharpening_notes.md`.

## Open conjectures (research notes, not framework content)
- **$k_{\text{frust}}$ as a second primitive axis.** R1/R2/R3 survived on a synthetic 3-cycle; elevation to a numbered primitive is earned only by a real cross-substrate instance exercising (a) drive-independent NESS circulation, (b) chirality conservation under a chirality-preserving transformation, (c) the three triality registers measuring the same thing. Candidate class: active non-reciprocal metamaterials wired into Harary-frustrated loops (Veenstra/Coulais robotic rings, Bartolo active hydraulics) — gauge-irremovable circulation; bottleneck is data, not physics.
- **$k_{\text{frust}}$ topology-floor posit.** Functional form tying smallest-cycle-affinity floor to graph topology not yet committed.
- **$k_{\text{frust}}$ information-native characterisation.** Currently native to dynamical / differential-geometric registers; a substrate-independent information-native characterisation (candidate: topological mutual information surviving detailed-balance restoration) is owed.
- **Bilingual register as a structural-universality claim.** That the bit/chit dual *mapping* is itself substrate-independent needs a test independent of the per-row falsifier; until then it is expository organisation, not framework content.
- **Substrate-transformation classification** (chirality-preserving / chirality-flipping / axis-mixing). Two entries already in their homes (Markovian $\gamma$-sign inversion; strong-chaos Wall round-trip); three further candidates (time-reversal on non-conservative substrates; parity on active-matter with definite $C$ sign; mirror operations on intrinsically chiral substrates) are future work.
- **Two-faces boundary correspondence** (is face-independence only a *bulk* statement?). The amplitude and sign-topological faces are independent axes in the bulk; open conjecture: they are **corresponded at their boundaries** — each computable from the other there — which would *refine*, not break, the independence commitment (independent in the bulk, locked at the boundary). Candidate established home: bulk–boundary / index-theory, and for this driven-dissipative (non-Hermitian) setting **exceptional-point / non-Hermitian topology**. A candidate wall-crossing law already sits in §Central commitment ($\mathrm{spec}(M)$ complex pair $\Leftrightarrow\mathcal{A}\ne0$; boundary $\mathcal{A}=0$ = eigenvalue coalescence). Gated on index-grade criteria — exact pairing $\nu=F(\Phi)$; $\Delta\nu\ne0\Leftrightarrow\Phi$ singular; transversality/reconstruction — none yet met. Working notes `docs/deformation_calculus_sharpening_notes.md` §10.

---

# Appendix — Principles & method

Two preambles govern how the framework is built and tested; neither constrains the operator algebra or capacity claims (upstream of the protocol layer). Long-form: [Architectural Block-In](../architecture/MPA_Architectural_Block-In.md) §"Foundational principles (consolidated)".

**Architectural commitments (five).**
1. **Color-management discipline.** Three layers — substrate-native, canonical representation, realizer-output — with declared, named, versioned, swappable transforms; the canonical representation is substrate-neutral by construction.
2. **Observer-driven scale management.** $\tau_{obs}$ is the camera; the canonical representation is observer-relative; cross-scale composition is camera motion, not transform invocation. §Scale-relativity is the operational consequence.
3. **Demand-bounded sufficiency.** Commit to *enough* representation for the demand, not maximal substrate fidelity; past the declared envelope the framework is silent. MPA is not the bottleneck on substrate fidelity.
4. **Singular working-space path.** One canonical-representation shape per version; plurality lives in drivers, intent flags, and version succession — never at the working-space layer. *Peel*, not scrape.
5. **Thin-RFC discipline.** Exchange surfaces written at gross-underengineering resolution; the rigor lives here, the contract in the RFCs. *It was never brittle if it never broke.* (Governs the RFCs, not the framework docs.)

The five are coupled; they constrain the RFC sequence and driver/realizer architecture, not the operator algebra or capacity claims.

**Methodological imperatives (seven).**
- **Trajectory primacy.** NESS observables on bounded time-series of sustained holding, not static point measurements.
- **NESS-by-default.** Detailed-balance breaking is the baseline; equilibrium is the degenerate (zero-drive) special case.
- **mpa-legal.** Every dynamical quantity flows with the operating point unless physics says otherwise; an inert constant frozen where physics requires flow is illegal (the audit has caught two — Receipts §13 / §Topological-drain mpa-LEGAL audit).
- **Falsifier discipline.** Each claim states a predicted measurement on a named substrate (or class), kill condition formalised in receipts. Surface-code $s$-aging is the load-bearing positive instance; the rest await empirical contact.
- **Goalpost-optic.** Refinements during a falsification campaign must shrink the falsifiable surface, not enlarge it. Survival is the operative verdict.
- **Reading rules inherit across projections.** Substrate-conditional sign caveats apply identically to both readings (§Substrate-conditional reading rules).
- **API surface, not closed theory.** The five posits encode the framework's API; substrate-thermodynamic derivation of exact functional shapes is the canonical extension mode, not a defect.
