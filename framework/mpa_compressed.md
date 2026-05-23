# MPA (unified operational source of truth)

**Status:** Live operational source of truth. One phenomenology, **two readings** joined at a
shared spine: a **STRUCTURAL** projection (discrete operator algebra, the finite-$D$ interior of
the Boolean ring) and a **CHARACTER** projection (the continuous driven-dissipative dynamics that
traverse that algebra). Both apply to any substrate (glass, QEC, brain, behavioral, future). The
spine is organised around the **Boolean→MPA deformation** (the asymmetric triality); the two
projection-specific bodies are the wings.

Every claim states a predicted measurement on a named substrate (or substrate class) and is
**mpa-legal** (dynamical quantities flow with the operating point; no inert constants where the
physics requires flow).

**Companions:**
- [`mpa_receipts.md`](mpa_receipts.md) — line-keyed justifications and falsifier formalisations
  behind the compressed claims. Unified in Phase 2 (2026-05-23) from the split sources
  [`v9_receipts.md`](v9_receipts.md) + [`cdv1_receipts.md`](cdv1_receipts.md), which stay live until
  Phase 3's gates confirm the merge. All `Receipts §…` pointers below resolve against the unified
  file (`§N` for register/character entries, section-name match for spine/structural entries; see
  its §Section-map).
- [`v9_unabridged.md`](v9_unabridged.md) / [`cdv1_unabridged.md`](cdv1_unabridged.md) — public-facing
  prose-and-prior-art versions. Rebuilt from compressed + receipts; allowed to lag. Do not lean on
  them for operational lookups.
- [`FALSIFICATION.md`](../FALSIFICATION.md) — the open attack front. Read this when asking *what
  are we trying to break?*

If this file disagrees with an unabridged, this file wins. If it disagrees with receipts, treat as
bug. The discrete and continuous readings are complementary, not competing; a disagreement between
them on a shared primitive is a bug.

> **Unification status (working draft).** Phases 1–2 landed (born 2026-05-22; receipts unified
> 2026-05-23; see [`unification_shape_and_handoff.md`](unification_shape_and_handoff.md)). This file +
> [`mpa_receipts.md`](mpa_receipts.md) are the unified pair; Phase 3 (interface + character-test gates)
> is next. Until the unification lands, the live split sources remain [`v9_compressed.md`](v9_compressed.md)
> and [`cdv1_compressed.md`](cdv1_compressed.md); this file does not yet replace them. Merge =
> union of claims, never lossy.

---

## Principles & method

Two preambles govern the framework: the five **architectural commitments** (structural, from v9)
and the seven **methodological imperatives** (Character-projection working discipline). Long-form
treatment of the architectural commitments: [Architectural Block-In](../architecture/MPA_Architectural_Block-In.md)
§"Foundational principles (consolidated)".

**Architectural commitments (five).**

1. **Color-management discipline.** Three layers — substrate-native, canonical representation,
   realizer-output — with declared, named, versioned, swappable transforms between them. The
   canonical representation is substrate-neutral by construction.
2. **Observer-driven scale management.** $\tau_{obs}$ is the camera. The canonical representation is
   observer-relative; cross-scale composition is camera motion, not transform invocation. No
   scale-class taxonomy baked into the framework. §Scale-relativity is the operational consequence.
3. **Demand-bounded sufficiency.** The framework commits to *enough* representation for the demand
   placed on it, not maximal faithfulness to substrate. Drivers declare a demand envelope; canonical
   representation is sized to it; past the envelope the framework is silent. MPA is not the
   bottleneck on substrate fidelity.
4. **Singular working-space path.** Within a version, exactly one canonical-representation shape.
   Plurality lives in drivers (substrate-conditional), realizer-interface intent flags
   (user-intent-conditional), and version succession (time-conditional) — never at the working-space
   layer. *Peel*, not scrape.
5. **Thin-RFC discipline.** Exchange surfaces written at gross-underengineering resolution by design;
   this file carries the rigor underneath, the RFCs carry the contract. *It was never brittle if it
   never broke.* Does not govern this file.

The five are coupled (Block-In §"Coupling between principles"). They constrain the RFC sequence and
the driver/realizer architecture; they do not constrain the operator algebra or capacity claims that
follow, which are upstream of the protocol layer.

**Methodological imperatives (seven).**

- **Trajectory primacy.** Bounded time-series of sustained holding, not static point measurements.
- **NESS-by-default.** Detailed-balance breaking is foundational baseline; equilibrium is the
  degenerate (zero-drive) special case.
- **mpa-legal.** Every dynamical quantity (rate, coupling, response, current) must *flow with the
  operating point* unless the physics explicitly says otherwise. An inert constant frozen where
  physics requires flow is illegal; the audit method has caught two such cases (Receipts §13 /
  §Topological-drain mpa-LEGAL audit, 2026-05-20).
- **Falsifier discipline.** Each claim states a predicted measurement on a named substrate (or
  substrate class), with a sharp falsifier formalised in Receipts. Surface-code $s$-aging is the
  load-bearing positive cross-substrate instance; the rest are predictions awaiting empirical contact.
- **Goalpost-optic.** Refinements during a falsification campaign must shrink the falsifiable
  surface, not enlarge it. Survival is the operative verdict.
- **Reading rules inherit across projections.** Substrate-conditional sign caveats (Markovian
  $\gamma$-sign inversion; detection-event preprocessing) apply identically (§Substrate-conditional
  reading rules).
- **API surface, not closed theory.** The five posits (§Five leading-order posits) encode the
  framework's API: each posit places a primitive at its critical limit via the simplest natural form;
  substrate-thermodynamic derivation of exact functional shapes is the canonical extension mode, not
  a defect.

---

# SPINE — the Boolean→MPA deformation

The spine is organised end-to-end around one structure: MPA *is* the finite-$D$ deformation of the
Boolean ($D\to\infty$) ring. Read topology (signed coupling graph, Harary balance) → asymptote
(open-interval boundaries, the $D\to\infty$ Boolean ceiling). The deformation has **two independent
faces** — an amplitude face and a sign-topological face — and everything in the spine hangs off one
or the other.

## Setting & primitives

Boolean = $D \to \infty$ limit, where $D = \Phi^*/\kappa$ (work supplied / dissipation scale). MPA is
the finite-$D$ generalization. Maintaining a proposition costs work; cut the work, structure dissolves.
Substrate classes are characterised by the $(\Phi^*, \kappa)$ envelopes their realizers can produce,
intersected with the $D$ values the spec asks for.

The same setting read in the continuous register: a **coherence** is a macroscopic pattern of
continuation maintained against natural dissolution; a **holding** is the continuous extraction of
entropy or application of work that maintains it. The Character projection specifies the
driven-dissipative dynamics that traverse the topology, edge shears, and operator algebra the
structural projection lays down.

**Primitives (unioned).**
- *Structural:* trail vector (kernel-weighted history while a proposition is active), drive $D$,
  observer kernel $\tau_{obs}$.
- *Substrate (Character):* gain rate $G_0$ (unsaturated gain rate $[\text{time}^{-1}]$,
  scales with $D$; laser-analogue small-signal gain — a rate, like $L$, so $G_0/L$ is dimensionless); decay rate $L$ (spontaneous relaxation rate to
  bath; cavity loss); signed edge structure $\gamma_{AB}$ on the mode graph.
- *Derived primitive (operational anchor):* $\text{chit} = \ln(G_0/L)$ — headroom above threshold. The
  framework's operational content keys to chit. Full treatment: §The chit unit (Character wing).
- *Topological invariant:* $k_{\text{frust}}$. Receipts §10 lists it as derived (heteroclinic-cycle
  consequence of the universal kernel + Harary structural balance). Its operational content — *the
  stationary state is irreducibly a NESS: a topologically-forced circulating current (broken detailed
  balance)* — survived the R1/R2/R3 falsification ladder (Receipts §846 PROMOTED; FALSIFICATION.md
  Finding 4). The operational content stands at the level of §Typed objects + §The deformation & its
  two faces + §k_frust drain; elevation to a numbered framework primitive awaits a real cross-substrate instance
  (§Open items).

## The deformation & its two faces

**$\mathcal{M}_2$ — the Boolean section.** Three identifications of the same set:
1. Codomain of $K$ (§Operators)
2. Fixed-point set of coarse-graining flow ($s$ metastable)
3. Section on which the limit-equivalence quotient $q: \mathcal{M}(\infty) \to \mathbb{B}$ is bijective

Restriction of $\Sigma=\{C,S,K,R,\top,\bot\}$ to $\mathcal{M}_2 \cong (\mathbb{B},\land,\lor,\oplus,\neg)$.
Closure at $\sigma$-shadow level (regime can stray to $s$ but the shadow holds).

**Reed-Muller / ANF presentation.** $\mathcal{M}_2$ is the $\{\oplus,\land,1\}$ ring ($\oplus = K$,
$\land = C$, $1 = \top$; $\neg = \oplus\,1$ via $K(\cdot,\top)$). MPA is its finite-$D$ deformation (the
$D\to\infty$ Boolean limit above): $R$'s irreversibility ($c\to r$, non-involutive) is the deformed
involution. The drive $G_0$ is the deformation coordinate (chit register $\ln(G_0/L)$), not the
ring's $1$.

**The two faces.** The deformation off Boolean carries **two independent coordinates**:
- **Amplitude face** (continuous): chit$/D$ — drives the $c\to s\to r$ migration; its cross-substrate
  observables are $\alpha_s, P_s$ (§FDR signatures). Full treatment of the chit coordinate: §The chit
  unit.
