## Setting
Boolean = $D \to \infty$ limit, where $D = \Phi^*/\kappa$ (work supplied / dissipation scale). MPA is the finite-$D$ generalization. Maintaining a proposition costs work; cut the work, structure dissolves. Substrate classes are characterised by the $(\Phi^*, \kappa)$ envelopes their realizers can produce, intersected with the $D$ values the spec asks for.
**Primitives**: trail vector (kernel-weighted history while proposition active), drive $D$, observer kernel $\tau_{obs}$.

## Three typed objects
**Vertex regime** (single trail, stability axis $\lambda_A$):
- $c$ committed: $\lambda_A \ll -D$ — self-sustaining, ≈ 1
- $s$ suspended: $|\lambda_A| \lesssim D$ — true-while-pumped
- $r$ reset: $\lambda_A \gg D$ — decayed, ≈ 0

Three-regime threshold structure = cooperativity pattern of driven open quantum systems (Sieberer–Buchhold–Diehl) and laser threshold (Haken).

**Edge** (signed shear $\gamma_{AB}$):
- $\gamma<0$ cooperative · $\gamma\approx 0$ orthogonal · $\gamma>0$ conflicting (per-edge cost $\gamma_{AB}$ in $D$-units)

**Subgraph** ($k_{\text{frust}}$): cycle of $c$-edges with obstructive shear product. Topological invariant of the coupling graph (Mézard–Parisi–Virasoro). Not resolvable by $D$. Vertex-level substrate-neutrality and subgraph-level substrate-specificity are the same fact stated at two layers.

A thermodynamic distinction survives scale-relativity: self-sustaining structure (closed coupling) is energetically distinct from drive-pumped structure regardless of $\tau_{obs}$. The §3.5 mentor pairing turns on this distinction.

## Scale-relativity
Vertex label depends on $\tau_{obs}$ (same trail reads $c$/$s$/$r$ at narrow/mid/wide window). Hierarchy itself is substrate-fixed. $\gamma$ scales with $\tau_{obs}$. $k_{\text{frust}}$ is invariant.

## Operators
$\mathcal{M}=\{c,s,r\}$, $\mathcal{M}_2=\{c,r\}$.

| Op | Signature | Action | $D \to \infty$ limit |
|---|---|---|---|
| $C$ | $\mathcal{M}^2 \to \mathcal{M}$ | try to merge: $d_{A\oplus B}=w_A d_A + w_B d_B$, evaluate $\lambda_{A\oplus B}$ | $\land$ |
| $S$ | $\mathcal{M}^2 \to \mathcal{M}$ | hold both: $|\lambda_A|+|\lambda_B|+\max(0,\gamma_{AB})\le D$ | $\lor$ |
| $K$ | $\mathcal{M}^2 \to \mathcal{M}_2$ | $\delta(A,B)=\hat d_A - \hat d_B$, $\lambda_{A\ominus B}=|\gamma_{AB}|-D/2$; $c$ if $\delta\ne 0$ ∧ $D>2|\gamma_{AB}|$, else $r$ | $\oplus$ |
| $R$ | $\mathcal{M} \to \mathcal{M}$ | sever to bath: $W_R/\kappa \ge \ln 2 \cdot H(A\mid\text{rest})$; recovers Landauer when $\kappa = k_BT \cdot \xi_{sub}$ | $\neg$ |

Notation. C∈ΣC \in \SigmaC∈Σ is the try-merge operator. It is a distinct object from the compression operator C\mathcal{C}C introduced in §Compression Axiom — different category (operator on trails vs. operator on the ledger tower), different role. Typographical distinction (CCC vs C\mathcal{C}C) is preserved throughout this document.

$K$ is unique: codomain restricted to $\mathcal{M}_2$; quotient acts on its inputs. $C, S, R$ quotient acts on output. Asymmetric typing = coordinate-free expression of where the metastable $s$ sits in each signature. $K$ over $\mathbb{F}_2$ is the parity-check object that distinguishes XOR-SAT from $k$-SAT (Mézard–Ricci-Tersenghi–Zecchina).

## Boolean section ($\mathcal{M}_2$)
Three identifications of the same set:
1. Codomain of $K$
2. Fixed-point set of coarse-graining flow ($s$ metastable)
3. Section on which limit-equivalence quotient $q: \mathcal{M}(\infty) \to \mathbb{B}$ is bijective

Restriction of $\Sigma=\{C,S,K,R,\top,\bot\}$ to $\mathcal{M}_2 \cong (\mathbb{B},\land,\lor,\oplus,\neg)$. Closure at $\sigma$-shadow level (regime can stray to $s$ but shadow holds).

**Boundary rules** at $\mathcal{M}_2 \times \{s\}$: $\bot$ not global annihilator, $\top$ not global identity — shear and drive remain active. $C(\top,s)$ tracks edge/budget; $C(\bot,s), S(\bot,s)$ pass-through; $S(\top,s)$ → $s$ or competitive dropout; $K(\top,s)$ uses residual non-parallelism. Operator-level shadow of the §3.5 mentor pairing. (Full per-operator table: §3.6.)