- **Sign-topological face** (topological): Harary balance of the signed coupling graph. Boolean is the
  **balanced/gaugeable** ring (every signed cycle of even negative parity, so gauge-equivalent to
  unsigned — real spectrum, no protected current). The deformation's sign-face is **Harary-imbalance**:
  the chimeric sign of a Harary triad $\triangle_H$ (below) *is* the deformation coordinate away from
  Harary-balance — the ANF-ring deformation made dynamical — with order parameter the cycle affinity
  $\mathcal{A}$ (defined in §Central commitment, below). Boolean (gaugeable) $\leftrightarrow$ MPA
  (deformed) is one structure read at two depths.

The two faces are coordinates of one deformation but **independent axes**: the sign-topological face is
topological, not amplitude — the source of $k_{\text{frust}}$'s $\tau_{obs}$-invariance
(§Scale-relativity) — and organising the spine around the deformation does **not** couple
$\alpha_s/P_s$ to $k_{\text{frust}}$.

**MPA adds no object.** It imports the ring (Reed-Muller/ANF), the balance (Harary), the cycle
(May–Leonard), and the affinity (Schnakenberg), and reads them under sustained dissipation.

**Two bits, one per deformation face** *(extends the bit/chit correspondence below; the topological bit
is the protected sign of §Central commitment).*

The Boolean deformation carries a distinct "bit" on each face:

- *Amplitude bit* — the $D\to\infty$ endpoint of the chit axis: a which-state (occupancy) distinction,
  **emergently** discrete (continuous until the limit). Erased by $R$ at the Landauer floor
  $W/\kappa \ge \ln 2$; must be *held* against thermal leak; flippable reversibly (no fundamental cost).
- *Topological bit* — the chimeric sign of a Harary triad on the sign-topological face: a which-wiring
  distinction, **intrinsically** discrete at every finite $D$ (cycle parity is binary — no limit to
  approach), gauge-irremovable, invariant under $\tau_{obs}$ and under continuous amplitude variation.
  *Free to hold* (topological protection, no barrier-leak), but not flippable reversibly: protection
  forbids a continuous CW↔CCW path, so any chirality change is forced through the balanced (sign-erased)
  state, paying $\ge \ln 2$ per protected sign. **The thermodynamic cost moves from maintenance to
  modification.**

**Signature (falsifier).** The two bits are orthogonal: chit, $Q$, and the full FDR locus can be swept
continuously while the topological bit stays locked — a decoupling impossible in a two-level memory,
where the informational and energetic degrees of freedom are the same object. The forced-erasure floor
counts the independent protected signs (= cycle-space dimension of the frustrated subgraph): a bound
saturated quasistatically, not a quantisation.

**Operator status.** $\Sigma=\{C,S,K,R,\top,\bot\}$ is complete on the amplitude face but carries no
operator on the sign-topological face — $R$ (sever) and the deferred transfer operator $T$ are
state-level; chirality surgery is graph-level. Reference class: topological quantum memory (Kitaev); MPA
imports the structure and reads it dissipatively, adding no mechanism. Receipt: §Two bits /
topological-Landauer (forced-erasure floor $\ge\ln2$ per cycle-space dimension; isolation protocol owed).

**Bit/chit correspondence** (the framework's natural thermo↔info bridge). The per-event row is the
discrete↔continuous hinge: chit is the continuous instance whose $D\to\infty$ Boolean endpoint is the
bit. Per-row measurements:

| Axis | Thermodynamic | Informational |
|---|---|---|
| Per-event | chit $= \ln(G_0/L)$ | bit $= \ln 2$ |
| Per-rate | $\langle\sigma\rangle$ | $I_{\text{pred}}$ |
| Precision | TUR | channel capacity |
| Compression | heat-tax tower | rate-distortion tower |
| Coupling | $\langle\sigma\rangle \ge -\Delta I$ | (same bound, dual reading) |

Apparatus (TUR / $\langle\sigma\rangle$ detail, $\varepsilon$-machine cryptic order, the P5
optimal-encoding derivation): §Thermodynamic and informational accounting (Character wing). Whether the
dual *mapping* itself is substrate-independent stays expository, not framework content (§Open items ›
Open conjectures).

### Central commitment (falsifier of record)

The stand the Character projection makes, planted as a falsifiable claim — *not* awaiting confirmation.
Distinct from the gated $k_{\text{frust}}$-primitive elevation (§Open items): that elevation stays
gated; this is the narrower **ignition** claim, made framework content deliberately so the projection
is falsifiable here.

**Harary triad** ($\triangle_H$): a directed 3-cycle, non-reciprocal ($M_{ij}\neq M_{ji}$),
Harary-unbalanced (odd number of negative edges; no node gauge $\varepsilon\in\{\pm1\}^N$ balances the
cycle), chiral (the sign-product fixes a circulation handedness no gauge removes). $N=3$ is the minimal
frustrated cycle: a non-reciprocal two-mode current circulates but is gauge-removable (not protected), so
the triad is the minimal carrier of gauge-irremovable circulation.

$\mathcal{A} = \oint_C v/D$ — Schnakenberg cycle affinity (nats), gauge-invariant; $\mathrm{spec}(M)$
carries a complex-conjugate pair $\Leftrightarrow \mathcal{A}\neq 0$.

**Commitment** (onset necessity — *not* generativity, *not* determinism). The onset of
topologically-protected NESS circulation ($\mathcal{A}\neq 0$, removable only by edge deletion) requires
a Harary triad:
$$\text{protected circulation}\;\Rightarrow\;\triangle_H\ \text{in the coupling graph.}$$
The claim is on ignition only — what it takes to spin a current up. No claim that $\triangle_H$ generates
the $c/s/r$ backbone ($\alpha_s, P_s$ remain independent); no claim of exclusive post-onset traction.

**Falsified by** (§846 bar — real cross-substrate instance, not synthetic): one substrate sustaining
topologically-protected circulation ($\mathcal{A}\neq 0$, removable only by rewiring) with **no** Harary
triad in its coupling graph. A single such instance collapses the commitment.

**Status:** un-instanced on a real substrate (synthetic instance only: `library/banach_frustrated.py`).
The stand is planted here precisely because it is not yet met. Receipt: §Central commitment.

**Named prediction — biological homochirality (staked, un-instanced).**

The framework predicts that biological homochirality is not a frozen historical accident but an
*actively maintained* coherence whose single handedness is the gauge-irremovable chimeric sign of a
Harary triad. Life sustains one chirality against spontaneous racemization — the natural dissolution —
through continuous dissipative proofreading, the holding; the framework predicts that this maintenance
network carries a topologically-protected circulating current (cycle affinity $\mathcal{A} = \oint v/D
\neq 0$, a complex-conjugate Jacobian pair, broken detailed balance) whose chimeric sign — *which hand*
— is removable only by rewiring (edge deletion), never by continuous deformation. The protected sign is
the maintained bit: chirality is read here as the primordial Boolean distinction, and its universality
across all extant life is the macroscopic signature of topological protection rather than bistable
inheritance. MPA adds no mechanism; it reads the maintenance dissipatively and stakes a structural
prediction.

*Probe placement (predicted measurement).* Instrument the network that maintains chirality against
racemization (the chiral proofreading/editing system). Measure (i) the steady-state cyclic fluxes among
chiral states and (ii) the Jacobian spectrum of the linearised maintenance dynamics. The prediction
requires a frustrated ≥3-node cycle — minimal core a non-reciprocal, odd-negative-signed 3-cycle —
sustaining a circulating current with a complex Jacobian pair and a gauge-irremovable sign.

*Decisive falsifier (drive-sweep).* Titrate the metabolic drive (ATP/GTP) toward zero. The current
*magnitude* must collapse toward the racemic ($r$) limit while the *sign* remains invariant. If the
handedness flips, the sign was drive-set rather than topology-protected, and the framework is invalid
here. Structurally equivalent nulls, each fatal: a gauge-balanced maintenance network (no frustrated
cycle), a two-component bistable mechanism (no 3-cycle), or detailed balance at steady state (no
current).

*Scope and status.* Un-instanced — pre-registered as a risky prediction, not a confirmed result. The
framework specifies the *signature* and the *kill conditions* precisely and the *subsystem*
approximately; it does not derive the molecular identity of the three nodes (substrate biochemistry is
imported, not generated), supplying a template to match rather than the molecules. This is a distinct,
bolder falsifier than the general onset-necessity commitment: it stakes the framework on a specific,
universal, ancient natural phenomenon. Receipt: §Homochirality.

### Boundary rules and terminal attractor

**Boundary rules** at $\mathcal{M}_2 \times \{s\}$: $\bot$ not global annihilator, $\top$ not global
identity — shear and drive remain active. $C(\top,s)$ tracks edge/budget; $C(\bot,s), S(\bot,s)$
pass-through; $S(\top,s)$ → $s$ or competitive dropout; $K(\top,s)$ uses residual non-parallelism.
Operator-level shadow of the mentor pairing (§Composite catalogue).

**Terminal attractor.** Repeated compression contracts toward $\mathcal{M}_2$ geometrically; $\epsilon$
measures residual information mass outside $\mathcal{M}_2$ after each step (§Compression / heat-tax).

## Typed objects & the bridge

**Vertex regime** (single trail, stability axis $\lambda_A$):
- $c$ committed: $\lambda_A \ll -D$ — self-sustaining, ≈ 1
- $s$ suspended: $|\lambda_A| \lesssim D$ — true-while-pumped
- $r$ reset: $\lambda_A \gg D$ — decayed, ≈ 0

Three-regime threshold structure = cooperativity pattern of driven open quantum systems
(Sieberer–Buchhold–Diehl) and laser threshold (Haken).

**Edge** (signed shear $\gamma_{AB}$):
- $\gamma<0$ cooperative · $\gamma\approx 0$ orthogonal · $\gamma>0$ conflicting (per-edge cost
  $\gamma_{AB}$ in $D$-units)

**Subgraph** ($k_{\text{frust}}$): cycle of $c$-edges with obstructive shear product. Topological
invariant of the coupling graph (Mézard–Parisi–Virasoro). Not resolvable by $D$. Vertex-level
substrate-neutrality and subgraph-level substrate-specificity are the same fact stated at two layers.

A thermodynamic distinction survives scale-relativity: self-sustaining structure (closed coupling) is
energetically distinct from drive-pumped structure regardless of $\tau_{obs}$. The mentor pairing
(§Composite catalogue) turns on this distinction.

**The bridge (the coordinate hinge).** At zero amplitude, the linearised field equation has eigenvalue
$\lambda_A \approx L - G_0$. The structural regime conditions translate into the Character coordinates:

| regime | $\lambda_A$ vs $D$ | $G_0$ vs $L$ | Reading |
|---|---|---|---|
| $c$ | $\lambda_A \ll -D$ | $G_0 - L \gg D$ | deeply above threshold, saturation-clamped |
| $s$ | $\lvert\lambda_A\rvert \lesssim D$ | $\lvert G_0 - L\rvert \lesssim D$ | near threshold; Schawlow–Townes broadening + CK aging coexist |
| $r$ | $\lambda_A \gg D$ | $G_0 - L \ll -D$ | sub-threshold; spontaneous emission only |

$G_0/L$ and $\lambda_A/D$ are different coordinates on the same regime structure. This is the hinge:
two coordinates, one regime structure.

## Operators

$\mathcal{M}=\{c,s,r\}$, $\mathcal{M}_2=\{c,r\}$. Discrete signatures and their continuous-traversal
shadows, side by side.

| Op | Signature | Action | $D \to \infty$ limit | Continuous-traversal shadow |
|---|---|---|---|---|
| $C$ | $\mathcal{M}^2 \to \mathcal{M}$ | try to merge: $d_{A\oplus B}=w_A d_A + w_B d_B$, evaluate $\lambda_{A\oplus B}$ | $\land$ | $C_{\text{Character}}$ (merge), below |
| $S$ | $\mathcal{M}^2 \to \mathcal{M}$ | hold both: $\lvert\lambda_A\rvert+\lvert\lambda_B\rvert+\max(0,\gamma_{AB})\le D$ | $\lor$ | — |
| $K$ | $\mathcal{M}^2 \to \mathcal{M}_2$ | $\delta(A,B)=\hat d_A - \hat d_B$, $\lambda_{A\ominus B}=\lvert\gamma_{AB}\rvert-D/2$; $c$ if $\delta\ne 0$ ∧ $D>2\lvert\gamma_{AB}\rvert$, else $r$ | $\oplus$ | — |
| $R$ | $\mathcal{M} \to \mathcal{M}$ | sever to bath: $W_R/\kappa \ge \ln 2 \cdot H(A\mid\text{rest})$; recovers Landauer when $\kappa = k_BT \cdot \xi_{sub}$ | $\neg$ | $R_{\text{Character}}$ (sever), below |

Notation. $C \in \Sigma$ is the try-merge operator. It is a distinct object from the compression
operator $\mathcal{C}$ introduced in §Compression / heat-tax — different category (operator on trails
vs. operator on the ledger tower), different role. Typographical distinction ($C$ vs $\mathcal{C}$) is
preserved throughout.

$K$ is unique: codomain restricted to $\mathcal{M}_2$; the quotient acts on its inputs. For $C, S, R$
the quotient acts on output. Asymmetric typing = coordinate-free expression of where the metastable
$s$ sits in each signature. $K$ over $\mathbb{F}_2$ is the parity-check object that distinguishes
XOR-SAT from $k$-SAT (Mézard–Ricci-Tersenghi–Zecchina).

**$C_{\text{Character}}$ (merge).** Adiabatic deformation from $\gamma_{AB} \approx 0$ to
$\gamma_{AB} \ll 0$ while sustaining NESS. Adiabaticity bound: deformation rate slow vs $L$. Failure
mode: forced non-adiabatic merge spikes $\sigma$, drops one or both modes sub-threshold.
Information-geometric reading: merge succeeds iff a Fisher-information geodesic stays on the
above-threshold manifold. Discrete shadow recovers Theorem 9 (§Deformation calculus) in the
sharp-threshold limit: $\Delta_C(A,B) = 1$ iff $\gamma_{AB} > 0 \land D < \gamma_{AB}$.

**$R_{\text{Character}}$ (sever).** Quench trajectory: choke $G_0$ (demand-load) or open mode to bath
($L\uparrow$, decay-load). Native edge dissolution — $\gamma_{AB}\rho_A\rho_B$ vanishes as
$\rho_A \to 0$. The discrete Landauer bound is the asymptotic limit.

## Scale-relativity

Vertex label depends on $\tau_{obs}$ (same trail reads $c$/$s$/$r$ at narrow/mid/wide window). Hierarchy
itself is substrate-fixed. $\gamma$ scales with $\tau_{obs}$. $k_{\text{frust}}$ is invariant —
topological, it does not migrate under the $\tau_{obs}$ sweep while $c/s/r$ does. (Authoritative
statement; cross-referenced from §The deformation & its two faces, §FDR signatures, §Falloff profile.)

## Composite catalogue (molecular layer)

Two faces of one rule-set: the discrete composite (vertex+edge) face, and the continuous
phase-relationship face (sweeping $\gamma_{AB}$).

*Discrete composite face.*

| Pair | Edge | Composite | Field-name |
|---|---|---|---|
| $c$–$c$ aligned | $\gamma<0$ | $c$ deepened | Hebbian; force chains |
| $c$–$c$ orthogonal | $\gamma\approx 0$ | $s$ | independent memory |
| $c$–$c$ opposed | $\gamma>0$ | $s$ if $D$ covers, else one→$r$ | competing hypotheses |
| $c$–$s$ | $\gamma<0$ | $s$ (mentor) | synaptic tagging; pilot-light |
| $s$–$s$ | $\gamma>0$ | $s$ or competitive dropout | Lotka–Volterra |
| $c$–$c$–$c$ cycle | obstructive product | $k_{\text{frust}}$ | gridlock; UNSAT |
| oscillatory–$c$ | limit cycle, $\lambda_B \ll 0$ | entrainment / quench | Kuramoto; circadian |

*Continuous phase-relationship face.*

| Regime | $\gamma_{AB}$ | Phase relationship |
|---|---|---|
| $c$–$c$ aligned | $\ll 0$ | in-phase locked (Hebbian / force chain) |
| $c$–$s$ mentor | $< 0$, asymmetric | driven entrainment, non-reciprocal, priority queue |
| $c$–$c$ orthogonal | $\approx 0$ | unlocked / phase drift |
| $c$–$c$ opposed (lock) | $> 0$, $K > \Delta\omega$ | anti-phase locked |
| $c$–$c$ opposed (split) | $> 0$, $K < \Delta\omega$ | competitive desync (pitchfork) |
| $k_{\text{frust}}$ | $N \ge 3$ obstructive | frustrated sync |

Per row: MPA's contribution is modest — the field already has the phenomenon, the framework supplies a
unifying mapping/vocabulary. Per table: the contribution is sharper — the same vertex+edge rule set
generates phenomena with no shared microphysics across neuroscience, ecology, statistical mechanics,
combustion, organisational dynamics. The cycle / $k_{\text{frust}}$ row sits at a different type
(subgraph, not pair) — the molecular layer's natural carrier of $k_{\text{frust}}$. (The §Adoption
catalogue inherits this per-row/per-table reading.)

## Capacity

On a classically consistent (frustration-free) graph, the sustainable subgraph $\Gamma^*$ has a static
structural ceiling:
$$|\Gamma^*| \le \sqrt{\frac{2D}{\alpha\,\gamma_{min}\,d_{avg}}}$$
Sparse: $\sim D$. Dense: $\sim\sqrt{D}$ — the Hopfield ceiling (Amit–Gutfreund–Sompolinsky); sharp
threshold at the wall (random $k$-SAT, Mézard–Parisi–Zecchina). Predicts modular sparsification of
densely-coupled substrates. $k_{\text{frust}}$ marks where structure is unsustainable at any $D$.
**Complexity Wall** = spectral analogue at the meta-ledger layer (§Compression / heat-tax).

**Dynamic conjugate.** Character supplies the dynamic conjugate to the static ceiling:
$$\sum_{i \in \Gamma^*} L_i \le G_{total}\,\eta(\Gamma^*)$$
with cross-saturation efficiency $\eta(\Gamma^*) \in (0,1]$, $\eta \to 0$ at the $\sqrt{D}$ Hopfield
ceiling. Violation forces sparsification or sub-threshold phase transition.

**Erlang-B closure.**
$$\eta(\Gamma^*) = 1 - B(c,\rho), \qquad B(c,\rho) = \frac{\rho^c/c!}{\sum_{k=0}^c \rho^k/k!}$$
with $c = \lfloor|\Gamma^*|_{\text{crit}}\rfloor$ and $\rho$ the effective offered load on the mode-slot
pool.

**Hard-vs-soft falsifier per substrate class** (Receipts §5/§22). Soft substrates:
$\eta = 1 - B(c,\rho)$, smooth crossover. Hard-wall substrates (surface code at logical-error onset):
$\eta = \mathbb{1}[|\Gamma^*| \ge c]$ — one error breaks the code. Falsifier: behavioral/cognitive
substrate exhibiting sharp Hopfield-snapping instead of Erlang-B tails; or QEC-class substrate showing
soft Erlang-B blocking instead of abrupt threshold.