**Terminal attractor.** Repeated compression contracts toward $\mathcal{M}_2$ geometrically; $\epsilon$ measures residual information mass outside $\mathcal{M}_2$ after each step.

## Composite catalogue (molecular layer)
| Pair | Edge | Composite | Field-name |
|---|---|---|---|
| $c$–$c$ aligned | $\gamma<0$ | $c$ deepened | Hebbian; force chains |
| $c$–$c$ orthogonal | $\gamma\approx 0$ | $s$ | independent memory |
| $c$–$c$ opposed | $\gamma>0$ | $s$ if $D$ covers, else one→$r$ | competing hypotheses |
| $c$–$s$ | $\gamma<0$ | $s$ (mentor) | synaptic tagging; pilot-light |
| $s$–$s$ | $\gamma>0$ | $s$ or competitive dropout | Lotka–Volterra |
| $c$–$c$–$c$ cycle | obstructive product | $k_{\text{frust}}$ | gridlock; UNSAT |
| oscillatory–$c$ | limit cycle, $\lambda_B \ll 0$ | entrainment / quench | Kuramoto; circadian |

Per row: MPA's contribution is modest — the field already has the phenomenon, the framework supplies unifying vocabulary. Per table: the contribution is sharper — the same vertex+edge rule set generates phenomena with no shared microphysics across neuroscience, ecology, statistical mechanics, combustion, organisational dynamics. Cycle row sits at a different type (subgraph, not pair) — molecular layer's natural carrier of $k_{\text{frust}}$.

## Capacity
On classically consistent (frustration-free) graph, sustainable subgraph $\Gamma^*$:
$$|\Gamma^*| \le \sqrt{\frac{2D}{\alpha\,\gamma_{min}\,d_{avg}}}$$
Sparse: $\sim D$. Dense: $\sim\sqrt{D}$ — the Hopfield ceiling (Amit–Gutfreund–Sompolinsky); sharp threshold at the wall (random $k$-SAT, Mézard–Parisi–Zecchina). Predicts modular sparsification of densely-coupled substrates. $k_{\text{frust}}$ marks where structure is unsustainable at any $D$. **Complexity Wall** = spectral analogue at the meta-ledger layer (§6).

## Fluctuation-dissipation signatures
Parametric plot $\chi(\tau)$ vs $C(0)-C(\tau)$:
- $r$ (vertex): unit slope (FDT)
- $c$ (vertex): $X \ll 1$, suppressed response, narrow horizontal locus
- $s$ (vertex): aging diagonal, plateaus at long times — Cugliandolo–Kurchan
- $k_{\text{frust}}$ (subgraph): transient **negative** response (loop-level, spin-glass response theory)

Signatures attach to objects of distinct type. $X \gg 1$ excluded by dissipative dynamics (unstable amplifier, not a sustained representation).

**Surface-code identification (§5, Figure 1).** Distance-3 rotated memory-Z syndrome streams trace a clean $s$-aging diagonal at sub-threshold operation — places the QEC substrate in the Cugliandolo–Kurchan universality class. Locus deforms toward threshold. The framework's most direct cross-substrate empirical content. Frustration negative-FDR not present in this measurement: uncorrelated depolarising drives $s \to r$ (vertex migration), not toward closed frustrated loops on the syndrome graph; test condition tightens to a noise model that closes such a loop.

**Scale-sweep prediction.** $\tau_{obs}$ sweep at fixed substrate walks the locus through $c \to s \to r$. $k_{\text{frust}}$ does not migrate (topological).

## Substrate-conditional reading rules (Appendix F)
- **Markovian sign caveat (F.1):** stiff/Markovian substrates (overdamped Langevin, syndrome streams) invert $\gamma$ signs (kernel-width artefact); use $|\gamma|$ + FDR shape jointly, not signs.
- **Detection events (F.2):** when readout violates the locality requirement of $\dot x$ (raw stabiliser flip propagates), use canonical local preprocessing — for surface codes, $e_i(t) = s_i(t) \oplus s_i(t-1)$ (bounded-local: an error at $t$ triggers exactly two events). Trail by EMA against detection events.

## Compression Axiom / meta-ledger flow
Ledger tracks substrate. Who tracks ledger? Tower converges iff each ascent contracts under the compression operator C\mathcal{C}C (distinct from C∈ΣC \in \SigmaC∈Σ, §Operators): ϵ=∥C∥op<1\epsilon = \|\mathcal{C}\|_{op} < 1ϵ=∥C∥op​<1.

Flow is RG-like (Wilson–Kadanoff + Banach):
- $c$, $r$ fixed points; $s$ metastable (→$c$ if reinforced, →$r$ if not)
- $\mathcal{M}_2$ = terminal attractor
- $k_{\text{frust}}$ invariant on substrates carrying it
- edges follow endpoints; shear-positive edges with both endpoints→$r$ vanish
- Boolean = degenerate limit (every level collapses to identity)

Trail vectors = equivalence classes under this flow. Substrate-neutrality at vertex = same flow class. Substrate-specificity at subgraph = topology of interaction graph. Quotient $q: \mathcal{M}(\infty) \to \mathbb{B}$ at the limit; $\mathcal{M}_2$ is the cavity-method *frozen core*, $s$ is the *free* region (Krzakala et al. 2007).

**Tower of dimensionless drives.** Each meta-ledger level carries its own $D_n = \Phi^*_n/\kappa_n$. The Compression Axiom acquires a dimensional statement: the contraction $\epsilon < 1$ on each ascent bounds $D_{n+1}$ relative to $D_n$. A compressed ledger that tracks a richer substrate must do so with proportionally less informational mass. Substrate classes at level $n$ characterised by $(\Phi^*_n, \kappa_n)$ envelopes intersected with the $D_n$ the architecture asks for. Spec-layer dimensional structure extends to the whole tower.

**Convergent Tower / Complexity Wall (Appendix G).** $\Phi_{total} = \Phi^{(0)}/(1-\epsilon)$ when $\epsilon<1$. When $\epsilon \ge 1$ (insufficient spectral gap or modularity), tower diverges: thermodynamic impossibility theorem on resource-bounded inference for maximally-entangled substrates. The flow has a downward extension too — within a level, constituent regimes can migrate while the cluster reads as committed at the level above; nested convergence at every level.

(Open: formal coarse-graining map at the rigour-level the RG literature requires; metric on trail-class space; per-regime universality invariants — flagged in Appendix A. The $s$-aging cross-substrate transfer is the strongest evidence to date that this programme is well-posed.)

## Falloff profile (three faces)
- **Longitudinal** (along $D$, fixed everything else): polynomial-in-$1/D$ / critical-scaling / exponential-with-power-law-correction
- **Lateral** (other commitments — scalar trail, single kernel, reciprocal coupling, continuous time): smooth or cusps?
- **Scale** ($\tau_{obs}$): kernel sweep walks $c\to s\to r$ on vertex; $k_{\text{frust}}$ doesn't migrate

Conjecture: Boolean is codimension-$N$ singular point in the parameter landscape, $N$ = relaxable commitments producing non-perturbative structure. Mathematics on hand: bifurcation/catastrophe (Thom–Arnold), spin-glass landscape theory (Mézard–Parisi–Virasoro, Cugliandolo–Kurchan, Wolynes–Onuchic), non-reciprocal active matter (Fruchart–Vitelli) — most directly aligned existing formalism for operators with no Boolean shadow.

## Extension axes (§8 candidates — exist only at $D < \infty$ + at least one commitment relaxed)
- **Limit-cycle trail** → rhythm primitive, oscillator-$c$ composites, closed-loop FDR
- **Hierarchical kernel** → multi-timescale, fragile-here-stable-there, multi-scale aging FDR (parametrises kernel-width axis; carries the coarse-graining flow itself)
- **Non-reciprocal coupling** → dominance/inhibition, no symmetric truth-table shadow, turbulent FDR (Fruchart–Vitelli formalism)
- **Higher-order frustration** (hypergraph) → multi-plateau aging, full glassy taxonomy (graph-dimension extension parallel to multi-timescale extension on kernel-width)
- **Finite-population discreteness** → flickering $c\leftrightarrow r$, native probabilistic logic

Each = candidate operator with no Boolean limit. Two further deferred: **transfer operator** $T(A \to A')$ with $W_T/\kappa \ge \ln 2 \cdot [H(A\mid A',\text{rest}) - \mathcal{I}(A;A')]$ (irreducible cost minus salvage credit); **latent ledgers** (encoded structure at near-zero ongoing cost, decompression-on-demand).

## Deformation calculus (finite-$D$ interior, Appendix J)
| Theorem | Bound | Limit |
|---|---|---|
| 6 (associator) | $\|\alpha_C\| \lesssim (1/D)\sum\|\gamma\|$ | $\to 0$ |
| 7 (distributivity defect) | $\|\delta_{dist}\| \lesssim (1/D)[\max(0,\gamma_{YZ})-\max(0,\gamma_{XY},\gamma_{XZ})]^+$ | $\to 0$ |
| 9 (Boolean deviation) | $\Delta_C(A,B)=1$ iff $\gamma_{AB}>0$ ∧ $D < \gamma_{AB}$ | sharp threshold |

Theorem 9 is the resource-induced instability: a substrate's $\gamma$ profile measured at operating $D$ determines exactly which propositional pairs admit joint commitment. Same cooperativity threshold structure as cavity QED / laser threshold. Interior is quantified; the §3.6 section is exact.