## FDR signatures

Coherences are path-dependent NESS; equilibrium FDR fails. The Apparatus reads spontaneous fluctuations
$C(\tau)$ and response $\chi(\tau)$ in a parametric plot $\chi(\tau)$ vs $C(0)-C(\tau)$. Harada–Sasa:
integrated FDR-violation = steady-state entropy production rate $\langle\sigma\rangle$.

- $r$ (vertex): unit slope (FDR)
- $c$ (vertex): $X \ll 1$, suppressed response, narrow horizontal locus
- $s$ (vertex): aging diagonal, plateaus at long times — Cugliandolo–Kurchan
- $k_{\text{frust}}$ (subgraph): transient **negative** response (loop-level, spin-glass response theory)

Signatures attach to objects of distinct type. $X \gg 1$ excluded by dissipative dynamics (unstable
amplifier, not a sustained representation).

**Per-regime universality invariants.**

| Regime | Chit | Invariant | Reading |
|---|---|---|---|
| $c$ | $\gg 0$ | $X_c = \lim_\tau \chi(\tau)/(C(0)-C(\tau)) = 0$ | suppression / narrow horizontal locus |
| $s$ | $\to 0^+$ | $\alpha_s = $ slope of aging segment in $\chi$ vs $(C(0)-C)$ | CK ratio |
| $s$ | $\to 0^+$ | $P_s = \lim_\tau C(\tau)/C(0)$ | plateau height |
| $r$ | $< 0$ | $X_r = \lim_\tau \chi(\tau)/(C(0)-C(\tau)) = 1$ | unit-slope FDR |
| $k_{\text{frust}}$ | non-stationary | $N_f = \int_T \min(0,\chi)\,d\tau \big/ \int_T \lvert\chi\rvert\,d\tau$; drive-independent cycle affinity; complex Jacobian spectrum | transient-negative fraction; spin-glass loop signature (§k_frust drain) |

Universal within universality class; substrate-dependent corrections fall off with system size,
temperature, and finite-time effects. $\alpha_s$ and $P_s$ are the load-bearing cross-substrate
observables; the rest are within-class structural identifiers.

**$s$-regime FDR is two-step** (Receipts §gFDR staged candidate). Quasi-equilibrium ($X=1$) on short
lags; FDR-violated aging ($X<1$, slope $\alpha_s$) on long lags. A short-lag $X=1$ reading alone does
not place a substrate in $r$ — the long-lag aging segment is the c/s/r discriminator. (Survived
2026-05-20 on driven-critical RFIM: $X=0.118$ via self-overlap + staggered-field estimator. Not the
collective magnetisation, which is soft-mode-dominated near criticality and gives unstable $X$.) $X$ is
recoverable by the five-vector inversion (mpa-conform), domain-gated against out-of-family inputs —
Receipts §gFDR; FALSIFICATION FINDING 2 closed 2026-05-21.

**Two conjugate FDR frames** (Receipts §gFDR/§16 two-frame; promoted 2026-05-22). The FDR-violation
reads from two conjugate force–flux frames. *External-probe:* (amplitude × external field $h$) →
violation factor $X$ ($\alpha_s, P_s$ the aging observables); needs a probe. *Self-probe:* (current $J$
× intrinsic affinity $\mathcal{A}$, in nats) → violation factor is the TUR-tightness
$T=\langle\sigma\rangle\,\mathrm{Var}(J)/(2\langle J\rangle^2)$, measurable core
$\mathrm{SNR}_J=\langle J\rangle^2/\mathrm{Var}(J)\le\langle\sigma\rangle/2$; **dimensionless by
construction**, **defined iff a current exists** ($k_{\text{frust}}$-bearing). Harada–Sasa bridges them
in principle ($\int$FDR-violation $=\langle\sigma\rangle=J\!\cdot\!\mathcal{A}$). The operational claim is **same
regime verdict where both frames are computable** — confirmed on a real substrate (class-B laser: both
frames flag NESS; driven_ring: self-frame closes with exact $\langle\sigma\rangle=J\!\cdot\!\mathcal{A}$). Their
*disagreement* is the falsifier. The frames are *different functionals* (verdict-agreement, not
magnitude identity); the exact cross-frame $V_{ext}=\langle\sigma\rangle$ via velocity-frame Harada–Sasa
is a refinement, not a gate.

**Surface-code identification (load-bearing positive cross-substrate instance).** Distance-3 rotated
memory-Z syndrome streams trace a clean $s$-aging diagonal at sub-threshold operation — placing
surface-code QEC in the Cugliandolo–Kurchan universality class. The locus deforms toward threshold; the
$s \to r$ migration across the physical-error threshold is the framework's primary cross-substrate test
and its most direct cross-substrate empirical content. Frustration negative-FDR is not present in this
measurement: uncorrelated depolarising drives $s \to r$ (vertex migration), not toward closed frustrated
loops on the syndrome graph; the test condition tightens to a noise model that closes such a loop.
Falsifier (Receipts §4): (a) syndrome FDR shows unit slope sub-threshold (no CK signature); or (b) FDR
shape persists unchanged across threshold crossing.

**Scale-sweep prediction.** $\tau_{obs}$ sweep at fixed substrate walks the locus through
$c \to s \to r$; $k_{\text{frust}}$ does not (§Scale-relativity).

**Apparatus measurement notes** (from FALSIFICATION.md). Do not infer $X$ from a single linear FDR
slope on aging loci — it biases up (kww_oracle calibration: prescribed $X=0.2$ reads 0.47 via
single-slope vs 0.26 via segmented fit). The 5-vector inversion ($q_{EA}$, $\tau_\alpha$,
$\beta_{\text{KWW}}$, $\tau_\beta$, $X$) is owed; until landed, $X$-bearing verdicts read at the raw
FDR-locus-slope layer, where the grinder is faithful (validated to ~2% on two_temp_ou prescribed-$X$
cells).

## Compression / heat-tax — one RG flow, two ledgers

The ledger tracks the substrate. Who tracks the ledger? The meta-ledger tower converges iff each
ascent contracts under the compression operator $\mathcal{C}$ (distinct from $C \in \Sigma$,
§Operators): $\epsilon = \|\mathcal{C}\|_{op} < 1$. The flow carries **two ledgers** — an informational
ledger (the $\epsilon$-contraction of structure) and a thermodynamic ledger (the heat-tax routing the
exhaust) — coupled at the same RG fixed point.

**Informational ledger (RG-like flow; Wilson–Kadanoff + Banach):**
- $c$, $r$ fixed points; $s$ metastable (→$c$ if reinforced, →$r$ if not)
- $\mathcal{M}_2$ = terminal attractor
- $k_{\text{frust}}$ invariant on substrates carrying it
- edges follow endpoints; shear-positive edges with both endpoints→$r$ vanish
- Boolean = degenerate limit (every level collapses to identity)

Trail vectors = equivalence classes under this flow. Substrate-neutrality at vertex = same flow class.
Substrate-specificity at subgraph = topology of the interaction graph. The quotient
$q: \mathcal{M}(\infty) \to \mathbb{B}$ acts at the limit; $\mathcal{M}_2$ is the cavity-method *frozen
core*, $s$ is the *free* region (Krzakala et al. 2007).

**Thermodynamic ledger (heat-tax tower).** Character routes the thermodynamic exhaust:
$$L_{n+1} = L_{n+1}^{(0)} + \alpha_\sigma\langle\sigma_n\rangle + \alpha_\Sigma\langle\Sigma_n\rangle$$
Two effect axes propagate level-$n$ activity to level $n+1$:
- $\alpha_\sigma\langle\sigma_n\rangle$: heat from level-$n$ flow as ambient noise to level $n+1$.
- $\alpha_\Sigma\langle\Sigma_n\rangle$: active stress from level-$n$ maintenance as
  mechanical/informational/structural stress on level $n+1$.

Heat-tax coupling Landauer-pinned: $\alpha_\sigma(\epsilon) = \alpha_{\sigma,0}(1-\epsilon)$. Cumulative
tower tax to depth $N$ scales as $1-\epsilon^N$; at $\epsilon \to 1$ per-level Landauer heat vanishes (no
erasure) while cumulative informational mass $\Phi_{\text{total}} = \Phi^{(0)}/(1-\epsilon)$ diverges.

**Shared construction (one flow, established from two sides).** $\mathcal{C}$ is not primitive; it is the
abstract re-presentation of the heat-tax tower flow on the space of slow-manifold generators. The
level-to-level map $\mathcal{A}_n \mapsto \mathcal{A}_{n+1}$ is induced by Mori–Zwanzig projection
$\Pi_{\text{slow}}$ of the universal two-mode kernel onto the slow manifold, with heat-tax substitution
carrying level-$n$ entropy production into level-$(n+1)$ dissipation. $\epsilon$ is the leading IR
linear-stability eigenvalue of this map at $\mathcal{M}_2$, Landauer-pinned to the substrate's
thermal-conductivity coefficient $\alpha_{\sigma,0}$. Banach contraction $\epsilon < 1$ is therefore a
*derived* property (IR fixed-point linear stability), not an axiom on an abstract operator. The
continuous flow $T_\nu$ between integer levels exists by integration of the running-coupling
$\beta$-functions; no $\ln\mathcal{C}$ construction is required. $\Pi_{\text{slow}}$ *is* the
conjugating isometry $\phi$ of the Wilson–Kadanoff structural-equivalence statement (Wilson–Polchinski-style
functional RG on the space of generators). Receipts §6.5.

**Tower of dimensionless drives.** Each meta-ledger level carries its own $D_n = \Phi^*_n/\kappa_n$. The
Compression Axiom acquires a dimensional statement: the contraction $\epsilon < 1$ on each ascent bounds
$D_{n+1}$ relative to $D_n$. A compressed ledger that tracks a richer substrate must do so with
proportionally less informational mass. Substrate classes at level $n$ characterised by
$(\Phi^*_n, \kappa_n)$ envelopes intersected with the $D_n$ the architecture asks for. Spec-layer
dimensional structure extends to the whole tower.

**Convergent Tower / Complexity Wall.** $\Phi_{total} = \Phi^{(0)}/(1-\epsilon)$ when $\epsilon<1$. When
$\epsilon \ge 1$ (insufficient spectral gap or modularity), the tower diverges: a thermodynamic
impossibility theorem on resource-bounded inference for maximally-entangled substrates. The **Complexity
Wall** lives in the cumulative informational mass. The flow has a downward extension too — within a
level, constituent regimes can migrate while the cluster reads as committed at the level above; nested
convergence at every level.

**Three independent fraying channels.** Sustained level-$(n+1)$ coherence requires
$\ln(G_{0,n+1}/L_{n+1}) > 0$. Fraying at level $n$ inflates $L_{n+1}$ via:
1. $\alpha_\sigma\langle\sigma_n\rangle$ heat-tax spike (above).
2. $\alpha_\Sigma\langle\Sigma_n\rangle$ active-stress spike (§Adoption catalogue, active-stress).
3. $r_n$ drop in level-$n$ collective sync, raising $L_{n+1}^{(0)}$ via lost cooperative gain-sharing
   (§Adoption catalogue, synchronization).

By the Cobham/Kleinrock priority-queue mapping (§Adoption catalogue, heavy-traffic; Receipts §22), all
three are faces of Cobham wait-time inflation $W_{n+1}=W_0/[(1-u_n)(1-u_{n+1})]$ across tower-level
priority classes. The $u\to 1$ queueing singularity is coincident with $\epsilon\to 1$; for
rate-distortion-optimal encoding $u_n = \epsilon_n$ (posit P4). **Channels 2 and 3 share $r$ as driver
in opposing directions:** Toner–Tu gives active-stress correction $f(r) = Cr^2$, so the active-stress
channel scales as $1+Cr^2$ in level-$n$ sync while the cooperative-gain channel is triggered by
$r$-drop. Substrate active-coupling $C$ (contractile $>0$, extensile $<0$, isotropic $\approx 0$)
determines the balance.

**Trail-class metric.** Under the spectral-gap condition (isolated leading eigenvalue $\epsilon$ of
$\mathcal{C}$), trail equivalence is
$d_A \sim d_B \iff \lim_n \epsilon^{-n}\|\mathcal{C}^n(d_A-d_B)\| = 0$ — agreement at leading rate;
difference decays strictly faster than $\epsilon^n$. Metric on $\mathcal{T}/\!\sim$:
$$\rho\bigl([A],[B]\bigr) = \lim_{n\to\infty} \epsilon^{-n}\,\bigl\|\mathcal{C}^n(d_A-d_B)\bigr\|.$$
Amplitude of the leading-eigenmode component of $d_A - d_B$. Well-defined because faster-decaying modes
vanish under $\epsilon^{-n}$ rescaling. Spectral gap closes at the Complexity Wall; $\rho$ undefined
there by construction. Distinct from $\varepsilon_n = \|\mathcal{C}_n\|_{op}$ (operator-norm contraction
rate at level $n$) — $\rho$ measures distance between trail classes; $\varepsilon_n$ measures rate of
compression.

**RG closure.** Operationally: $\|\mathcal{C}\|_{op} = \epsilon < 1$ is sufficient for all theorems above
(Banach fixed-point, geometric convergence on $\{\mathcal{C}^n\}$, Convergent Tower, capacity bound, FDR
signatures). Structurally: $\mathcal{C}$'s identification with Wilson–Kadanoff block-averaging is
type-identity (the shared construction above). Both the meta-ledger flow and Wilson–Polchinski functional
RG are running-coupling flows on a space of generators with an IR-attracting fixed point. The three-step
proof strategy — (i) locality factorization, (ii) block-variable capacity preservation, (iii) conjugating
isometry $\phi$ — maps directly: spectral gap; heat-tax substitution preserving kernel form at the next
level; $\phi = \Pi_{\text{slow}}$. The Markovian / spectral-gap regime is proven scope; non-Markovian
Caputo $\beta_{\text{mem}} < 1$ uses fractional-RG generalization with the same construction.
Substrate-conditional functional form of the $\beta$-functions is the remaining classification residual;
per-substrate-class fingerprints read off from heat-tax coefficients.

(The $s$-aging cross-substrate transfer instances $\alpha_s$ and $P_s$ universality — §FDR signatures —
the strongest cross-substrate evidence to date that this programme is well-posed.)

## k_frust drain (the sign-topological face, full treatment)

**Definitional core (Receipts §846 PROMOTED, 2026-05-20).** The stationary state is irreducibly a NESS:
a topologically-forced circulating current (broken detailed balance). The deterministic flow realises
this in two sub-regimes by sign of the relaxation eigenvalue's real part — both are $k_{\text{frust}}$;
**the complex spectrum (irreducible rotation), not fixed-point non-existence, is the invariant**:

- *Stable circulating focus* (Re $<0$, complex spectrum): spirals into a NESS that still circulates
  ($J\ne 0$).
- *Repelling focus + attracting limit cycle* (Re $>0$): cooperative fixed point repels onto attracting
  orbit.

**Affinity vs magnitude** (Receipts §13/§16/§Topological-drain mpa-LEGAL audit, 2026-05-20).
Drive-independence is a property of the cycle **affinity**
$\mathcal{A} = \oint v/D = \ln(\prod_+ k / \prod_- k)$ (intensive log-rate-ratio, the thermodynamic force),
forced nonzero regardless of $D$. The current **magnitude** $J_{ss}$ scales with absolute kinetic rates
and therefore flows with chit (R1 measured: $J$ grew $1.3\times 10^{-2} \to 2.5\times 10^{-1}$ as $G_0$
swept 0.9 → 2.0). Falsifier reads: "$J$ becomes $D$-(noise)-dependent OR resolves to detailed balance" —
not "drive-dependent" (pump-dependence of magnitude is legal).

**Survived falsification ladder** (Receipts §846 R1/R2/R3):
- *R1 — operating-point sweep.* $J$ sign-definite + drive-independent across drive/headroom; scales
  only with wiring. At chit$=0.010$, $J$ reads 5.8σ above matched reciprocal control.
- *R2 — Wall round-trip, dual lens.* Discrete (sign-class) representation: scanning Wall corruption to
  8× the destruction anchor, frustration is never destroyed — strong chaos only flips chirality sign
  (a reversed loop is still frustrated).
- *R3 — gradient/detailed-balance test.* Frustrated-loop Jacobian spectrum is complex at all coupling;
  matched cooperative control reads real-spectrum.

**Predicted measurements on a new substrate** (the falsifier surface):
1. Frustrated-loop coexistence-Jacobian has complex eigenvalues at every coupling in the surviving
   operating range.
2. $J$ is sign-definite, $D$-noise-invariant, and scales (only) with absolute kinetic rates.
3. After strong-chaos Wall round-trip, chirality may flip but $|J|$ recovers; detailed-balance recovery
   (real spectrum) is forbidden while wiring is intact.

**gFDR signature.** Transient negative response $N_f$ in loop-level apparatus (noting that $N_f$ is a
$\tau_{obs}$-conditional observer-shadow, weaker than the intrinsic $J$ meter; do not run a kill-shot on
$N_f$ alone).

## Asymptotic closure

Every framework-prediction observable in MPA takes values in an open interval whose boundaries are 0, 1,
or $\infty$. No prediction attains 0, 1, or $\infty$ exactly at any non-asymptotic operating point.
Boundary values exist only as limits: $\mathcal{M}_2$ at $D \to \infty$; $\varepsilon \to 1$ at the
Complexity Wall; $\text{chit} = 0$ as critical limit; $X_c \to 0$ in deep $c$; $X_r \to 1$ in deep $r$
(and at thermodynamic equilibrium); $u_n \to 1$ at Cobham blocking; $\eta \to 0$ at the Hopfield
ceiling; $\beta_{\text{mem}} \to 1$ at the Markovian limit. Categorical labels ($\top$, $\bot$,
$k_{\text{frust}}$) exist only at the $\mathcal{M}_2$ boundary or as discrete derivatives of continuous
parameters with the boundary itself ill-defined ($k_{\text{frust}}$ singular at $\gamma_{AB} \to 0$).

**Domain reading (open interval, not endpoints).** Observables are continuous on an open interval;
Boolean/discrete logic is the degenerate limit at the endpoints ($0, 1, \infty$). chit is the per-event
instance — continuous $\ln(G_0/L)$ whose Boolean endpoint is the bit ($\ln 2$; §The deformation & its
two faces › Bit/chit correspondence). An *attained* endpoint has left the domain, so it surfaces as a **NaN
falsification tripwire**, not a fillable value. The structural commitment that boundary values are
asymptotic-only is what makes the framework continuous *across* observables, not just within any one.
(Scope statement; not the demoted claim that the bit↔chit *mapping* is substrate-independent — §Open
items › Open conjectures.)

**Falsifier.** A framework-prediction observable shown to attain exactly 0 or 1 at a finite,
non-degenerate operating point. The only conceivable instance is the exact equilibrium of cosmic heat
death — where equilibrium FDR predicts $X_r = 1$ exactly. Standard cosmology places heat death at
$t \to \infty$, never exactly reached, so the falsifier is itself asymptotic. MPA is therefore
falsifiable in principle and unfalsifiable in practice within cosmic time: the framework's
continuous-physics identity is preserved by the universe's own continuous-time structure. Falsification
routes through any observable whose predicted value can be shown to attain 0 or 1 (or $\infty$) at a
finite, non-degenerate operating point.

## Substrate-conditional reading rules

Inherited identically by both projections:

- **Markovian sign caveat (F.1):** stiff/Markovian substrates (overdamped Langevin, syndrome streams)
  invert $\gamma$ signs (kernel-width artefact); use $|\gamma|$ + FDR shape jointly, not signs. For
  $k_{\text{frust}}$-bearing content this is chirality-flipping (sign reverses); chit-axis content is
  preserved.
- **Detection events (F.2):** when readout violates the locality requirement of $\dot x$ (raw stabiliser
  flip propagates), use canonical local preprocessing — for surface codes,
  $e_i(t) = s_i(t) \oplus s_i(t-1)$ (bounded-local: an error at $t$ triggers exactly two events). Trail
  by EMA against detection events.

---

# STRUCTURAL WING (v9 projection — the discrete algebra interior)

## Deformation calculus (finite-$D$ interior)

| Theorem | Bound | Limit |
|---|---|---|
| 6 (associator) | $\|\alpha_C\| \lesssim (1/D)\sum\|\gamma\|$ | $\to 0$ |
| 7 (distributivity defect) | $\|\delta_{dist}\| \lesssim (1/D)[\max(0,\gamma_{YZ})-\max(0,\gamma_{XY},\gamma_{XZ})]^+$ | $\to 0$ |
| 9 (Boolean deviation) | $\Delta_C(A,B)=1$ iff $\gamma_{AB}>0$ ∧ $D < \gamma_{AB}$ | sharp threshold |

Theorem 9 is the resource-induced instability: a substrate's $\gamma$ profile measured at operating $D$
determines exactly which propositional pairs admit joint commitment. Same cooperativity threshold
structure as cavity QED / laser threshold. The interior is quantified; the boundary-rules treatment in
§The deformation & its two faces is exact.

## Extension axes (exist only at $D < \infty$ + at least one commitment relaxed)

- **Limit-cycle trail** → rhythm primitive, oscillator-$c$ composites, closed-loop FDR
- **Hierarchical kernel** → multi-timescale, fragile-here-stable-there, multi-scale aging FDR
  (parametrises kernel-width axis; carries the coarse-graining flow itself)
- **Non-reciprocal coupling** → dominance/inhibition, no symmetric truth-table shadow, turbulent FDR
  (Fruchart–Vitelli formalism)
- **Higher-order frustration** (hypergraph) → multi-plateau aging, full glassy taxonomy (graph-dimension
  extension parallel to the multi-timescale extension on kernel-width)
- **Finite-population discreteness** → flickering $c\leftrightarrow r$, native probabilistic logic

Each = candidate operator with no Boolean limit. Two further deferred: **transfer operator**
$T(A \to A')$ with $W_T/\kappa \ge \ln 2 \cdot [H(A\mid A',\text{rest}) - \mathcal{I}(A;A')]$ (irreducible
cost minus salvage credit); **latent ledgers** (encoded structure at near-zero ongoing cost,
decompression-on-demand).

## Falloff profile (three faces)

- **Longitudinal** (along $D$, fixed everything else): polynomial-in-$1/D$ / critical-scaling /
  exponential-with-power-law-correction
- **Lateral** (other commitments — scalar trail, single kernel, reciprocal coupling, continuous time):
  smooth or cusps?
- **Scale** ($\tau_{obs}$): kernel sweep walks $c\to s\to r$ on vertex; $k_{\text{frust}}$ doesn't (§Scale-relativity)

Conjecture: Boolean is a codimension-$N$ singular point in the parameter landscape, $N$ = relaxable
commitments producing non-perturbative structure. Mathematics on hand: bifurcation/catastrophe
(Thom–Arnold), spin-glass landscape theory (Mézard–Parisi–Virasoro, Cugliandolo–Kurchan,
Wolynes–Onuchic), non-reciprocal active matter (Fruchart–Vitelli) — the most directly aligned existing
formalism for operators with no Boolean shadow.

---

# CHARACTER WING (cdv1 projection — the continuous dynamical engine)

## The chit unit

$$\text{chit} = \ln(G_0/L)$$

The log form is required by stochastic thermodynamics: $\ln(k_+/k_-)$ is the Crooks rate-ratio entropy
production per stochastic transition.

**Markovian / orbit-affinity faces.** The rate-ratio reading is the Markovian specialisation of a
per-orbit reading: $\text{chit}_{\text{orbit}} = \oint v(\theta)/D(\theta)\,d\theta$ — the
continuous-orbit Schnakenberg affinity. The two faces agree at $\beta_{\text{mem}}=1$; for non-Markovian
(Caputo-memory) substrates the orbit-affinity face is canonical.

**Saturation.** In sustained NESS, saturated gain clamps to loss: $G_{sat} = L$. Chit measures the
*unsaturated* excess — headroom above threshold, not operating point.

**Threshold behaviour.** chit $\gg 0 \Rightarrow c$; chit $\to 0^+ \Rightarrow s$; chit $< 0 \Rightarrow r$.

**Limit-point status.** chit $= 0$ is a critical limit, not an attainable operating state. Substrates
approach it asymptotically; the $s$-regime is a finite window around the limit. Width: drive-axis
substrates carry an irreducible thermodynamic floor ($kT/q$); damping-axis vanishes in the deterministic
limit (F-003-rlc $Q=0.5$ zero). (Open-interval domain + NaN tripwire: §Asymptotic closure.)

## Fraying sequence

Load monotonically reduces the chit:

> Saturated holding (chit $\gg 0$, $c$, resilient) → visible strain (chit $\to 0^+$, $s$) → mode-hopping
> (chit $\approx 0$, $s$ multistability) → sub-threshold collapse (chit $< 0$, $r$).

Detailed fluctuation theorem $P(\sigma)/P(-\sigma) = e^\sigma$: anomalous fraying-resistance trajectories
are exponentially rare in $|\sigma|$. The fraying sequence is the *typical* trajectory.

## Universal two-mode kernel

$$\frac{\partial \rho_A}{\partial t} = (G_{0,A} - L_A)\rho_A - \gamma_{AB}\,\rho_A\rho_B + \mathcal{D}[\rho_A,\rho_B;\gamma_{AB}]$$

(symmetric for $\rho_B$; $\gamma_{AB}<0$ contributes positively to $\partial_t \rho_A$.) The
$\mathcal{D}$-kernel admits three closures.

*Lamb stationary closure.* $G_{0,A}^{\text{eff}} = G_{0,A}/(1+\sum_{j\ne A}\rho_j/\rho_{\text{sat}})$ —
multi-mode laser saturation.

*Dynamic bath inversion.* $B(t)\in[0,1]$ promoted to dynamical coordinate; Mori–Zwanzig projection-out
gives a non-Markovian history integral; fast-bath limit $\gamma_B\to\infty$ recovers Lamb. $\gamma_B^{-1}$
identifies as bath-server service time in the Cobham mapping (§Adoption catalogue, heavy-traffic; Receipts
§22).

*Caputo fractional memory.* For glassy / $s$-regime aging: Mittag-Leffler kernel
$\Gamma_{AB}(\tau) = \Gamma_0\,E_{\beta_{\text{mem}}}(-(\tau/\tau_c)^{\beta_{\text{mem}}})$,
$\beta_{\text{mem}}\in(0,1]$. $\beta_{\text{mem}}=1$ exponential; $\beta_{\text{mem}}<1$ power-law decay.

**Three-register identity for $s$-regime exponent** (substrate-class conditional). Under the
*common-exponent condition* — the substrate's slow-resource memory kernel and load-arrival process share
a single anomalous-diffusion exponent —
$$\alpha_s = \beta_{\text{mem}} = \text{anomalous heavy-traffic exponent}.$$
Composes Pottier (non-Markovian FDR identifying Caputo $\beta_{\text{mem}}$ with the aging slope) with
Norros (fractional-Brownian heavy-traffic generalises $1/(1-\rho)$ to $1/(1-\rho)^{\beta_{\text{mem}}}$).

**Falsifier (Receipts §22, reframed per FALSIFICATION.md Finding 3).** The original mm1_queue falsifier
($\alpha_s = \frac{1}{2}$ at $\rho \to 1$) is *mis-specified* — a category error mixing planes:
$\frac{1}{2}$ is the reflected-BM time-scaling (Hurst) exponent in the C-vs-lag plane; $\alpha_s$ is the
FDR effective-temperature slope in the $\chi$-vs-C plane. Two reframed routes: (i) measure C-decay-time
scaling vs $(1-\rho)$ in the C-vs-lag plane — where the $\frac{1}{2}$ lives — on Markovian vs
non-Markovian queues; predicted exponent matches the substrate's memory class. (ii) Extend the sampling
window to $\sim(1-\rho)^{-2}$ on M/M/1 (Markovian, reversible) and verify $X\approx 1$ (reversibility),
not aging $X<1$. The structural tension — "heavy-traffic M/M/1 maps to $s$-regime, but reversibility
forces $X=1$" — is the sharp form of this test; the cleaner instance is `ising_equilibrium` (equilibrium
critical slowing must read $X=1$). Predicted measurement: on Markovian–Poisson reversible substrates
exhibiting heavy traffic, raw FDR slope $\approx 1$ across $\rho \to 1$.

(The composite-catalogue phase-relationship table this kernel generates lives in §Composite catalogue.)

## Relaxation-oscillation register (stability)

The bridge eigenvalue's real part (§Typed objects & the bridge) sets the regime; the full complex structure governs perturbation
recovery. Above threshold a single-mode coherence is 2D in local linearisation (field × slow-resource)
with a complex-conjugate pair — the relaxation-oscillation (RO) regime. Exact forms (Lamb closure;
mpa-legal, validated to machine precision against the class-B laser Jacobian; Receipts §13):
$$\gamma_{RO} = \tfrac{\gamma_s}{2}e^{\text{chit}}, \quad \omega_{RO} = \sqrt{2L\gamma_s(e^{\text{chit}}-1) - \tfrac{\gamma_s^2}{4}e^{2\text{chit}}}, \quad Q = \sqrt{\tfrac{2L(e^{\text{chit}}-1)}{\gamma_s} - \tfrac{e^{2\text{chit}}}{4}}\;e^{-\text{chit}}.$$

**Non-monotonic $Q$ = cycles-of-headroom** (chit-conjugate: chit reads *whether* threshold is cleared,
$Q$ reads *how many cycles* of natural oscillation the headroom buys). $Q\to 0$ at both ends (chit
$\to 0^+$ and chit $\to \infty$), peaking at **chit $= \ln 2$**; underdamped only in a mid-chit band,
overdamped at both ends — the class-B picture ($s$-threshold is critical *slowing*, deep-$c$ damps RO
out), not "many cycles deep in $c$."

**Per-regime attractors.** $c$-deep stable focus; $c$-mid stable spiral at $\omega_{RO}$; $s$ centre
manifold at threshold (algebraic settling = CK aging — $P_s$ = slow-manifold amplitude, $\alpha_s$ =
slow-eigenvalue residual scaling against saturating gain; the isolating $\Pi_{\text{slow}}$ is the
meta-ledger level-projection read at within-level scale); $r$ stable origin; $k_{\text{frust}}$
circulating focus / limit cycle. Codim-1 bifurcations: transcritical at chit $=0$ ($c\leftrightarrow r$),
pitchfork at $\gamma_{AB}=\gamma_c$, Hopf at obstructive-$\gamma$ onset; codim-2 normal forms and the
Wall-forces-NRT delay-Hopf chain in Receipts §14.

**Active/passive probe = on/off resonance.** Probes within $\gamma_{RO}$ of $\omega_{RO}$ are
$Q$-amplified (active); off-resonance probes are passive baseline; boundary linewidth $\gamma_{RO}$.
Active-probe channel bandwidth $B\sim\gamma_{RO}\propto e^{\text{chit}}$ and S/N $\sim Q$ (non-monotonic)
— channel capacity peaks at intermediate headroom, not deep in $c$.

**Open prediction** (mpa-legal fix, 2026-05-20): deep-$c$ phase-lock collapse. Deep in $c$, $Q\to 0$
restores direct lock ($K_{AB}\propto(1+4Q^2)^{-1/2}\to 1$); over-provisioned holdings may collapse
multi-mode independent-memory capacity (locked modes cannot store orthogonal trails). Falsifier and named
substrate owed (§Open items).

## Thermodynamic and informational accounting

Stochastic thermodynamics and information theory consolidate into one dual ledger; the borrowed
derivations (TUR, Schnakenberg, channel capacity, rate-distortion, Sagawa–Ueda) are in Receipts §16/§17.

- **Entropy production.** Detailed fluctuation theorem $P(\sigma)/P(-\sigma) = e^\sigma$ (Crooks);
  integrated FDR-violation $=\langle\sigma\rangle$ (Harada–Sasa, §FDR signatures).
- **TUR-tightness fingerprint.** $T = \langle\sigma\rangle\,\text{Var}(J)/(2k_B\langle J\rangle^2)$
  varies by substrate class (biological active matter $T\approx 1$; engineered queues $T\gg 1$).
  Falsifier (Receipts §16): nominally same-class substrates with arbitrary $T$.
- **Schnakenberg affinity.** $\langle\sigma\rangle = \sum_C J_C\ln(\prod_+k/\prod_-k)$; for limit cycles
  $\sigma_{\text{frust}} = J_{ss}\oint v/D\,d\theta$. $k_{\text{frust}}$'s drive-independence lives at the
  affinity $\oint v/D$; magnitude $J_{ss}$ flows with chit (§k_frust drain).
- **Predictive information** $I_{\text{pred}} = I(\text{past};\text{future})$ — third coherence
  observable alongside chit and $Q$. Extended second law $\langle\sigma\rangle \ge -\Delta I$
  (Sagawa–Ueda).

**Bit/chit dual ledger.** The per-event bit↔chit identity and the dual-ledger table are elevated to the
spine (§The deformation & its two faces › Bit/chit correspondence) — they are the discrete↔continuous
bridge, not wing apparatus. The apparatus stays here: the entropy-production, TUR-tightness,
Schnakenberg, and predictive-information bullets above *are* the per-row thermodynamic↔informational
measurements; the optimal-encoding identity below is the coupling row's derivation.

**Optimal-encoding identity** (posit P5). $\langle\sigma\rangle - \langle\sigma\rangle_{\min} \ge
\gamma_s\,\chi$, with $\chi = C_\mu - I_{\text{pred}}$ (cryptic order; $C_\mu$ = $\varepsilon$-machine
structural complexity), equality at the rate-distortion-optimal limit. **Optimal-encoding Rosetta:**
$\chi = \Delta_n = \langle\sigma\rangle_{\text{excess}}/\gamma_s$ — one quantity, three registers
(information / queueing / thermodynamic). Falsifier (Receipts §17/§20): a substrate where $I_{\text{pred}}$
scaling (with chit, $Q$, internal-model richness) deviates from its thermodynamic dual — *also* the
per-substrate-class fingerprint falsifier (one falsifier, two readings). Whether the dual *mapping* is
itself substrate-independent → §Open items › Open conjectures.

## Adoption catalogue

Ten cross-framework registers were adopted into the Character projection (the 2026-05-10 cascade;
methodology and per-register provenance in [`translating FDR.md`](translating%20FDR.md)). Each row gives
the borrowed register, MPA's one-phrase mapping, the load-bearing observable that survives
substrate-stripping, its falsifier, and the receipts entry holding the apparatus. As in §Composite
catalogue, per row MPA's contribution is a unifying mapping; per table it is that one regime+kernel
rule-set generates these phenomena across fields with no shared microphysics. Claims too heavy for a row
are promoted below; the five posits are tabled in §Five leading-order posits.

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

**Four-aspect Complexity Wall** (promoted). At $\epsilon=1$ four critical signatures coincide:
*thermodynamic* (cumulative-mass series diverges), *dynamical* (meta-ledger flow bifurcation — §RO
register Wall-forces-NRT), *informational* (compression rate → 1), *SOC-critical* (fraying branching
ratio → 1). $\beta_{\text{mem}}\approx 1-\epsilon$ (P1) is the unifying parameter behind the four faces
(Receipts §9). For sub-optimal encoding the aspects split: thermodynamic + SOC reach criticality first
via $u\to 1$; the informational aspect ($\epsilon\to 1$) only for optimal-encoding substrates —
**sub-optimal substrates die thermodynamically before informationally.**

**Regime ontology** (promoted). The $s$-regime is the *generic* attractor of feedback-coupled NESS, not
the unstable middle of a triplet: $c$ = over-provisioned (chit pulled deep above threshold), $s$ =
self-organised operating point, $r$ = post-collapse. Explains the empirical over-representation of $s$.

**Heavy-traffic = $s$-aging** (promoted). Kingman's $\langle Q\rangle\sim(1-\rho)^{-1}$ divergence is the
§FDR-signatures $s$-aging signature in the queueing register: the FDR aging exponent $\alpha_s$ and the
queueing-tail exponent are one critical phenomenon — coincident for Markovian substrates, divergent for
non-Markovian (the divergence pattern is the substrate-class diagnostic; three-register identity
$\alpha_s=\beta_{\text{mem}}=$ anomalous heavy-traffic exponent under the common-exponent condition,
§Universal two-mode kernel). Cobham priority-wait $\propto[(1-u_n)(1-u_{n+1})]^{-1}$ diverges at
$u\to 1^-$ coincident with the §Compression/heat-tax singularity at $\epsilon\to 1^-$; Cobham / Jackson /
Kelly $\ell_c$ / Erlang-B closures and the three Cobham–Haken bridge conditions (each a
substrate-conditional falsifier) in Receipts §5/§22.

**Active-stress / MIPS fingerprints** (promoted). Hydrodynamic substrate-class fingerprint
$\alpha_\Sigma/\alpha_\sigma\sim v_0^2\tau_R/D_{\text{trans}}$ (alignment-independent, MIPS-compatible,
survives $r\to 0$); active-coupling sign $C$ (contractile $>0$ / extensile $<0$ / isotropic $\approx 0$)
sets the §Compression/heat-tax channel-2/3 balance via $f(r)=Cr^2$. MIPS gives clustering at
$\gamma_{AB}\ge 0$ — a mechanism absent from the §Universal two-mode kernel. Toner–Tu / Green–Kubo
$\tau_R$ / giant-number-fluctuation / non-reciprocal-Jacobian apparatus in Receipts §21.

## Five leading-order posits

Five framework primitives share an identical four-part shape: (1) simplest functional form placing a
primitive at its critical / optimal limit; (2) substrate-conditional deviation from that form; (3)
falsifier formalised in Receipts; (4) substrate-thermodynamic derivation as a receipts-only residual.

| # | Posit | Section | Receipts | Predicted measurement |
|---|---|---|---|---|
| P1 | $\beta_{\text{mem}} \approx 1-\epsilon$ | §Adoption catalogue (Wall) | §9 | Substrate's $\beta_{\text{mem}}(\epsilon)$ relation linear to leading order with both endpoints respected |
| P2 | $\mu = e^{\text{chit}}$ | §Adoption catalogue (SOC) | §18 | Avalanche branching ratio tracks $e^{\text{chit}}$; $\tau\approx 3/2$ at chit $=0$ |
| P3 | $w_i = \gamma_{\text{ref}}/\gamma_{s,i}$ | §Adoption catalogue (control) | §20 | Substrate-native weights inverse-scale with $\gamma_{s,i}$ |
| P4 | $u_n = \epsilon_n$ | §Adoption catalogue (queueing) | §22 | At rate-distortion-optimal encoding, $u_n - \epsilon_n \to 0$ |
| P5 | $\chi = \Delta_n$ | §Thermodynamic and informational accounting | §20 | $C_\mu - I_{\text{pred}} = u_n - \epsilon_n = \langle\sigma\rangle_{\text{excess}}/\gamma_s$ |

Universality fixes that *there is* a critical-limit form (the exponents); substrates fix the amplitudes
(deviations from the form). RG language. Each posit is testable; none is derived from substrate
thermodynamics.

---

## Open items

Predictions awaiting empirical contact (live falsifiers) and pieces of pipeline owed before some
verdicts can be adjudicated (owed work). Architectural conjectures and meta-organisational claims that
are not yet framework content are listed at the bottom. (Structural-projection open conjectures — the
codimension-$N$ Boolean-singularity question, the deferred transfer-operator and latent-ledger operators
— live in their homes in the Structural wing: §Falloff profile, §Extension axes.)

### Live falsifiers (named falsifier substrate + predicted measurement)

- Surface-code $s \to r$ migration as gFDR cross-substrate test (Receipts §4; primary instance).
- Habit-extinction Caputo $\beta_{\text{mem}}<1$ on variable-ratio schedules (Receipts §20).
- Avalanche $\tau \approx 3/2$ on feedback-coupled NESS with separable timescales (Receipts §18).
  Apparatus validated 2026-05-20 on critical Galton–Watson + RFIM.
- Meta-ledger branching ratio = 1 at $\epsilon = 1$ in any observable hierarchical NESS substrate
  (Receipts §18).
- Strange-attractor / chaotic Character dynamics on any substrate crossing $\epsilon \ge 1$ (Receipts §14).
- MIPS clustering at $\gamma_{AB} \ge 0$ in high-Péclet substrates (Receipts §21).
- Chimera-state substrate instancing under SBN spectral test (Receipts §15).
- TUR-tightness as substrate-class universality (Receipts §16).
- $I_{\text{pred}}$ scaling with chit, $Q$, internal-model richness across substrate classes — *also the
  falsifier for the bit/chit dual ledger if a substrate breaks the per-row correspondence* (Receipts
  §17/§20).
- Heavy-traffic exponent vs $\alpha_s$ on Markovian and non-Markovian substrates — the reframed mm1
  falsifier per FALSIFICATION.md Finding 3 (Receipts §22).
- Substrate-class hard-vs-soft capacity walls (Receipts §5/§22).
- Turing-class three-condition refinement (non-reciprocity + autocatalysis + differential diffusion)
  (Receipts §19).
- Memory-exponent collapse near the Wall ($\beta_{\text{mem}} \approx 1-\epsilon$) (Receipts §9).
- Auto-tuning inverse-form $w_i = \gamma_{\text{ref}}/\gamma_{s,i}$ on substrates requiring diagonal
  stability (Receipts §20).
- Common-exponent condition for the $s$-regime exponent identity. Falsifier: substrate classes where the
  FDR exponent and queueing-tail exponent are measured to differ.
- Cobham–Haken bridge conditions: three substrate-side conditions, each with own falsifier.
- SBN strong-heterogeneity extension: falsifier on substrate classes where SBN spectral predictions and
  observed sync behaviour disagree quantitatively under strong heterogeneity.
- Toner–Tu active-matter overlay: direct for active-matter substrates; effective $v_0, \tau_R$ derivation
  a substrate-class residual for substrates lacking intrinsic self-propulsion.
- Deep-$c$ phase-lock collapse / multi-mode memory capacity loss (raised by the mpa-LEGAL fix to
  non-monotonic $Q$, 2026-05-20). Falsifier owed; named substrate owed.
- $k_{\text{frust}}$ cross-substrate instance (see "Open conjectures" below).

### Owed work (pipeline)

- **5-vector inversion** (`conformer/compute/five_vector.py::fit_kww5` first-cut exists; recovers $X$ on
  two_temp_ou to ~1–2%). Until landed + integrated, $X$-bearing verdicts read at the raw
  FDR-locus-slope layer per FALSIFICATION.md adjudication policy.
- **Domain-of-validity gate** on the conform pipeline (FALSIFICATION.md Finding 2: pure oscillation reads
  as `s_critical` with locus_residual ~0.8; no gating). Awaits the 5-vector fitter absorbing valid-aging
  residuals before a residual threshold can isolate out-of-domain cases.
- **Underdamped/oscillatory inversion** (FALSIFICATION.md Finding B): conform clamps to deep-$r$ on
  class-B laser ringing $C(\tau)$, $\chi(\tau)$. Adjudicate alongside Finding 2 when the domain gate /
  5-vector work is taken up.
- **Auditor layer never exercised on controls.** Once inversion carries $X$, push a control cell through
  the auditor and check the regime story.
- **$\varepsilon$-machine stationarity-gap criterion.** Substrate-thermodynamic derivation of the
  slow-variation criterion separating the trajectory-ensemble-local-stationarity reading from the
  time-varying-$\varepsilon$-machine reading.
- **Two-frame velocity-frame closure + real-substrate contract (future research).** The two conjugate FDR
  frames are promoted on *verdict-agreement* (§FDR signatures, "Two conjugate FDR frames"); the exact
  cross-frame magnitude identity $V_{ext}=\langle\sigma\rangle=J\!\cdot\!\mathcal{A}$ is owed to the
  **velocity-frame Harada–Sasa integral** (the position frame gives different functionals — confirmed on
  laser, driven_ring, and now the nonlinear `banach_active_ring.py`; driven_ring is the ideal closer
  since $\langle\sigma\rangle$ is exact there). Apparatus is ready on a nonlinear topologically-forced
  limit cycle (`library/banach_active_ring.py`: both frames run, TUR $T\ge1$, frustration-necessity
  control passes). A real §846-clearing instance needs **author-collected active-lattice data** — the
  public active-metamaterial deposits (Veenstra/Coulais/Bartolo, 2021–2025) lack the perturbation-response
  protocol and carry friction-dominated $\mathrm{Var}(J)$, so they read the self-frame's mean current but
  not its thermodynamic variance. See FALSIFICATION.md §TWO-FRAME + memory
  `project_harary_triad_substrate_data`.

### Open conjectures (research notes, not framework content)

- **$k_{\text{frust}}$ as second primitive axis.** The R1/R2/R3 ladder survived on a synthetic 3-cycle;
  Receipts §846 explicitly flagged the elevation to numbered primitive as "still steeping" and earned
  only by a real cross-substrate instance. Operational content (NESS circulation, complex spectrum,
  affinity ≠ magnitude) sits at the level of §Typed objects + §FDR signatures + §k_frust drain.
  Promotion remains available when a real substrate exercises (a) drive-independent NESS circulation, (b)
  chirality conservation under a chirality-preserving substrate transformation, (c) the three triality
  registers measuring the same thing — *on a non-synthetic system*. **Candidate substrate class
  (2026-05-22):** active non-reciprocal metamaterials wired into Harary-frustrated loops (Veenstra/Coulais
  robotic rings, Bartolo active hydraulics) are the real systems whose circulation is gauge-irremovable
  (topology-forced, not bias-removable) — the live §846 target. Bottleneck is data, not physics: no
  public deposit carries a perturbation-response protocol, and macroscopic-robot $\mathrm{Var}(J)$ is
  friction-dominated rather than thermodynamic (memory `project_harary_triad_substrate_data`).
- **$k_{\text{frust}}$ topology-floor posit.** Functional form not yet committed. Promote when a committed
  functional form ties the smallest-cycle-affinity floor to graph topology and a measurement names a
  falsifier substrate.
- **$k_{\text{frust}}$ information-native characterisation.** $k_{\text{frust}}$ currently lives natively
  in dynamical-systems / differential-geometric registers; its information-face is a derived
  consequence-set (forced past-future mutual information; non-zero KS entropy). Owed: a
  substrate-independent information-native characterisation (candidate direction: topological mutual
  information that survives detailed-balance restoration).
- **Bilingual register as a structural-universality claim.** The bit/chit dual ledger (§Thermodynamic and
  informational accounting) is per-row content with a stated falsifier ($I_{\text{pred}}$ scaling
  deviation). The further claim that "the dual mapping itself is substrate-independent" needs a substrate
  test independent of the per-row falsifier; until then, it lives as expository organisation, not
  framework content.
- **Substrate-transformation classification (chirality-preserving / chirality-flipping / axis-mixing).**
  Two known entries already live in their original homes: Markovian $\gamma$-sign inversion
  (§Substrate-conditional reading rules) and strong-chaos Wall round-trip (§k_frust drain R2). Three
  candidate residuals (time-reversal on non-conservative substrates; parity on active-matter substrates
  with definite $C$ sign; mirror operations on intrinsically chiral substrates) are future work. Promote
  when a substrate test names a chirality-preserving transformation and demonstrates identity-class
  non-interconversion.
- **Chirality-typed identity catalogue.** The predictive content — "chiral identities have sharper
  substrate-class scope than achiral ones" — needs a substrate where the prediction has been (or will be)
  tested. Promote when that substrate is named.
