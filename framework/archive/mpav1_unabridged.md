# Metastable Propositional Algebra
## The finite-drive deformation of Boolean structure — a structural reading and a dynamical reading

Ron Viers · Claude v4.7 Opus (Anthropic)  
· Kimi v2.6 (Moonshot AI) · Gemini v3.6 (Google)

> **Status.** Public-facing prose-and-prior-art version of MPA — the structural and Character projections
> joined at one spine. Rebuilt periodically from the operational source of truth
> [`mpav1_compressed.md`](mpav1_compressed.md) (+ [`mpav1_receipts.md`](mpav1_receipts.md), which carries the
> line-keyed justifications, derivations, and falsifier formalisations); allowed to lag between rebuilds, so
> read the compressed for operational lookups. The open attack front is `FALSIFICATION.md` — read it when
> asking *what are we trying to break?*

## Abstract

Metastable Propositional Algebra (MPA) is a substrate-neutral specification language for the
driven-dissipative dynamics of propositional structure. Its organising fact is a deformation: Boolean
logic is the infinite-drive limit of a dissipative algebra, recovered as $D \to \infty$ where
$D = \Phi^*/\kappa$ is supplied work over the dissipation scale, and MPA is the finite-$D$ interior — what
the Boolean ring becomes when maintaining a proposition costs work against a bath. Read end to end, the
deformation runs from topology to asymptote: from the signed coupling graph and its Harary balance, to the
open-interval boundaries that the framework's observables approach but never attain at the $D\to\infty$
Boolean ceiling. The deformation carries two independent faces. The **amplitude face** is the headroom
coordinate $\mathrm{chit} = \ln(G_0/L)$, which drives the migration of a proposition through the
committed, suspended, and reset regimes and whose cross-substrate observables are the aging slope
$\alpha_s$ and plateau $P_s$. The **sign-topological face** is Harary-imbalance of the coupling graph,
which forces a topologically protected circulating current with order parameter the Schnakenberg cycle
affinity $\mathcal{A}$. The two faces are coordinates of one deformation but independent axes; the
framework couples neither to the other.

The same phenomenology admits two complementary readings. The **structural** projection is the discrete
operator algebra ($C, S, K, R$ taking the operational roles of AND/OR/XOR/NOT as $D\to\infty$) — the
finite-$D$ interior of the Boolean section. The **Character** projection is the continuous economics of
*being* a coherence on that graph against a bath — the dynamics that traverse the algebra. MPA introduces
no new mechanism on either reading: it imports the Reed–Muller/ANF ring, Harary balance, the May–Leonard
heteroclinic cycle, Schnakenberg affinity, Cugliandolo–Kurchan aging, Wilson–Kadanoff renormalization, and
Landauer-grounded stochastic thermodynamics, and reads each under sustained dissipation. Its most direct
cross-substrate instance is the surface-code aging diagonal: distance-3 rotated memory-Z syndrome streams
trace a Cugliandolo–Kurchan aging shape at sub-threshold operation, placing quantum error correction in
the CK universality class, and the framework predicts the locus migrates toward unit slope as the
physical-error rate crosses threshold. Its falsifier of record is the **Central commitment** —
the onset of protected NESS circulation requires a Harary triad — staked as a named, un-instanced
prediction about biological homochirality.

---

# SPINE — the Boolean→MPA deformation

The spine is organised end to end around one structure: MPA *is* the finite-$D$ deformation of the
Boolean ($D\to\infty$) ring. The reading runs topology → asymptote — from the signed coupling graph and
Harary balance, to the open-interval boundaries at the Boolean ceiling. The deformation has **two
independent faces**, an amplitude face and a sign-topological face, and every section that follows is a
beat in that one argument: each hangs off one face or the other.

## Setting & primitives

The dimensionless drive $D = \Phi^*/\kappa$ — supplied work over the dissipation scale — is the parameter
the framework works in. Boolean structure is the $D\to\infty$ limit of operator action; at finite $D$ the
operators are dynamical actions on trail structure, and the framework's predictive content is the *shape
of the deviation* from that limit. Maintaining a proposition costs work; cut the work, and the structure
dissolves. Substrate classes are characterised by the $(\Phi^*, \kappa)$ envelopes their realizers can
produce, intersected with the $D$-values the spec asks for.

The same setting read in the continuous register: a **coherence** is a macroscopic pattern of
continuation maintained against natural dissolution; a **holding** is the continuous extraction of entropy
or application of work that maintains it as a NESS. Where the structural reading supplies the stability
axis and the operator algebra, the Character reading supplies the laser-threshold conjugate that traverses
them — the syndrome-measurement stream that holds a surface-code logical qubit (Kitaev 2003; Fowler et
al. 2012), the cage maintenance of a glassy supercooled liquid, the carrying-capacity adjustment of a
Lotka–Volterra ecology (Hofbauer & Sigmund 1998), the reinforcement-extinction loop of a Rescorla–Wagner
behavioural substrate (Rescorla & Wagner 1972) are all holdings, read off one axis.

**Primitives (unioned across the two readings).**

- *Structural.* The **trail vector** — the kernel-weighted history of how the system has moved while a
  proposition was active; the drive $D$; and the observer kernel $\tau_{obs}$ through which a trail is
  read. When two propositions conflict, their trails push the system in incompatible directions, and that
  destructive interference is the physical substrate of logical contradiction.
- *Substrate (Character).* The **gain rate** $G_0$ (the unsaturated rate at which the coherence is pumped
  above threshold, scaling with $D$; the laser small-signal gain), the **loss rate** $L$ (spontaneous
  relaxation to the bath; cavity loss), and the signed edge structure $\gamma_{AB}$ on the mode graph.
  $G_0$ and $L$ are both rates ($[\text{time}^{-1}]$; the kernel term $(G_0 - L)\rho$ and the linearised
  $\lambda_A \approx L - G_0$ fix this), so the chit $\ln(G_0/L)$ is a log-ratio of rates. The pair
  $(G_0, L)$ is the holding's instantaneous economic state.
- *Derived primitive (the operational anchor).* $\mathrm{chit} = \ln(G_0/L)$ — the headroom above
  threshold. The framework's operational content keys to chit; its full treatment is §The chit unit
  (Character wing).
- *Topological invariant.* $k_{\text{frust}}$ — a cycle of $c$-edges with obstructive shear product, not
  resolvable by drive. It is derived (a heteroclinic-cycle consequence of the universal kernel and Harary
  structural balance), and its operational content — *the stationary state is irreducibly a NESS, a
  topologically forced circulating current* — survived the R1/R2/R3 falsification ladder (Receipts §846;
  FALSIFICATION.md Finding 4). Its elevation to a numbered framework primitive awaits a real
  cross-substrate instance (§Open items); the operational content stands without it.

## The deformation & its two faces

### The Boolean section $\mathcal{M}_2$

Write $\mathcal{M} = \{c, s, r\}$ for the vertex regime space and $\mathcal{M}_2 = \{c, r\}$ for its
Boolean section. Three independent characterisations identify the same two-cell set: $\mathcal{M}_2$ is
the codomain of the difference operator $K$; it is the fixed-point set of the coarse-graining flow ($c\to
c$, $r\to r$, with the metastable $s$ migrating to one or the other); and it is the section on which the
limit-equivalence quotient $q: \mathcal{M}(\infty) \to \mathbb{B}$ restricts to a bijection. The same
two-cell algebra is read three ways. Restricting the operator signature $\Sigma = \{C, S, K, R, \top,
\bot\}$ to $\mathcal{M}_2$ yields a Boolean algebra isomorphic to $(\mathbb{B}, \land, \lor, \oplus,
\neg)$. Closure holds at the level of the Boolean shadow $\sigma$, not necessarily at the regime label:
with $\mathcal{M}_2$-inputs, $C$ can still produce $s$ (an orthogonal or drive-covered merge is
metastable but maintained, and $\sigma(s) = 1 = \sigma(c)\land\sigma(c)$), so the homomorphism is
preserved even when the label strays. The full interface dynamics at $\mathcal{M}_2 \times \{s\}$ are the
boundary rules below.

### Reed–Muller / ANF, and what deforms

$\mathcal{M}_2$ is not a classical prejudice grafted onto the framework; it is the algebraic ceiling the
deformation runs toward. Presented as a ring, $\mathcal{M}_2$ is the $\{\oplus, \land, 1\}$ Reed–Muller /
algebraic-normal-form ring — $\oplus = K$, $\land = C$, $1 = \top$, with $\neg$ recovered as $\oplus\,1$.
MPA is its finite-$D$ deformation. The deformed piece is the involution: $R$'s irreversibility ($c \to r$,
non-involutive at finite drive) is the deformation of Boolean negation, and the drive $G_0$ — entering
through the chit register $\ln(G_0/L)$ — is the deformation coordinate, not the ring's unit $1$. This is
the binding that tethers MPA to a known structure: the v9 algebra is a finite-$D$ deformation of the
familiar $\{\oplus, \land, 1\}$ ring, and the deformation is what the rest of the spine measures.

### Two faces

The deformation off Boolean carries two independent coordinates.

The **amplitude face** is continuous: $\mathrm{chit}/D$ drives the $c \to s \to r$ migration, and its
cross-substrate observables are the aging slope $\alpha_s$ and plateau $P_s$ (§FDR signatures). This is
the face the Character projection traverses; its coordinate, the chit, gets its full treatment in the
Character wing.

The **sign-topological face** is topological: the Harary balance of the signed coupling graph. Boolean is
the *balanced* — equivalently, *gaugeable* — ring: every signed cycle has even negative parity, so a node
gauge $\varepsilon \in \{\pm 1\}^N$ renders the graph unsigned, the spectrum real, and no current
protected. The deformation's sign-face is **Harary-imbalance**: the chimeric sign of a Harary triad (the
minimal frustrated cycle, defined under §Central commitment) *is* the coordinate away from balance — the
ANF-ring deformation made dynamical — with order parameter the gauge-invariant cycle affinity
$\mathcal{A}$. Boolean (gaugeable) $\leftrightarrow$ MPA (deformed) is one structure read at two depths.

The two faces are coordinates of one deformation but **independent axes**. The sign-topological face is
topological, not amplitude: it is the source of $k_{\text{frust}}$'s invariance under the observer kernel
(§Scale-relativity), and organising the spine around the deformation does **not** couple the amplitude
observables $\alpha_s, P_s$ to the topological one $k_{\text{frust}}$. This independence is load-bearing
and is preserved throughout.

**MPA adds no object.** It imports the ring (Reed–Muller/ANF), the balance (Harary 1953), the cycle
(May–Leonard), and the affinity (Schnakenberg 1976), and reads them under sustained dissipation. The
framework's content is the reading, not the machinery.

### Two bits, one per face

The deformation carries a distinct *bit* on each face, and their non-interconvertibility is the sharpest
expression of the two faces' independence.

- The **amplitude bit** is the $D\to\infty$ endpoint of the chit axis: a which-state (occupancy)
  distinction, *emergently* discrete — continuous until the limit. It is erased by $R$ at the Landauer
  floor $W/\kappa \ge \ln 2$, must be *held* against thermal leak, and is flippable reversibly at no
  fundamental cost.
- The **topological bit** is the chimeric sign of a Harary triad on the sign-topological face: a
  which-wiring distinction, *intrinsically* discrete at every finite $D$ — cycle parity is binary, with
  no limit to approach — gauge-irremovable, and invariant under both $\tau_{obs}$ and continuous amplitude
  variation. It is *free to hold* (topological protection, no barrier leak), but not flippable reversibly:
  protection forbids a continuous CW$\leftrightarrow$CCW path, so any chirality change is forced through
  the balanced (sign-erased) state, paying $\ge \ln 2$ per protected sign. **The thermodynamic cost moves
  from maintenance to modification.** Reference class: topological quantum memory (Kitaev 2003); MPA
  imports the structure and reads it dissipatively, adding no mechanism.

Their orthogonality is measurable: chit, the quality factor $Q$, and the full FDR locus can be swept
continuously while the topological bit stays locked — a decoupling impossible in a two-level memory, where
the informational and energetic degrees of freedom are the same object. The forced-erasure floor counts
the independent protected signs (the cycle-space dimension of the frustrated subgraph): a bound saturated
quasistatically, not a quantisation. The operator signature is complete on the amplitude face but carries
no operator on the sign-topological face — $R$ and the deferred transfer operator $T$ are state-level,
while chirality surgery is graph-level. The decoupling is the falsifier: it fails — and the framework with
it — if the protected sign cannot be held without a per-time maintenance cost scaling with held duration
(an amplitude bit in disguise), or if the chirality can be flipped along a continuous path below $\ln 2$.
Formalised in receipts (§Two bits / topological-Landauer).

### The bit/chit correspondence

The per-event correspondence between the two bits' costs is the framework's natural thermodynamic↔informational
bridge, and the discrete↔continuous hinge of the whole construction: the chit is the continuous instance
whose $D\to\infty$ Boolean endpoint is the bit.

| Axis | Thermodynamic | Informational |
|---|---|---|
| Per-event | $\mathrm{chit} = \ln(G_0/L)$ | $\mathrm{bit} = \ln 2$ |
| Per-rate | $\langle\sigma\rangle$ | $I_{\text{pred}}$ |
| Precision | TUR | channel capacity |
| Compression | heat-tax tower | rate-distortion tower |
| Coupling | $\langle\sigma\rangle \ge -\Delta I$ | (same bound, dual reading) |

The apparatus behind each row — the thermodynamic-uncertainty detail, the $\varepsilon$-machine cryptic
order, the optimal-encoding derivation — lives in §Thermodynamic and informational accounting (Character
wing). The per-event row is solid; whether the dual *mapping itself* is substrate-independent is a
separate, stronger claim that stays expository, not framework content (§Open items › Open conjectures).

### Central commitment (the falsifier of record)

The stand the framework makes on the sign-topological face is planted as a falsifiable claim, not held
back awaiting confirmation. It is the narrower **ignition** claim — distinct from, and not dependent on,
the gated elevation of $k_{\text{frust}}$ to a numbered primitive (§Open items).

A **Harary triad** $\triangle_H$ is a directed 3-cycle that is non-reciprocal ($M_{ij} \neq M_{ji}$),
Harary-unbalanced (an odd number of negative edges, so no node gauge balances it), and chiral (the
sign-product fixes a circulation handedness no gauge removes). $N=3$ is the minimal frustrated cycle: a
non-reciprocal two-mode current circulates but is gauge-removable — not protected — so the triad is the
minimal carrier of *gauge-irremovable* circulation. The cycle affinity
$\mathcal{A} = \oint_C v/D$ is the Schnakenberg log-rate-ratio (in nats), gauge-invariant, and the
spectrum of $M$ carries a complex-conjugate pair if and only if $\mathcal{A} \neq 0$.

> **Commitment** (onset necessity — *not* generativity, *not* determinism). The onset of
> topologically-protected NESS circulation ($\mathcal{A} \neq 0$, removable only by edge deletion)
> requires a Harary triad:
> $$\text{protected circulation} \;\Rightarrow\; \triangle_H \text{ in the coupling graph.}$$

The claim is on ignition only — what it takes to spin a current up. It does *not* claim that
$\triangle_H$ generates the $c/s/r$ backbone ($\alpha_s, P_s$ remain independent), and it claims no
exclusive post-onset traction. This scoping is exact: ignition-necessity, not generativity, not
determinism.

A single real substrate — not synthetic — sustaining topologically-protected circulation
($\mathcal{A} \neq 0$, removable only by rewiring) with no Harary triad in its coupling graph would
collapse the commitment; the formal statement is in receipts (§Central commitment). The claim is
un-instanced on a real substrate, the only instance being synthetic
(`library/banach_frustrated.py`); the stand is planted here precisely because it is not yet met.

### Named prediction — biological homochirality (staked, un-instanced)

The framework predicts that biological homochirality is not a frozen historical accident but an *actively
maintained* coherence whose single handedness is the gauge-irremovable chimeric sign of a Harary triad.
Life sustains one chirality against spontaneous racemization — the natural dissolution — through
continuous dissipative proofreading, the holding; the framework predicts that this maintenance network
carries a topologically-protected circulating current ($\mathcal{A} = \oint v/D \neq 0$, a
complex-conjugate Jacobian pair, broken detailed balance) whose chimeric sign — *which hand* — is
removable only by rewiring, never by continuous deformation. The protected sign is the maintained bit:
chirality is read as the primordial Boolean distinction, and its universality across all extant life is
the macroscopic signature of topological protection rather than bistable inheritance.

*Probe placement.* Instrument the network that maintains chirality against racemization (the chiral
proofreading/editing system) and measure (i) the steady-state cyclic fluxes among chiral states and (ii)
the Jacobian spectrum of the linearised maintenance dynamics. The prediction requires a frustrated
$\ge 3$-node cycle — minimal core a non-reciprocal, odd-negative-signed 3-cycle — sustaining a circulating
current with a complex Jacobian pair and a gauge-irremovable sign.

The decisive test is a drive-sweep. Titrate the metabolic drive (ATP/GTP) toward zero: the current
*magnitude* must collapse toward the racemic limit while the *sign* remains invariant. A handedness flip
would mean the sign was drive-set rather than topology-protected, and the framework is invalid here. Three
structurally equivalent nulls are each fatal — a gauge-balanced maintenance network (no frustrated cycle),
a two-component bistable mechanism (no 3-cycle), or detailed balance at steady state (no current). This is
a bolder test than the general onset-necessity commitment, staking the framework on a specific, universal,
ancient phenomenon. The framework specifies the signature and the kill conditions precisely and the
subsystem approximately; it does not derive the molecular identity of the three nodes — substrate
biochemistry is imported, not generated. The formal falsifier is in receipts (§Homochirality).

### Boundary rules and terminal attractor

At the interface $\mathcal{M}_2 \times \{s\}$ — one input Boolean, the other metastable — the operators do
not reduce to Boolean identities, because edge shear and drive budget remain active: $\bot$ is not a global
annihilator and $\top$ is not a global identity. $C(\top, s)$ tracks the edge and budget; $C(\bot, s)$ and
$S(\bot, s)$ pass through; $S(\top, s)$ goes to $s$ or to competitive dropout; $K(\top, s)$ turns on
residual non-parallelism. These are dynamical rules, not equations — the operator-level shadow of the
mentor pairing (§Composite catalogue).

Under the compression flow (§Compression / heat-tax), $\mathcal{M}_2$ is the **terminal attractor**:
repeated compression contracts every proposition toward $c$ or $r$ geometrically, and $\epsilon$ measures
the residual information mass left outside $\mathcal{M}_2$ after each step. $\mathcal{M}_2$ is therefore
neither a separate algebra grafted on nor a Boolean prejudice imported; it is the fixed-point set of the
framework's own renormalization-group flow, the codomain restriction that makes $K$ structurally unique,
and the terminal object that makes the compression tower converge.

## Typed objects & the bridge

The framework classifies static structure on a coupling graph into three objects of distinct type, and
the typing is load-bearing: each object answers to a different layer of the deformation. Truth values are
endpoints — a proposition stably maintained approximates $1$, one decayed into the bath approximates $0$ —
and between them lie three kinds of structure.

A **vertex regime** is the state of a single trail on a one-dimensional stability axis, read off the
Lyapunov rate $\lambda_A$:

- $c$ (committed): $\lambda_A \ll -D$ — self-sustaining, approximating $1$ with minimal external work.
- $s$ (suspended): $\lvert\lambda_A\rvert \lesssim D$ — true-while-pumped; marginal, held against decay by
  active maintenance, gone if the pump stops.
- $r$ (reset): $\lambda_A \gg D$ — decayed, approximating $0$, at no maintenance cost.

The three-regime threshold is the cooperativity pattern of driven open quantum systems (Sieberer,
Buchhold & Diehl 2016) and the pump–loss balance of laser-threshold theory (Haken 1985); MPA reads regime
labels off the same stability axis those literatures already work in. Forgetting is not a separate
operation — an unreinforced trail shrinks until its projections fall below the noise floor and its
cross-dissipations evaporate into the bath.

An **edge** carries a signed shear $\gamma_{AB}$: $\gamma < 0$ cooperative (trails reinforce),
$\gamma \approx 0$ orthogonal (independent), $\gamma > 0$ conflicting (the shear must be paid for, at
per-edge cost $\gamma_{AB}$ in $D$-units). A **subgraph** carries $k_{\text{frust}}$: a cycle of $c$-edges
whose shear product around the loop is obstructive, admitting no drive that resolves it — the standard
topological invariant of a coupling graph (Mézard, Parisi & Virasoro 1987), read at its native level. The
framework's substrate-neutrality at the vertex (universality across microphysics) and its
substrate-specificity at the subgraph (the topology of the interaction graph) are the same fact stated at
two layers.

One thermodynamic distinction survives scale-relativity: self-sustaining structure, with internal coupling
closure, is energetically distinct from drive-pumped structure regardless of the kernel through which
either is read. The mentor pairing (§Composite catalogue) turns on this distinction even where the labels
at any single $\tau_{obs}$ do not.

**The bridge.** The two readings meet at a coordinate hinge. At zero amplitude the linearised field
equation has eigenvalue $\lambda_A \approx L - G_0$ (loss minus gain, the standard laser linearisation;
Haken 1983), and the structural regime conditions translate directly into the Character coordinates
$(G_0, L)$:

| regime | $\lambda_A$ vs $D$ | $G_0$ vs $L$ | reading |
|---|---|---|---|
| $c$ | $\lambda_A \ll -D$ | $G_0 - L \gg D$ | deeply above threshold; saturation-clamped |
| $s$ | $\lvert\lambda_A\rvert \lesssim D$ | $\lvert G_0 - L\rvert \lesssim D$ | near threshold; Schawlow–Townes broadening and Cugliandolo–Kurchan aging coexist |
| $r$ | $\lambda_A \gg D$ | $G_0 - L \ll -D$ | sub-threshold; spontaneous emission only |

$G_0/L$ and $\lambda_A/D$ are different coordinates on one regime structure. That is the hinge — two
coordinates, one regime structure — and it fixes the Character projection's relationship to the structural
one throughout. The substrate-conditional reading rules (§Substrate-conditional reading rules) inherit
across the bridge without modification.

## Operators

The operator algebra acts on $\mathcal{M} = \{c, s, r\}$ with Boolean section $\mathcal{M}_2 = \{c, r\}$.
Each operator is a constructive protocol whose infinite-drive limit reduces to a Boolean connective; at
finite drive it is a dynamical action on trail structure, and the Character projection reads off its
continuous-traversal shadow. The two readings sit side by side:

| Op | Signature | Action | $D \to \infty$ limit | Continuous-traversal shadow |
|---|---|---|---|---|
| $C$ | $\mathcal{M}^2 \to \mathcal{M}$ | try to merge: $d_{A\oplus B}=w_A d_A + w_B d_B$, evaluate $\lambda_{A\oplus B}$ | $\land$ | $C_{\text{Character}}$ (merge), below |
| $S$ | $\mathcal{M}^2 \to \mathcal{M}$ | hold both: $\lvert\lambda_A\rvert+\lvert\lambda_B\rvert+\max(0,\gamma_{AB})\le D$ | $\lor$ | — |
| $K$ | $\mathcal{M}^2 \to \mathcal{M}_2$ | $\delta(A,B)=\hat d_A - \hat d_B$, $\lambda_{A\ominus B}=\lvert\gamma_{AB}\rvert-D/2$; $c$ if $\delta\ne 0$ ∧ $D>2\lvert\gamma_{AB}\rvert$, else $r$ | $\oplus$ | — |
| $R$ | $\mathcal{M} \to \mathcal{M}$ | sever to bath: $W_R/\kappa \ge \ln 2 \cdot H(A\mid\text{rest})$; recovers Landauer when $\kappa = k_BT \cdot \xi_{sub}$ | $\neg$ | $R_{\text{Character}}$ (sever), below |

$C \in \Sigma$, the try-merge operator, is a distinct object from the compression operator $\mathcal{C}$
of §Compression / heat-tax — a different category (an operator on trails, not on the ledger tower); the
typographical distinction is preserved throughout. $K$ is the unique operator whose codomain is restricted
to $\mathcal{M}_2$: the quotient acts on its *inputs* rather than its output, the coordinate-free
expression of where the metastable $s$ sits in its signature. Over $\mathbb{F}_2$, $K$ is the
parity-check object that distinguishes XOR-SAT from $k$-SAT (Mézard, Ricci-Tersenghi & Zecchina 2003).

**$C_{\text{Character}}$ (merge)** is the continuous shadow of $C$: an adiabatic deformation from
$\gamma_{AB} \approx 0$ to $\gamma_{AB} \ll 0$ while sustaining the NESS, the deformation rate slow
relative to $L$. Forced non-adiabatically, the chit approaches zero, the system enters $s$-regime visible
strain, and the Harada–Sasa entropy production spikes before the cooperative fixed point is acquired; if
the drive cannot cover the transient, one or both modes drop sub-threshold. Information-geometrically the
merge succeeds iff a Fisher-information geodesic stays on the above-threshold manifold (Amari & Nagaoka
2000). Sampled at fixed $D$, the adiabaticity bound recovers the structural Theorem 9 in the
sharp-threshold limit, $\Delta_C(A,B) = 1$ iff $\gamma_{AB} > 0 \land D < \gamma_{AB}$ — the Boolean step
is the sharp limit of a continuous survivability function.

**$R_{\text{Character}}$ (sever)** is the quench: choke $G_0$ (demand-load) or open the mode to the bath
($L\uparrow$, decay-load). The edge dissolves natively — $\gamma_{AB}\rho_A\rho_B$ vanishes as
$\rho_A \to 0$, with no separate graph-edit — and the discrete Landauer bound is the integrated cost of
the quench, the asymptotic limit of the driven-dissipative collapse.

## Scale-relativity

The vertex label of a trail depends on the kernel $\tau_{obs}$ through which it is read: the same trail
returns $c$ at narrow windows, $s$ at intermediate, $r$ at wide, with the substrate's intrinsic timescales
fixing where each dominates. The hierarchy itself is substrate-fixed; only the labels migrate. The edge
shear $\gamma$ scales with $\tau_{obs}$, because cross-correlation depends on the integration window. The
subgraph invariant $k_{\text{frust}}$ does **not** migrate — it is a topological property of the coupling
graph, not of the kernel, and is either present or absent. The amplitude face moves under the camera; the
sign-topological face does not.

## Composite catalogue (molecular layer)

The vertex regimes are atomic and the operators are pair-actions; between them sits a molecular layer,
where two propositions in specified regimes under a specified edge occupy a composite regime. The
catalogue has two faces of one rule-set — a discrete composite face (vertex + edge), and a continuous
phase-relationship face (sweeping $\gamma_{AB}$).

| Pair | Edge | Composite | Field-name |
|---|---|---|---|
| $c$–$c$ aligned | $\gamma<0$ | $c$ deepened | Hebbian; force chains |
| $c$–$c$ orthogonal | $\gamma\approx 0$ | $s$ | independent memory |
| $c$–$c$ opposed | $\gamma>0$ | $s$ if $D$ covers, else one→$r$ | competing hypotheses |
| $c$–$s$ | $\gamma<0$ | $s$ (mentor) | synaptic tagging; pilot-light |
| $s$–$s$ | $\gamma>0$ | $s$ or competitive dropout | Lotka–Volterra |
| $c$–$c$–$c$ cycle | obstructive product | $k_{\text{frust}}$ | gridlock; UNSAT |
| oscillatory–$c$ | limit cycle, $\lambda_B \ll 0$ | entrainment / quench | Kuramoto; circadian |

| Regime | $\gamma_{AB}$ | Phase relationship |
|---|---|---|
| $c$–$c$ aligned | $\ll 0$ | in-phase locked (Hebbian / force chain) |
| $c$–$s$ mentor | $< 0$, asymmetric | driven entrainment, non-reciprocal, priority queue |
| $c$–$c$ orthogonal | $\approx 0$ | unlocked / phase drift |
| $c$–$c$ opposed (lock) | $> 0$, $K > \Delta\omega$ | anti-phase locked |
| $c$–$c$ opposed (split) | $> 0$, $K < \Delta\omega$ | competitive desync (pitchfork) |
| $k_{\text{frust}}$ | $N \ge 3$ obstructive | frustrated sync |

Per row, MPA's contribution is modest: the field already has the phenomenon — Hebbian co-firing, synaptic
tagging (Frey & Morris 1997), Lotka–Volterra competition, Kuramoto entrainment (Kuramoto 1984), $k$-SAT
frustration — and the framework supplies a unifying mapping. Per table, the contribution is sharper: one
vertex+edge rule-set generates phenomena with no shared microphysics across neuroscience, ecology,
statistical mechanics, combustion, and organisational dynamics. The cycle / $k_{\text{frust}}$ row sits at
a different type — a subgraph, not a pair — the molecular layer's natural carrier of the topological
object. (The Adoption catalogue of the Character wing inherits this same per-row / per-table reading.)

## Capacity

In Boolean logic structure is free; at finite drive it is not. For a classically consistent graph — one
containing no $k_{\text{frust}}$ — with average degree $d_{avg}$ and minimum interaction cost
$\gamma_{min}$, the maximum sustainable subgraph $\Gamma^*$ has a static structural ceiling

$$|\Gamma^*| \le \sqrt{\frac{2D}{\alpha\,\gamma_{min}\,d_{avg}}}.$$

Sparse graphs scale linearly with the drive; dense graphs scale only as $\sqrt{D}$, because
edge-maintenance costs dominate once the graph thickens. The square-root ceiling is the Hopfield storage
capacity (Amit, Gutfreund & Sompolinsky 1985); the dense-graph wall under constraint pressure shows the
corresponding sharp threshold (random $k$-SAT; Mézard, Parisi & Zecchina 2002). The bound predicts modular
sparsification rather than describing it after the fact — organelles, cortical functional segregation,
clonal selection in immunity are the empirical shadow of the $\sqrt{D}$ ceiling. Classical consistency is
load-bearing: $k_{\text{frust}}$ marks where structure is unsustainable at any drive, and the Complexity
Wall (§Compression / heat-tax) is the spectral analogue at the meta-ledger layer.

The Character projection supplies the dynamic conjugate to the static ceiling. A sustainable phase-locked
subgraph requires the integrated loss to fit inside the cooperatively shared budget,

$$\sum_{i \in \Gamma^*} L_i \le G_{total}\,\eta(\Gamma^*),$$

with cross-saturation efficiency $\eta(\Gamma^*) \in (0,1]$ and $\eta \to 0$ at the $\sqrt{D}$ Hopfield
ceiling, where non-orthogonal interference between continuous flows depletes the shared gain. This is not
a second wall but the same wall read from the dynamic side, and its closure is Erlang's loss formula
(Erlang 1917):

$$\eta(\Gamma^*) = 1 - B(c,\rho), \qquad B(c,\rho) = \frac{\rho^c/c!}{\sum_{k=0}^c \rho^k/k!},$$

with $c = \lfloor|\Gamma^*|_{\text{crit}}\rfloor$ and $\rho$ the effective offered load on the mode-slot
pool. The soft/hard split is itself a substrate-class fingerprint: soft substrates cross over smoothly,
while hard-wall substrates — a surface code at logical-error onset, where one error breaks the code —
replace $B$ by the indicator $\mathbb{1}[|\Gamma^*| \ge c]$ and fail abruptly at threshold. A behavioural
or cognitive substrate exhibiting sharp Hopfield-snapping instead of Erlang-B tails, or a QEC-class
substrate showing soft Erlang-B blocking instead of an abrupt threshold, would falsify the split (receipts
§5/§22; surveyed in §Open items). When the inequality is violated the system sparsifies — dropping
vertices to $r$ — or distributes the deficit into a sub-threshold phase transition, regardless of local
chit margins.

## FDR signatures

Coherences are path-dependent NESS, and equilibrium fluctuation–dissipation fails on them. The apparatus
reads a trail's spontaneous fluctuations $C(\tau)$ against its response $\chi(\tau)$ to a small probe, in
the parametric plot $\chi(\tau)$ versus $C(0)-C(\tau)$; by the Harada–Sasa equality (Harada & Sasa 2005)
the integrated FDR-violation is the steady-state entropy-production rate $\langle\sigma\rangle$ — the true
thermodynamic cost of holding without arresting. Each object of the typing leaves a distinct trace, three
vertex regimes and one subgraph:

| Regime | Chit | Invariant | Reading |
|---|---|---|---|
| $c$ | $\gg 0$ | $X_c = \lim_\tau \chi(\tau)/(C(0)-C(\tau)) = 0$ | suppression / narrow horizontal locus |
| $s$ | $\to 0^+$ | $\alpha_s = $ slope of aging segment in $\chi$ vs $(C(0)-C)$ | Cugliandolo–Kurchan ratio |
| $s$ | $\to 0^+$ | $P_s = \lim_\tau C(\tau)/C(0)$ | plateau height |
| $r$ | $< 0$ | $X_r = \lim_\tau \chi(\tau)/(C(0)-C(\tau)) = 1$ | unit-slope FDR |
| $k_{\text{frust}}$ | non-stationary | $N_f = \int_T \min(0,\chi)\,d\tau \big/ \int_T \lvert\chi\rvert\,d\tau$; drive-independent affinity; complex Jacobian spectrum | transient-negative fraction; spin-glass loop signature (§k_frust drain) |

The aging slope $\alpha_s$ and plateau $P_s$ are the load-bearing cross-substrate observables; the rest are
within-class structural identifiers ($X \gg 1$ is excluded by dissipative dynamics — an unstable
amplifier, not a sustained representation). The $s$-regime signature is two-step: quasi-equilibrium
($X=1$) on short lags, FDR-violated aging ($X<1$, slope $\alpha_s$) on long lags, so a short-lag $X=1$
reading alone does not place a substrate in $r$ — the long-lag aging segment is the $c/s/r$ discriminator.
(On a driven-critical random-field Ising model the $s$-regime reads $X=0.118$ via a self-overlap,
staggered-field estimator — not the collective magnetisation, which is soft-mode-dominated near
criticality and gives an unstable $X$.)

The violation reads from two conjugate force–flux frames. The *external-probe* frame pairs amplitude with
an external field, giving the violation factor $X$ with $\alpha_s, P_s$ the aging observables; it needs a
probe. The *self-probe* frame pairs the current $J$ with the intrinsic affinity $\mathcal{A}$ (in nats),
giving a violation factor that is the thermodynamic-uncertainty-relation tightness
$T = \langle\sigma\rangle\,\mathrm{Var}(J)/(2\langle J\rangle^2)$, with measurable core
$\mathrm{SNR}_J = \langle J\rangle^2/\mathrm{Var}(J) \le \langle\sigma\rangle/2$ — dimensionless by
construction, and defined only where a current exists (a $k_{\text{frust}}$-bearing substrate).
Harada–Sasa bridges them in principle ($\int$FDR-violation $= \langle\sigma\rangle = J\!\cdot\!\mathcal{A}$).
The operational claim is the weaker one — *the same regime verdict wherever both frames are computable* —
confirmed on a real substrate (a class-B laser, where both frames flag NESS) and closed exactly on the
`driven_ring` testbed ($\langle\sigma\rangle = J\!\cdot\!\mathcal{A}$). The frames are different
functionals; their *disagreement* is the falsifier, and the exact cross-frame magnitude identity is a
refinement owed to the velocity-frame Harada–Sasa integral, not a gate (§Open items).

**Surface-code identification.** The framework's most direct cross-substrate instance. Distance-3 rotated
memory-Z syndrome streams (Kitaev 2003; Fowler et al. 2012) trace a clean $s$-aging diagonal at
sub-threshold operation, placing quantum error correction in the Cugliandolo–Kurchan universality class,
and the locus migrates toward unit slope ($X_r = 1$) as the physical-error rate crosses threshold. That $s \to r$ migration is the framework's primary
cross-substrate test and its most direct empirical content. The frustration negative-FDR signature is not
present in this measurement, and the absence is structural rather than evidential: uncorrelated
depolarising noise drives $s \to r$ (a vertex migration), not toward closed frustrated loops on the
syndrome graph, so the test for the frustration shape tightens to a noise model that closes such a loop.
The identification fails if syndrome FDR shows unit slope sub-threshold (no CK signature) or if its shape
persists unchanged across the threshold crossing (no migration); the formal statement is in receipts (§4).
A second prediction on the same data follows from scale-relativity — sweeping $\tau_{obs}$ at fixed
substrate should walk the locus through $c \to s \to r$, while $k_{\text{frust}}$ does not migrate.

A measurement caution carries from the falsification campaign: do not infer $X$ from a single linear slope
on an aging locus — it biases upward (a prescribed $X=0.2$ cell reads $0.47$ under a single slope, $0.26$
under a segmented fit). The five-vector inversion ($q_{EA}, \tau_\alpha, \beta_{\text{KWW}}, \tau_\beta,
X$) that would recover $X$ cleanly is owed (§Open items); until it lands, $X$-bearing verdicts are read at
the raw FDR-locus-slope layer, where the measurement is faithful (validated to ~2% on prescribed-$X$
cells).

## Compression / heat-tax — one RG flow, two ledgers

The ledger tracks the substrate; who tracks the ledger? An infinite tower of meta-ledgers threatens to
collapse the architecture under its own thermodynamic weight, and converges only under the **Compression
Axiom**: each ascent must strictly contract under the compression operator $\mathcal{C}$ (distinct from
$C \in \Sigma$), $\epsilon = \|\mathcal{C}\|_{op} < 1$. The flow carries two ledgers coupled at one RG
fixed point — an informational ledger that contracts structure, and a thermodynamic ledger that routes the
exhaust.

The **informational ledger** has the form of a Wilson–Kadanoff renormalization flow with Banach
contraction supplying convergence (Wilson 1975; Kadanoff 1966; Cardy 1996): $c$ and $r$ are fixed points,
$s$ is metastable (flowing to $c$ if reinforced, to $r$ if not), $\mathcal{M}_2$ is the terminal
attractor, $k_{\text{frust}}$ is invariant on substrates that carry it; edges follow their endpoints, and
Boolean is the degenerate limit where every level collapses to identity. Trail vectors are the
equivalence classes under this flow — $\mathcal{M}_2$ the cavity-method *frozen core*, $s$ the *free*
region (Krzakala et al. 2007).

The **thermodynamic ledger** routes the heat. Each ascent inflates the next level's decay rate,
$$L_{n+1} = L_{n+1}^{(0)} + \alpha_\sigma\langle\sigma_n\rangle + \alpha_\Sigma\langle\Sigma_n\rangle,$$
along two effect axes: $\alpha_\sigma\langle\sigma_n\rangle$ carries level-$n$ flow as ambient noise,
$\alpha_\Sigma\langle\Sigma_n\rangle$ carries level-$n$ maintenance as active stress. The conductivity is
Landauer-pinned, $\alpha_\sigma(\epsilon) = \alpha_{\sigma,0}(1-\epsilon)$: per-level Landauer heat
vanishes as $\epsilon \to 1$ (nothing erased), while the cumulative informational mass
$\Phi_{\text{total}} = \Phi^{(0)}/(1-\epsilon)$ diverges. The Wall's thermodynamic content sits in the
cumulative mass, not the per-level heat.

These are one flow established from two sides. $\mathcal{C}$ is not primitive: it is the heat-tax tower
flow re-presented on the space of slow-manifold generators — the level-to-level map induced by a
Mori–Zwanzig projection $\Pi_{\text{slow}}$ of the universal two-mode kernel, with $\epsilon$ the leading
infrared linear-stability eigenvalue, Landauer-pinned to the substrate's thermal conductivity. Banach
contraction $\epsilon < 1$ is therefore *derived* (IR fixed-point stability), not an axiom on an abstract
operator, and $\Pi_{\text{slow}}$ *is* the conjugating isometry of the Wilson–Kadanoff
structural-equivalence statement (receipts §6.5). Each level carries its own dimensionless drive
$D_n = \Phi^*_n/\kappa_n$, the contraction bounding $D_{n+1}$ against $D_n$: a compressed ledger tracking a
richer substrate must do so with proportionally less informational mass.

When $\epsilon \ge 1$ — insufficient spectral gap or modularity — the tower diverges: a thermodynamic
impossibility theorem on resource-bounded inference for maximally-entangled substrates. This is the
**Complexity Wall**, living in the cumulative informational mass. Sustained coherence at the next level
requires $\ln(G_{0,n+1}/L_{n+1}) > 0$, and fraying at level $n$ inflates $L_{n+1}$ through three channels —
the heat-tax spike, an active-stress spike, and an $r_n$ drop in collective sync that costs cooperative
gain-sharing. The three are not independent mechanisms but three registers of one queueing law: by the
Cobham–Kleinrock priority-queue mapping (Cobham 1954; Kleinrock 1976) they are faces of Cobham
wait-inflation $W_{n+1} = W_0/[(1-u_n)(1-u_{n+1})]$ across tower-level priority classes, whose singularity
at $u \to 1$ coincides with $\epsilon \to 1$ (and $u_n = \epsilon_n$ at rate-distortion-optimal encoding).
Channels two and three share $r$ in opposing directions — Toner–Tu hydrodynamics (Toner & Tu 1995) gives
an active-stress correction $f(r) = Cr^2$, and the substrate's active-coupling sign $C$ sets the balance.

Operationally, $\epsilon < 1$ is sufficient for every theorem above; structurally, $\mathcal{C}$'s
identification with Wilson–Kadanoff block-averaging is a type-identity, proven in the Markovian /
spectral-gap regime and extended to non-Markovian Caputo memory ($\beta_{\text{mem}} < 1$) by fractional
RG with the same construction. The cross-substrate transfer of $\alpha_s$ and $P_s$ universality (§FDR
signatures) is the strongest evidence that this renormalization programme is well-posed.

## k_frust drain (the sign-topological face, full treatment)

This is the full treatment of the topological object the Central commitment turns on. The stationary state
of a frustrated cycle is irreducibly a NESS — a topologically forced circulating current, broken detailed
balance (Receipts §846). The deterministic flow realises it in two sub-regimes by the
sign of the relaxation eigenvalue's real part — a stable circulating focus (Re $< 0$) that spirals into a
NESS which still circulates ($J \ne 0$), or a repelling focus with an attracting limit cycle (Re $> 0$) —
and both are $k_{\text{frust}}$: **the complex spectrum (irreducible rotation), not the non-existence of a
fixed point, is the invariant.**

The drive-independence belongs to the cycle *affinity*
$\mathcal{A} = \oint v/D = \ln(\prod_+ k/\prod_- k)$ — the intensive log-rate-ratio, forced nonzero
regardless of $D$ — not to the current *magnitude* $J_{ss}$, which scales with absolute kinetic rates and
so flows with chit (an operating-point sweep grew $J$ from $1.3\times10^{-2}$ to $2.5\times10^{-1}$ as
$G_0$ went $0.9 \to 2.0$). The falsifier therefore reads "$J$ becomes drive-noise-dependent *or* resolves
to detailed balance," not "$J$ is drive-dependent" — pump-dependence of the magnitude is legal
(§mpa-legal). The operational content survived a three-rung falsification ladder (Receipts §846): an
operating-point sweep (current sign-definite and drive-independent, $5.8\sigma$ above a matched reciprocal
control at chit $=0.010$); a Wall round-trip under strong chaos (frustration never destroyed — strong
chaos only flips chirality, and a reversed loop is still frustrated); and a gradient test (the
frustrated-loop Jacobian spectrum is complex at all coupling, while a matched cooperative control reads
real).

On a new substrate the predicted measurements — the falsifier surface — are three: the coexistence
Jacobian has complex eigenvalues at every coupling in the surviving range; $J$ is sign-definite,
drive-noise-invariant, and scales only with absolute kinetic rates; and after a strong-chaos Wall
round-trip the chirality may flip but $|J|$ recovers, while detailed-balance recovery (a real spectrum) is
forbidden while the wiring is intact. The loop-level gFDR shadow is the transient-negative response $N_f$
— but $N_f$ is a $\tau_{obs}$-conditional observer-shadow, weaker than the intrinsic $J$ meter, and no
kill-shot should rest on $N_f$ alone.

## Asymptotic closure

Every framework-prediction observable in MPA takes values in an open interval whose boundaries are $0$,
$1$, or $\infty$, and none attains its boundary at any non-asymptotic operating point. The boundaries
exist only as limits — $\mathcal{M}_2$ at $D \to \infty$, $\varepsilon \to 1$ at the Complexity Wall,
chit $= 0$ as a critical limit, $X_c \to 0$ deep in $c$, $X_r \to 1$ deep in $r$ (and at thermodynamic
equilibrium), $u_n \to 1$ at Cobham blocking, $\eta \to 0$ at the Hopfield ceiling, $\beta_{\text{mem}}
\to 1$ at the Markovian limit. The categorical labels $\top, \bot, k_{\text{frust}}$ exist only at the
$\mathcal{M}_2$ boundary or as discrete derivatives of continuous parameters; chit is the per-event
instance, a continuous $\ln(G_0/L)$ whose Boolean endpoint is the bit.

The structural commitment is that boundary values are asymptotic-only, and it is what makes the framework
continuous *across* observables, not merely within any one. An *attained* endpoint has left the domain, so
it surfaces as a NaN — a falsification tripwire, not a fillable value (which is why a state variable is
never clipped at $0$: clipping manufactures excluded zeros). The framework is falsified by any observable
shown to attain exactly $0$ or $1$ at a finite, non-degenerate operating point.

## Substrate-conditional reading rules

The framework's primitives are substrate-invariant; the *signs* and *natural preprocessing* of certain
observables are not, and two reading rules inherit identically across both projections. The **Markovian
sign caveat**: stiff or Markovian substrates (overdamped Langevin with stiff wells, conditionally
independent syndrome streams) invert the $\gamma$ signs while preserving magnitudes and FDR shapes — a
kernel-width artefact (a stiff well gives short $\tau_A$, hence positive $\gamma_A$). On such substrates
the classifier uses $|\gamma|$ and FDR shape jointly, not signs; for $k_{\text{frust}}$-bearing content
the inversion is chirality-flipping (the sign reverses), while chit-axis content is preserved. The
**detection-event rule**: where the readout violates the locality the trail integral requires — a single
physical error flipping every future measurement of an adjacent stabiliser — the substrate's canonical
local preprocessing is the correct input; for surface codes this is the detection event
$e_i(t) = s_i(t) \oplus s_i(t-1)$, bounded-local so an error at $t$ triggers exactly two events, with the
trail built by exponential-moving-average against detection events. These rules adjust how observables are
interpreted on a substrate, leaving the primitives intact, and new ones are earned by application work,
not posited.

# STRUCTURAL WING (v9 projection — the discrete operator algebra and its finite-$D$ interior)

The spine treats the deformation as a single object with two faces. The structural wing develops one of
them — the discrete operator algebra — at the resolution it deserves. The Boolean section $\mathcal{M}_2$
is an exact algebra; the finite-$D$ interior is its deformation, where closure, associativity, and
distributivity hold up to the quantified defects below. The wing covers how far the algebra bends from Boolean structure
as the drive falls, what operators open up when a structural commitment is relaxed, and the shape of the
landscape between the interior and the Boolean corner.

## Deformation calculus (the finite-$D$ interior)

The Boolean section is exact; the interior is quantified. Three theorems bound the deformation, each a
standard small-parameter expansion around the singular limit $D \to \infty$, each a candidate observable
on substrates where $D$, $\gamma$, and operator action are independently measurable:

| Theorem | Bound | Limit |
|---|---|---|
| 6 (associator) | $\lVert\alpha_C\rVert \lesssim (1/D)\sum\lvert\gamma\rvert$ | $\to 0$ |
| 7 (distributivity defect) | $\lVert\delta_{dist}\rVert \lesssim (1/D)[\max(0,\gamma_{YZ})-\max(0,\gamma_{XY},\gamma_{XZ})]^+$ | $\to 0$ |
| 9 (Boolean deviation) | $\Delta_C(A,B)=1$ iff $\gamma_{AB}>0 \land D < \gamma_{AB}$ | sharp threshold |

Theorems 6 and 7 give the associator and the distributivity defect a $1/D$ falloff — the order of pairwise
commitment, and the difference between committing-to-a-suspension and suspending-two-commitments, each
break only in proportion to pairwise shear and decay smoothly. Theorem 9 is sharper, and is the
framework's most direct quantitative criterion: a **resource-induced instability**, where two propositions
classical logic would conjoin cannot be jointly maintained because the budget does not cover the shear
($C(A,B)$ enters $r$ while $\sigma(A)\land\sigma(B)=1$). Its threshold $D < \gamma_{AB}$ is the same
cooperativity threshold as cavity QED and laser physics; a substrate's $\gamma$ profile measured at
operating $D$ determines exactly which propositional pairs admit joint commitment. This is where the
section docks the interior — the boundary rules are exact where the calculus is asymptotic. The defects
$\alpha_C$, $\delta_{dist}$, $\Delta_C$ are explicit operators with leading $O(1/D)$ bounds, vanishing as
$D \to \infty$.

## Extension axes

Each vertex regime is exhaustive only for the framework's current commitments — a scalar trail under a
single kernel, reciprocal pairwise couplings, continuous time. Relaxing any one opens a region of the
landscape with its own candidate operator, none with a Boolean shadow:

- **Limit-cycle trail** → a rhythm primitive whose content is irreducibly temporal, with a closed-loop
  FDR signature; the oscillatory–$c$ composite is its simplest pairing.
- **Hierarchical kernel** → multi-timescale holdings, fragile at one scale and stable at another, with
  multi-scale aging FDR. This axis parametrises the kernel-width dimension the regime classifier rides on
  and, under the equivalence-class formulation, carries the coarse-graining flow itself.
- **Non-reciprocal coupling** → dominance and inhibition primitives with no symmetric truth-table shadow
  and turbulent FDR; the non-reciprocal active-matter formalism (Fruchart, Hanai, Littlewood & Vitelli
  2021) is the appropriate mathematics.
- **Higher-order frustration** (hypergraph) → the graph-dimension generalisation of $k_{\text{frust}}$,
  expanding the cycle row into a full taxonomy of glassy phases with multi-plateau aging.
- **Finite-population discreteness** → a flickering $c \leftrightarrow r$ regime that natively grounds
  probabilistic logic rather than bolting probability on by hand.

Two further operators are deferred without elaboration: a **transfer operator** $T(A \to A')$ routing
$A$'s information to a recipient rather than the bath, at effective cost
$W_T/\kappa \ge \ln 2 \cdot [H(A\mid A',\text{rest}) - \mathcal{I}(A;A')]$ (irreducible cost minus a salvage
credit); and **latent ledgers** holding encoded structure at near-zero ongoing cost, decompressed on
demand.

## Falloff profile

The interpolation between the finite-drive interior and the Boolean corner has three faces. The
**longitudinal** falloff, along $D$ at fixed everything-else, is one of polynomial-in-$1/D$ (the form
Theorems 6–7 already exhibit), critical-scaling near the capacity wall, or
exponential-with-power-law-correction — distinguishable by FDR curves on a denser grid of operating
points. The **lateral** falloff, along the other commitments, asks whether the Boolean point is regular or
singular: if smooth everywhere, the extension-axis operators are perturbative ghosts; if it has cusps or
non-analytic boundaries, those operators inhabit phases unreachable from classical logic by any smooth
deformation. The **scale** falloff is the $\tau_{obs}$ sweep, which walks a vertex through $c \to s \to r$
while $k_{\text{frust}}$ stays put.

The framework's stake is that Boolean is a codimension-$N$ singular point in the parameter landscape, $N$
the number of commitment axes whose relaxation produces non-perturbative structure — the longitudinal
falloff being the codimension-1 slice. The mathematics is on hand: bifurcation and catastrophe theory
(Thom 1972; Arnold 1992) for how smoothness breaks at low codimension, spin-glass landscape theory
(Mézard–Parisi–Virasoro; Cugliandolo–Kurchan; Wolynes–Onuchic–Thirumalai) for metastable-basin geometry,
and non-reciprocal active matter (Fruchart–Vitelli) as the most directly aligned formalism for operators
with no Boolean shadow.

# CHARACTER WING (cdv1 projection — the continuous dynamical engine)

The structural wing develops the discrete face of the deformation; the Character wing develops the other —
the continuous economics of *being* a coherence on the graph the algebra lays down. Where the structural
reading asks what structure can be held, the Character reading asks what it costs to hold against a bath,
and traces the dynamics that carry a substrate through the $c/s/r$ migration. The amplitude coordinate is
the chit, introduced on the spine and given its full treatment here.

## The chit unit

$$\mathrm{chit} = \ln(G_0/L).$$

The logarithm is forced, not stylistic: for a process with effective forward rate $\sim G_0$ and backward
rate $\sim L$, $\ln(G_0/L)$ is the Crooks per-transition entropy production (Crooks 1999; Seifert 2012),
and threshold symmetry ($G_0 = L \Rightarrow \mathrm{chit} = 0$), additivity across independent gain
stages, and $\ln 2$-alignment with Landauer all collapse to faces of one rate-ratio structure. The
rate-ratio reading is itself the Markovian specialisation of a per-orbit one,
$\mathrm{chit}_{\mathrm{orbit}} = \oint v(\theta)/D(\theta)\,d\theta$, the continuous-orbit Schnakenberg
affinity (Schnakenberg 1976; Qian 2001), the two agreeing at $\beta_{\mathrm{mem}} = 1$ and the orbit form
canonical for non-Markovian substrates.

In a sustained NESS the saturated gain clamps to loss, $G_{\mathrm{sat}} = L$; the chit measures the
*unsaturated* excess — the headroom above threshold, not the operating point. Threshold behaviour follows
directly: chit $\gg 0$ gives $c$, chit $\to 0^+$ gives $s$, chit $< 0$ gives $r$. chit $= 0$ is a critical
limit, not an attainable state (§Asymptotic closure); the $s$-regime is a finite window around it whose
width resolves on a substrate split — drive-axis substrates carry an irreducible thermodynamic floor (the
$kT/q$ of a diode, the Schawlow–Townes broadening of a laser), while damping-axis substrates carry a
measurement-limited width that vanishes in the deterministic limit (the RLC testbed reads exactly zero at
$Q = 0.5$).

## Fraying sequence

Load monotonically reduces the chit, and the typical trajectory under load is a single sequence:

> saturated holding (chit $\gg 0$, $c$, resilient) → visible strain (chit $\to 0^+$, $s$) → mode-hopping
> (chit $\approx 0$, $s$ multistability) → sub-threshold collapse (chit $< 0$, $r$).

Mode-hopping is the laser-physics name for the multistable substructure that produces the aging plateau in
the CK-class FDR signature. That this is the *typical* path is itself a theorem: by the Crooks detailed
fluctuation theorem $P(\sigma)/P(-\sigma) = e^\sigma$, an anomalous fraying-resistance trajectory — a mode
sustaining despite the chit drop — is exponentially rare in $|\sigma|$.

## Universal two-mode kernel

The discrete composite catalogue is recovered as the fixed points of one continuous field equation, the
universal two-mode budget kernel:

$$\frac{\partial \rho_A}{\partial t} = (G_{0,A} - L_A)\rho_A - \gamma_{AB}\,\rho_A\rho_B + \mathcal{D}[\rho_A, \rho_B; \gamma_{AB}]$$

(symmetric for $\rho_B$; $\gamma_{AB} < 0$ contributes positively, matching the structural sign
convention). The non-local $\mathcal{D}$-kernel admits three increasingly general closures. The **Lamb
stationary closure** is standard multi-mode laser gain depletion (Lamb 1964; Haken 1983),
$G_{0,A}^{\mathrm{eff}} = G_{0,A}/(1 + \sum_{j\ne A}\rho_j/\rho_{\mathrm{sat}})$, with the cubic
cross-saturation as its leading expansion. The **dynamic bath inversion** promotes the bath to a
coordinate $B(t) \in [0,1]$ and projects it out by Mori–Zwanzig (Mori 1965; Zwanzig 1973), giving a
non-Markovian history integral whose fast-bath limit recovers Lamb and whose inverse bath rate
$\gamma_B^{-1}$ is the service time in the queueing mapping. The **Caputo fractional-memory** closure
replaces exponential relaxation with a Mittag-Leffler kernel
$\Gamma_{AB}(\tau) = \Gamma_0\,E_{\beta_{\mathrm{mem}}}(-(\tau/\tau_c)^{\beta_{\mathrm{mem}}})$ (Caputo
1967; Podlubny 1999; Metzler & Klafter 2000), Markovian at $\beta_{\mathrm{mem}} = 1$ and power-law for
$\beta_{\mathrm{mem}} < 1$ — the glassy signature.

The Caputo closure carries the framework's central cross-discipline coincidence. Under the *common-exponent
condition* — the substrate's slow-resource memory kernel and its load-arrival process share one
anomalous-diffusion exponent — the aging slope, the memory exponent, and the heavy-traffic queue-tail
exponent are one parameter:

$$\alpha_s = \beta_{\mathrm{mem}} = \text{anomalous heavy-traffic exponent}.$$

It composes the non-Markovian FDR (Pottier 1985), which identifies the Caputo exponent with the aging
slope, and the fractional-Brownian heavy-traffic limit (Norros 1994), which generalises $1/(1-\rho)$ to
$1/(1-\rho)^{\beta_{\mathrm{mem}}}$ — distinct substrate-side processes that coincide only under the shared
exponent. The original M/M/1 falsifier (that $\alpha_s = \tfrac12$ at $\rho \to 1$) was mis-specified, a
category error: the $\tfrac12$ is a reflected-Brownian-motion Hurst exponent in the $C$-versus-lag plane,
while $\alpha_s$ is the FDR slope in the $\chi$-versus-$C$ plane. Reframed, the prediction is that a
Markovian, reversible heavy-traffic substrate reads raw FDR slope $\approx 1$ across $\rho \to 1$ (the
clean instance is equilibrium critical slowing, which must read $X = 1$); a Markovian substrate showing
aging $X < 1$, or a non-Markovian one showing Markovian Kingman scaling, would falsify it (§Open items).

## Relaxation-oscillation register

The bridge eigenvalue's real part sets the regime; its full complex structure governs how perturbations
recover. Above threshold a single-mode coherence is two-dimensional in local linearisation (field ×
slow-resource), with a complex-conjugate pair — the relaxation-oscillation regime of laser physics. The
exact forms (Lamb closure, mpa-legal, validated to machine precision against the class-B laser Jacobian)
are

$$\gamma_{RO} = \tfrac{\gamma_s}{2}e^{\mathrm{chit}}, \quad \omega_{RO} = \sqrt{2L\gamma_s(e^{\mathrm{chit}}-1) - \tfrac{\gamma_s^2}{4}e^{2\mathrm{chit}}}, \quad Q = \sqrt{\tfrac{2L(e^{\mathrm{chit}}-1)}{\gamma_s} - \tfrac{e^{2\mathrm{chit}}}{4}}\;e^{-\mathrm{chit}},$$

with $\gamma_s$ the substrate's slow-resource turnover rate. The quality factor $Q$ is the chit-conjugate:
chit reads *whether* threshold is cleared, $Q$ reads *how many cycles* of natural oscillation the headroom
buys. It is non-monotonic — $Q \to 0$ at both chit $\to 0^+$ and chit $\to \infty$, peaking at
chit $= \ln 2$ — so a coherence is underdamped only in a mid-chit band and overdamped at both ends: the
class-B picture, where the $s$-threshold is critical *slowing* and deep $c$ damps the oscillation out, not
"many cycles deep in $c$." Probes within $\gamma_{RO}$ of $\omega_{RO}$ are $Q$-amplified (active),
off-resonance probes passive, so active-probe channel capacity peaks at intermediate headroom, not deep in
$c$. The codimension-1 bifurcations are explicit — transcritical at chit $= 0$ ($c \leftrightarrow r$),
pitchfork at $\gamma_{AB} = \gamma_c$, Hopf at obstructive-$\gamma$ onset — with codimension-2 normal forms
(Bogdanov–Takens, cusp, Bautin) in receipts §14. One open prediction follows from the mpa-legal fix to the
non-monotonic $Q$: deep in $c$, $Q \to 0$ restores direct phase-lock, so over-provisioned holdings may
collapse their multi-mode independent-memory capacity — the falsifier and a named substrate are owed
(§Open items).

## Thermodynamic and informational accounting

Stochastic thermodynamics and information theory consolidate into one dual ledger; the chit's $\ln$
structure already sits inside both. On the thermodynamic side: the Crooks detailed fluctuation theorem;
the thermodynamic-uncertainty relation $\mathrm{Var}(J)/\langle J\rangle^2 \ge 2k_B/\langle\sigma\rangle$
(Barato & Seifert 2015; Horowitz & Gingrich 2020), the framework's first explicit precision–cost
constraint; and the Schnakenberg cycle decomposition
$\langle\sigma\rangle = \sum_C J_C\ln(\prod_+ k/\prod_- k)$ (Schnakenberg 1976), which for a limit cycle
becomes $\sigma_{\mathrm{frust}} = J_{ss}\oint v/D\,d\theta$ on the orbit ring — the topological cycle
current whose affinity is drive-independent while the drive scales only $J_{ss}$. On the informational
side: predictive information $I_{\mathrm{pred}} = I(\mathrm{past};\mathrm{future})$ (Bialek, Nemenman &
Tishby 2001), a third coherence observable beside chit and $Q$; active-probe channel capacity
$C \sim \gamma_{RO}\log_2(1 + Q)$; and the extended second law $\langle\sigma\rangle \ge -\Delta I$ (Sagawa
& Ueda 2010), by which bit-readout holdings sustain at lower chit by paying in mutual information. The
per-event bit/chit correspondence and the dual-ledger table are on the spine; the apparatus is here — the
entropy-production, TUR, Schnakenberg, and predictive-information rows being the per-row
thermodynamic↔informational measurements.

The coupling row's derivation is the **optimal-encoding coincidence** (posit P5). The Still prediction bound
(Still, Sivak, Bell & Crooks 2012) gives $\langle\sigma\rangle - \langle\sigma\rangle_{\min} \ge
\gamma_s\,\chi$ with $\chi = C_\mu - I_{\mathrm{pred}}$ the cryptic order ($C_\mu$ the $\varepsilon$-machine
structural complexity; Crutchfield 1989; Shalizi & Crutchfield 2001), equality at the
rate-distortion-optimal limit. The same $\chi$ surfaces as encoding overhead and as dissipation excess —
one quantity, $\chi = \Delta_n = \langle\sigma\rangle_{\mathrm{excess}}/\gamma_s$, in three registers — and
only at that limit. A substrate whose $I_{\mathrm{pred}}$ scaling deviates from its thermodynamic dual would falsify it (§Open
items); whether the dual *mapping* is itself substrate-independent stays expository (§Open items › Open
conjectures).

## Adoption catalogue

Ten cross-framework registers were adopted into the Character projection. Each row gives the borrowed
register, the one-phrase MPA mapping, the observable that survives substrate-stripping, its falsifier, and
the receipts entry holding the apparatus. As with the composite catalogue, per row MPA supplies a unifying
mapping; per table, one regime-and-kernel rule-set generates these phenomena across fields with no shared
microphysics.

| Register | MPA mapping | Load-bearing observable | Falsifier | Receipts |
|---|---|---|---|---|
| Damping / resonance | RO trichotomy = $c/s/r$ damping shadow | $\gamma_{RO}, \omega_{RO}, Q$ | mpa-legal landed | §13 |
| Attractor classification | regimes ↔ attractor types | per-regime attractor | — | §14 |
| Synchronization | $\gamma_{AB}$ sign → in/anti-phase lock; $K_{AB} \propto (1+4Q^2)^{-1/2}$ | two independent transitions (chit-onset, Kuramoto $K_c$); collective $r$; chimera | only uniform sync/incoherence accessible | §15 |
| Nonequilibrium thermo | holdings are trajectory-NESS | $\langle\sigma\rangle$, Schnakenberg affinity, TUR-tightness $T$ | same-class arbitrary $T$ | §16 |
| Information theory | thermo↔info dual ledger | $I_{\mathrm{pred}}$, channel capacity, cryptic order $\chi$ | $I_{\mathrm{pred}}$ scaling breaks the dual | §17 |
| Self-organized criticality | chit-zero = SOC attractor; Galton–Watson $\mu = e^{\mathrm{chit}}$ | avalanche $\tau \approx 3/2$; branching $\to 1$ at $\epsilon = 1$ | stable $\tau \ne 3/2$, or branching $\ne 1$ at $\epsilon = 1$ | §18 |
| Dissipative structures | chit-zero crossing = Prigogine formation; chit = Haken order parameter | Turing wavelength | Turing three-condition failure | §9, §19 |
| Control theory | holding = plant + controller loop; internal-model principle | four-axis observable; $k_{\text{frust}}$ admits no gradient Lyapunov | habit-extinction Caputo $\beta_{\mathrm{mem}} < 1$, or $W$ off the P3 form | §17, §20 |
| Active matter | holdings = active-matter units | active-stress fingerprint; MIPS | high-Pe clustering at $\gamma_{AB} \ge 0$ without swim-pressure | §21 |
| Queueing | holdings are queues: chit $= -\ln\rho$; $c/s/r$ ↔ stable / heavy-traffic / unstable | heavy-traffic $= s$-aging; $\epsilon \leftrightarrow u$ | Markovian-reversible substrate showing aging $X < 1$ | §5, §22 |

Four claims are too heavy for a row. The **four-aspect Complexity Wall**: at $\epsilon = 1$, thermodynamic
(cumulative-mass divergence), dynamical (meta-ledger flow bifurcation), informational (compression rate
→ 1), and SOC-critical (branching ratio → 1) signatures coincide, with $\beta_{\mathrm{mem}} \approx
1-\epsilon$ the unifying parameter; for sub-optimal encoding the aspects split, the thermodynamic and SOC
reaching criticality first via $u \to 1$ — sub-optimal substrates die thermodynamically before
informationally. The **regime ontology**: $s$ is the *generic* attractor of feedback-coupled NESS, not the
unstable middle of a triplet ($c$ over-provisioned, $r$ post-collapse), which is why $s$ is empirically
over-represented. **Heavy-traffic $= s$-aging**: Kingman's $\langle Q\rangle \sim (1-\rho)^{-1}$ divergence
is the $s$-aging signature in the queueing register, the FDR aging exponent and the queue-tail exponent
being one phenomenon — coincident for Markovian, divergent for non-Markovian, the divergence itself the
substrate-class diagnostic. And the **active-stress / MIPS fingerprint** $\alpha_\Sigma/\alpha_\sigma \sim
v_0^2\tau_R/D_{\mathrm{trans}}$, with motility-induced phase separation giving clustering at $\gamma_{AB}
\ge 0$ — a mechanism absent from the two-mode kernel.

## Five leading-order posits

Five primitives share one four-part shape: a simplest functional form placing the primitive at its
critical or optimal limit; a substrate-conditional deviation; a falsifier; and a substrate-thermodynamic
derivation left as a receipts-only residual. Universality fixes the form (the exponents); substrates fix
the amplitudes (the deviations) — renormalization-group language. Each is testable, none derived from
substrate thermodynamics, and closing the derivation for a substrate class is the canonical extension mode
rather than a defect.

| # | Posit | Carried by | Receipts | Predicted measurement |
|---|---|---|---|---|
| P1 | $\beta_{\text{mem}} \approx 1-\epsilon$ | §Adoption (Wall) | §9 | $\beta_{\text{mem}}(\epsilon)$ linear to leading order, both endpoints respected |
| P2 | $\mu = e^{\text{chit}}$ | §Adoption (SOC) | §18 | avalanche branching tracks $e^{\text{chit}}$; $\tau \approx 3/2$ at chit $= 0$ |
| P3 | $w_i = \gamma_{\text{ref}}/\gamma_{s,i}$ | §Adoption (control) | §20 | substrate-native weights inverse-scale with $\gamma_{s,i}$ |
| P4 | $u_n = \epsilon_n$ | §Adoption (queueing) | §22 | at rate-distortion-optimal encoding, $u_n - \epsilon_n \to 0$ |
| P5 | $\chi = \Delta_n$ | §Thermo-info accounting | §20 | $C_\mu - I_{\text{pred}} = u_n - \epsilon_n = \langle\sigma\rangle_{\text{excess}}/\gamma_s$ |

## Cross-register structure

The same primitives surface across registers, and the relationships among those appearances sort into
three kinds — **correspondences** (one quantity or structure appearing in several registers, with the
binding condition stated), **relations** (one thing forcing or coupling another), and **decompositions**
(things that are irreducibly independent). The discipline is to state the *epistemic status* of each link,
because the easy error is to read a coincidence-under-a-condition or an equality-at-a-limit as an
ontological identity. The posits thread through them — each link that *is* or *follows from* a posit names
it.

**Cross-register correspondences.** *Parameter coincidences* — one scalar measured through several
protocols, equal under a stated condition or at a limit, not by definition. The **$\beta_{\mathrm{mem}}$
coincidence** (controlling posit $\beta_{\mathrm{mem}} \approx 1-\epsilon$): under the common-exponent
condition the aging slope, the Caputo memory exponent, and the anomalous heavy-traffic exponent are the
same number — a composition of Pottier and Norros, not a definitional identity, and falsified where the
exponents are measured to differ — and that parameter propagates through seven registers (the memory tail,
the Green–Kubo $\tau_R$ divergence, the swim-pressure fingerprint, the Kelly product-form breakdown, the
Wall-coupling posit, the variable-ratio extinction tail, and the traffic-to-frozen-topological transition
via $\ell_c$). The **optimal-encoding coincidence** is posit $\chi = \Delta_n$ (riding $u_n = \epsilon_n$):
cryptic order, encoding overhead, and dissipation excess coincide *at the rate-distortion-optimal limit* —
an equality at a limit, not an identity — and sub-optimal substrates split them (and split the four-aspect
Wall). *Structural correspondences* — one structure realized as genuinely distinct objects in different
registers; the framework maps the shared structure, it does not claim the realizations are the same
object. The **mentor-row dual face**: one non-reciprocal coupling realized as a temporal limit cycle
($\omega_{\mathrm{pq}}$) or a spatial Turing pattern ($k_c$) — distinct objects in different function
spaces, sharing the coupling asymmetry, with substrate spatial structure selecting. The
**$k_{\mathrm{frust}}$ topological correspondence**: one topological excision (no $P_{ss}$ in the region)
with three co-implied consequences — dynamical (no fixed point), information-geometric (a homotopy
obstruction), thermodynamic (a forced Schnakenberg current) — equivalent at the abstract level, distinct
measurement protocols in practice. The **plant–controller correspondence**: one closed loop read as an
active probe, as SOC self-tuning, and as Haken slaving. *Universality coincidence* — the **Galton–Watson
dual register** (posit $\mu = e^{\mathrm{chit}}$): one mean-field class ($\tau = 3/2$) at two framework
limits, horizontal ($\mu \to 1$ at chit $= 0$) and vertical (tower branching $\to 1$ at $\epsilon = 1$),
with substrate-graph dimensionality fixing the empirical exponent.

**Cross-register relations.** Not coincidences but forcings and couplings between distinct objects.
**Wall-forces-NRT** (a consequence of posit $u_n = \epsilon_n$): the Cobham wait diverges at $u_n \to
1^-$, forcing a generic Hopf at every tower-ascent, and $N \ge 3$ ascents complete the 3-torus for
Newhouse–Ruelle–Takens chaos — so meta-ledger chaos past the Wall is *forced*, not merely allowed,
contingent on $r$-collapse not preceding the sequence and on the Cobham–Haken bridge conditions.
**r-coupling of heat-tax channels 2 and 3**: they share $r$ as driver in opposing directions (channel 2 as
$1 + Cr^2$, channel 3 as $r$-drop sync degradation), with the active-coupling sign $C$ setting the
balance.

**Decompositions.** Assertions of irreducible independence — the opposite of a correspondence. **Three spatial
mechanisms**: Turing reaction–diffusion, Kelly queueing-congestion, and frozen-topological at
$\beta_{\mathrm{mem}} \to 0$ have distinct prerequisites and do not reduce to one another; a substrate may
carry one, two, or all three at different scales. **Four-channel pattern selection**: multi-mode
($N \ge 3$) emergence routes through four independent tests — frustration, spectral sync (generalised
master-stability, mild-heterogeneity scope), non-reciprocity, and active-matter overlay (direct for
active-matter substrates) — the operating system for $N \ge 3$ structure.

Two parameter trialities (optimal-encoding, $\beta_{\mathrm{mem}}$) and two structural trialities
($k_{\mathrm{frust}}$, plant–controller) share a "one thing, three readings" shape; the rhyme is
presentational, not a further claim. The auto-tuning weight posit $w_i = \gamma_{\mathrm{ref}}/\gamma_{s,i}$
has no coincidence partner and stays under the posits.

# Open items

The framework's predictions awaiting empirical contact, the pieces of pipeline owed before some verdicts
can be adjudicated, and the architectural conjectures that are not yet framework content. (The
structural-projection conjectures — the codimension-$N$ Boolean-singularity question, the deferred
transfer-operator and latent-ledger operators — live in their homes in the structural wing.)

## Live falsifiers

Each is a named falsifier substrate with a predicted measurement, formalised in receipts.

- **Surface-code $s \to r$ migration** as the gFDR cross-substrate test — the primary positive instance
  (Receipts §4).
- **Habit-extinction** Caputo $\beta_{\mathrm{mem}} < 1$ on variable-ratio reinforcement schedules
  (Receipts §20).
- **Avalanche $\tau \approx 3/2$** on a feedback-coupled NESS with separable timescales — apparatus
  validated on critical Galton–Watson and RFIM (Receipts §18).
- **Meta-ledger branching ratio $= 1$ at $\epsilon = 1$** in any observable hierarchical NESS substrate
  (Receipts §18).
- **Strange-attractor / chaotic Character dynamics** on any substrate crossing $\epsilon \ge 1$ (Receipts
  §14).
- **MIPS clustering at $\gamma_{AB} \ge 0$** in high-Péclet substrates (Receipts §21).
- **Chimera-state instancing** under the spectral (SBN) test (Receipts §15).
- **TUR-tightness as a substrate-class universality** (Receipts §16).
- **$I_{\mathrm{pred}}$ scaling** with chit, $Q$, and internal-model richness across substrate classes —
  also the falsifier for the bit/chit dual ledger if a substrate breaks the per-row correspondence
  (Receipts §17/§20).
- **Heavy-traffic exponent vs $\alpha_s$** on Markovian and non-Markovian substrates — the reframed M/M/1
  falsifier (Receipts §22).
- **Substrate-class hard-vs-soft capacity walls** (Receipts §5/§22).
- **Turing three-condition refinement** — non-reciprocity, autocatalysis, differential diffusion (Receipts
  §19).
- **Memory-exponent collapse near the Wall**, $\beta_{\mathrm{mem}} \approx 1-\epsilon$ (Receipts §9).
- **Auto-tuning inverse-form** $w_i = \gamma_{\mathrm{ref}}/\gamma_{s,i}$ on substrates requiring diagonal
  stability (Receipts §20).
- **Common-exponent condition** for the $s$-regime exponent coincidence — falsified by substrate classes
  where the FDR and queue-tail exponents are measured to differ.
- **Cobham–Haken bridge conditions** — three substrate-side conditions, each with its own falsifier.
- **Deep-$c$ phase-lock collapse** / multi-mode memory-capacity loss, raised by the mpa-legal fix to the
  non-monotonic $Q$; falsifier and named substrate owed.

## Owed work (pipeline)

Pieces of the measurement pipeline owed before certain verdicts can be credited. Until they land, no result
that traverses the conform/inversion pipeline is carried as valid evidence — the trustworthy layer is the
pre-conform direct simulation validated against exact analytical forms (the two-frame gFDR bricks,
rotational-OU, the class-B-laser Jacobian).

- **Five-vector inversion** ($q_{EA}, \tau_\alpha, \beta_{\mathrm{KWW}}, \tau_\beta, X$): a first-cut
  fitter recovers $X$ on `two_temp_ou` to ~1–2%, but until it lands and is integrated, $X$-bearing verdicts
  read at the raw FDR-locus-slope layer.
- **Domain-of-validity gate** on the conform pipeline: pure oscillation currently reads as `s_critical`
  with no gating; awaits the five-vector fitter absorbing valid-aging residuals before a residual threshold
  can isolate out-of-domain cases.
- **Underdamped/oscillatory inversion**: conform clamps to deep-$r$ on class-B laser ringing; adjudicate
  alongside the domain gate.
- **Auditor layer never exercised on controls**: once inversion carries $X$, push a control cell through
  the auditor and check the regime story.
- **$\varepsilon$-machine stationarity-gap criterion**: the substrate-thermodynamic derivation separating
  the trajectory-ensemble-local-stationarity reading from the time-varying one.
- **Two-frame velocity-frame closure + real-substrate contract**: the two conjugate FDR frames rest
  on verdict-agreement; the exact cross-frame magnitude identity
  $V_{ext} = \langle\sigma\rangle = J\!\cdot\!\mathcal{A}$ is owed to the velocity-frame Harada–Sasa
  integral. The apparatus runs on a nonlinear topologically-forced limit cycle (`banach_active_ring.py`),
  but a real §846-clearing instance needs author-collected active-lattice data — the public deposits lack
  the perturbation-response protocol and carry friction-dominated $\mathrm{Var}(J)$.
- **Deformation-calculus series**: the explicit $1/D$ operator expansion — associator, distributivity
  defect, and Boolean deviation as trail-vector functionals — beyond the leading defect bounds. The
  derivation chain is currently unrecovered in receipts, so the structural wing states bounds, not a
  closed-form series.

## Open conjectures (research notes, not framework content)

- **$k_{\mathrm{frust}}$ as a second primitive axis.** The R1/R2/R3 ladder survived on a synthetic 3-cycle;
  elevation to a numbered primitive is earned only by a real cross-substrate instance exercising
  drive-independent NESS circulation, chirality conservation under a chirality-preserving transformation,
  and the three triality registers measuring the same thing. The candidate class is active non-reciprocal
  metamaterials wired into Harary-frustrated loops (Veenstra/Coulais rings, Bartolo active hydraulics); the
  bottleneck is data, not physics.
- **$k_{\mathrm{frust}}$ topology-floor posit.** A functional form tying the smallest-cycle-affinity floor
  to graph topology is not yet committed.
- **$k_{\mathrm{frust}}$ information-native characterisation.** Currently native to the dynamical and
  differential-geometric registers; a substrate-independent information-native characterisation (candidate:
  a topological mutual information surviving detailed-balance restoration) is owed.
- **Bilingual register as a structural-universality claim.** That the bit/chit dual *mapping* is itself
  substrate-independent needs a test independent of the per-row falsifier; until then it is expository
  organisation, not framework content.
- **Substrate-transformation classification** (chirality-preserving / chirality-flipping / axis-mixing).
  Two entries already live in their homes — the Markovian $\gamma$-sign inversion and the strong-chaos Wall
  round-trip; three further candidates are future work.

---

# Appendices

## Appendix — Principles and working method

Two preambles govern how the framework is built and tested: five architectural commitments that constrain
the protocol architecture, and seven methodological imperatives that govern the conduct of falsification.
Neither constrains the operator algebra or the capacity claims of the body, which sit upstream of the
protocol layer; they are collected here, out of the way of the framework itself. The commitments'
long-form treatment is the [Architectural Block-In](../architecture/MPA_Architectural_Block-In.md)
§"Foundational principles (consolidated)".

**Architectural commitments.**

1. **Color-management discipline.** Three layers — substrate-native, canonical representation,
   realizer-output — with declared, named, versioned, swappable transforms between them. The canonical
   representation is substrate-neutral by construction.
2. **Observer-driven scale management.** $\tau_{obs}$ is the camera. The canonical representation is
   observer-relative; cross-scale composition is camera motion, not transform invocation. No scale-class
   taxonomy is baked into the framework; §Scale-relativity is the operational consequence.
3. **Demand-bounded sufficiency.** The framework commits to *enough* representation for the demand placed
   on it, not maximal faithfulness to substrate. Drivers declare a demand envelope; the canonical
   representation is sized to it; past the envelope the framework is silent. MPA is not the bottleneck on
   substrate fidelity.
4. **Singular working-space path.** Within a version, exactly one canonical-representation shape.
   Plurality lives in drivers, realizer-interface intent flags, and version succession — never at the
   working-space layer. *Peel*, not scrape.
5. **Thin-RFC discipline.** Exchange surfaces are written at gross-underengineering resolution by design;
   this paper carries the rigor underneath, the RFCs carry the contract. *It was never brittle if it never
   broke.* (Governs the RFCs, not this paper.)

The five are coupled. They constrain the RFC sequence and the driver/realizer architecture; they do not
constrain the operator algebra or capacity claims of the body, which are upstream of the protocol layer.

**Methodological imperatives.**

- **Trajectory primacy.** The primitives are NESS observables defined on bounded time-series of sustained
  holding, not static point measurements.
- **NESS-by-default.** Detailed-balance breaking is the foundational baseline; equilibrium is the
  degenerate (zero-drive) special case. The framework does not specialise NESS theory to near-equilibrium;
  equilibrium specialises NESS theory to detailed balance.
- **mpa-legal.** Every dynamical quantity — rate, coupling, response, current — must *flow with the
  operating point* unless the physics explicitly says otherwise. A constant frozen where the physics
  requires flow is illegal; the audit has caught two such cases (Receipts §13 / §Topological-drain
  mpa-LEGAL audit).
- **Falsifier discipline.** Each claim states a predicted measurement on a named substrate or substrate
  class, with the kill condition formalised in receipts and surveyed in §Open items. Surface-code
  $s$-aging is the load-bearing positive instance; the rest are predictions awaiting empirical contact.
- **Goalpost-optic.** A refinement made during a falsification campaign must shrink the falsifiable
  surface, not enlarge it. Survival is the operative verdict.
- **Reading rules inherit across projections.** Substrate-conditional sign caveats (the Markovian
  $\gamma$-sign inversion; detection-event preprocessing) apply identically to both readings
  (§Substrate-conditional reading rules).
- **API surface, not closed theory.** The five leading-order posits (Character wing) encode the
  framework's API: each places a primitive at its critical limit via the simplest natural form;
  substrate-thermodynamic derivation of the exact functional shapes is the canonical extension mode, not
  a defect of the present state.

## Appendix — Formal derivations

The formal derivations behind the claims above — the Erlang-B closure of the cross-saturation efficiency,
the Landauer pin of the heat-tax conductivity, the three $\mathcal{D}$-kernel closures, the
relaxation-oscillation parameters, the Wall-forces-NRT chain, the Schnakenberg cycle decomposition, the
Galton–Watson critical-branching closure, and the rest — are line-keyed in
[`mpav1_receipts.md`](mpav1_receipts.md), each entry tagged by citation, bespoke step, verification, and open
residual. This paper names the imported source at each step; the receipts carry the working.

---

# References

The framework imports established results and reads them under sustained dissipation; the prior art falls
into nine bodies of work, named inline throughout and collected here — the thermodynamics of inference and
computation (Landauer, Bennett, Sagawa–Ueda, Sekimoto, Seifert); driven-dissipative threshold structure
(Sieberer–Buchhold–Diehl, Haken); aging fluctuation–dissipation theory (Cugliandolo–Kurchan,
Crisanti–Ritort); capacity and constraint-satisfaction thresholds (Amit–Gutfreund–Sompolinsky,
Mézard–Parisi–Zecchina and collaborators, Krzakala et al.); spin-glass and energy-landscape mathematics
(Mézard–Parisi–Virasoro, Wolynes–Onuchic–Thirumalai); renormalization-group structure (Wilson, Kadanoff,
Cardy); catastrophe and non-reciprocal-active-matter landscape mathematics (Thom, Arnold, Fruchart et al.);
composite-pairing prior art (Hebb, Frey–Morris, Lotka, Volterra, Kuramoto, Strogatz, Miller,
Rescorla–Wagner); and surface-code thermodynamics and decoders (Dennis–Kitaev–Landahl–Preskill, Gidney,
Bausch et al.). Nine citations appear in both projections — Landauer, Sagawa–Ueda, Seifert,
Cugliandolo–Kurchan, Crisanti–Ritort, Fruchart et al., Kuramoto, Strogatz, Rescorla–Wagner — marking prior
art shared by the structural and Character readings.

Abrams, D. M., & Strogatz, S. H. (2004). Chimera states for coupled oscillators. *Physical Review Letters*, 93, 174102.

Amari, S., & Nagaoka, H. (2000). *Methods of Information Geometry*. American Mathematical Society / Oxford University Press.

Amit, D. J., Gutfreund, H., & Sompolinsky, H. (1985). Spin-glass models of neural networks. *Physical Review A*, 32, 1007.

Arnold, V. I. (1992). *Catastrophe Theory*. Springer.

Åström, K. J., & Murray, R. M. (2008). *Feedback Systems: An Introduction for Scientists and Engineers*. Princeton University Press.

Bak, P. (1996). *How Nature Works: The Science of Self-Organized Criticality*. Copernicus / Springer.

Bak, P., Tang, C., & Wiesenfeld, K. (1987). Self-organized criticality: An explanation of the 1/f noise. *Physical Review Letters*, 59, 381.

Barato, A. C., & Seifert, U. (2015). Thermodynamic uncertainty relation for biomolecular processes. *Physical Review Letters*, 114, 158101.

Bausch, J., et al. (2024). AlphaQubit. *Nature*.

Beggs, J. M., & Plenz, D. (2003). Neuronal avalanches in neocortical circuits. *Journal of Neuroscience*, 23, 11167–11177.

Bennett, C. (1982). *International Journal of Theoretical Physics*, 21, 905.

Bialek, W., Nemenman, I., & Tishby, N. (2001). Predictability, complexity, and learning. *Neural Computation*, 13, 2409–2463.

Bogdanov, R. I. (1975). Versal deformations of a singular point on the plane in the case of zero eigenvalues. *Functional Analysis and Its Applications*, 9, 144–145.

Brady, J. F. (2014). The swim force. Plenary lecture, *American Physical Society DFD*.

Braunstein, A., Mézard, M., & Zecchina, R. (2005). Survey propagation: An algorithm for satisfiability. *Random Structures & Algorithms*, 27, 201.

Burke, P. J. (1956). The output of a queueing system. *Operations Research*, 4, 699–704.

Caputo, M. (1967). Linear models of dissipation whose Q is almost frequency independent. *Geophysical Journal International*, 13, 529–539.

Cardy, J. (1996). *Scaling and Renormalization in Statistical Physics*. Cambridge University Press.

Cates, M. E., & Tailleur, J. (2015). Motility-induced phase separation. *Annual Review of Condensed Matter Physics*, 6, 219–244.

Cobham, A. (1954). Priority assignment in waiting line problems. *Operations Research*, 2, 70–76.

Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley.

Crisanti, A., & Ritort, F. (2003). Violation of the fluctuation-dissipation theorem in glassy systems: basic notions and the numerical evidence. *Journal of Physics A: Mathematical and General*, 36, R181.

Crooks, G. E. (1999). Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences. *Physical Review E*, 60, 2721.

Crutchfield, J. P. (1989). Inferring statistical complexity. *Physical Review Letters*, 63, 105.

Crutchfield, J. P., Ellison, C. J., & Mahoney, J. R. (2009). Time's barbed arrow: irreversibility, crypticity, and stored information. *Physical Review Letters*, 103, 094101.

Cugliandolo, L. F., & Kurchan, J. (1993). Analytical solution of the off-equilibrium dynamics of a long-range spin-glass model. *Physical Review Letters*, 71, 173.

Dennis, E., Kitaev, A., Landahl, A., & Preskill, J. (2002). Topological quantum memory. *Journal of Mathematical Physics*, 43, 4452.

Doi, M. (1976). Second quantization representation for classical many-particle system. *Journal of Physics A: Mathematical and General*, 9, 1465.

Erlang, A. K. (1917). Solution of some problems in the theory of probabilities of significance in automatic telephone exchanges. *The Post Office Electrical Engineers' Journal*, 10, 189–197.

Ermentrout, G. B., & Terman, D. H. (2010). *Mathematical Foundations of Neuroscience*. Springer.

Fily, Y., & Marchetti, M. C. (2012). Athermal phase separation of self-propelled particles with no alignment. *Physical Review Letters*, 108, 235702.

Fowler, A. G., Mariantoni, M., Martinis, J. M., & Cleland, A. N. (2012). Surface codes: Towards practical large-scale quantum computation. *Physical Review A*, 86, 032324.

Francis, B. A., & Wonham, W. M. (1976). The internal model principle of control theory. *Automatica*, 12, 457–465.

Frey, U., & Morris, R. G. M. (1997). Synaptic tagging and long-term potentiation. *Nature*, 385, 533.

Fruchart, M., Hanai, R., Littlewood, P. B., & Vitelli, V. (2021). Non-reciprocal phase transitions. *Nature*, 592, 363–369.

Galton, F., & Watson, H. W. (1875). On the probability of the extinction of families. *Journal of the Anthropological Institute*, 4, 138–144.

Gidney, C. (2021). Stim. *Quantum*, 5, 497.

Goh, B. S. (1977). Global stability in many-species systems. *American Naturalist*, 111, 135–143.

Guckenheimer, J., & Holmes, P. (1983). *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields*. Springer.

Haken, H. (1983). *Synergetics: An Introduction* (3rd ed.). Springer.

Haken, H. (1985). *Laser Light Dynamics*. North-Holland.

Harada, T., & Sasa, S. (2005). Equality connecting energy dissipation with a violation of the fluctuation-response relation. *Physical Review Letters*, 95, 130602.

Harary, F. (1953). On the notion of balance of a signed graph. *Michigan Mathematical Journal*, 2, 143–146.

Harris, T. E. (1963). *The Theory of Branching Processes*. Springer.

Hebb, D. O. (1949). *The Organization of Behavior*. Wiley.

Hofbauer, J., & Sigmund, K. (1998). *Evolutionary Games and Population Dynamics*. Cambridge University Press.

Hopfield, J. J. (1982). Neural networks and physical systems with emergent collective computational abilities. *Proceedings of the National Academy of Sciences*, 79, 2554–2558.

Horowitz, J. M., & Gingrich, T. R. (2020). Thermodynamic uncertainty relations constrain non-equilibrium fluctuations. *Nature Physics*, 16, 15–20.

Jackson, J. R. (1957). Networks of waiting lines. *Operations Research*, 5, 518–521.

Kadanoff, L. P. (1966). *Physics*, 2, 263.

Kelly, F. P. (1979). *Reversibility and Stochastic Networks*. Wiley.

Kingman, J. F. C. (1962). On queues in heavy traffic. *Journal of the Royal Statistical Society B*, 24, 383–392.

Kitaev, A. Y. (2003). Fault-tolerant quantum computation by anyons. *Annals of Physics*, 303, 2–30.

Kleinrock, L. (1976). *Queueing Systems, Volume II: Computer Applications*. Wiley.

Krzakala, F., Montanari, A., Ricci-Tersenghi, F., Semerjian, G., & Zdeborová, L. (2007). Gibbs states and the set of solutions of random constraint satisfaction problems. *Proceedings of the National Academy of Sciences*, 104, 10318.

Kuramoto, Y. (1984). *Chemical Oscillations, Waves, and Turbulence*. Springer.

Kuramoto, Y., & Battogtokh, D. (2002). Coexistence of coherence and incoherence in nonlocally coupled phase oscillators. *Nonlinear Phenomena in Complex Systems*, 5, 380–385.

Kuznetsov, Y. A. (2004). *Elements of Applied Bifurcation Theory* (3rd ed.). Springer.

Lamb, W. E. (1964). Theory of an optical maser. *Physical Review*, 134, A1429.

Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5, 183–191.

Lazarides, N., & Tsironis, G. P. (2015). Superconducting metamaterials. *Physics Reports*, 752, 1–67.

Leland, W. E., Taqqu, M. S., Willinger, W., & Wilson, D. V. (1994). On the self-similar nature of Ethernet traffic. *IEEE/ACM Transactions on Networking*, 2, 1–15.

Little, J. D. C. (1961). A proof for the queueing formula: L = λW. *Operations Research*, 9, 383–387.

Lotka, A. J. (1925). *Elements of Physical Biology*. Williams & Wilkins.

Mackey, M. C., & Glass, L. (1977). Oscillation and chaos in physiological control systems. *Science*, 197, 287–289.

Mainardi, F. (2010). *Fractional Calculus and Waves in Linear Viscoelasticity*. Imperial College Press.

Marchetti, M. C., Joanny, J. F., Ramaswamy, S., Liverpool, T. B., Prost, J., Rao, M., & Simha, R. A. (2013). Hydrodynamics of soft active matter. *Reviews of Modern Physics*, 85, 1143.

Metzler, R., & Klafter, J. (2000). The random walk's guide to anomalous diffusion: a fractional dynamics approach. *Physics Reports*, 339, 1–77.

Mézard, M., Parisi, G., & Virasoro, M. A. (1987). *Spin Glass Theory and Beyond*. World Scientific.

Mézard, M., Parisi, G., & Zecchina, R. (2002). Analytic and algorithmic solution of random satisfiability problems. *Science*, 297, 812.

Mézard, M., Ricci-Tersenghi, F., & Zecchina, R. (2003). Two solutions to diluted p-spin models and XORSAT problems. *Journal of Statistical Physics*, 111, 505.

Miller, N. E. (1944). Experimental studies of conflict. In *Personality and the Behavior Disorders*. Ronald Press.

Mittag-Leffler, G. (1903). Sur la nouvelle fonction $E_\alpha(x)$. *Comptes Rendus de l'Académie des Sciences*, 137, 554–558.

Mori, H. (1965). Transport, collective motion, and Brownian motion. *Progress of Theoretical Physics*, 33, 423–455.

Murray, J. D. (2003). *Mathematical Biology* (3rd ed.). Springer.

Newhouse, S., Ruelle, D., & Takens, F. (1978). Occurrence of strange Axiom-A attractors near quasi-periodic flows on $T^m$, $m \ge 3$. *Communications in Mathematical Physics*, 64, 35–40.

Nicolis, G., & Prigogine, I. (1989). *Exploring Complexity*. W. H. Freeman.

Norros, I. (1994). A storage model with self-similar input. *Queueing Systems*, 16, 387–396.

Parrondo, J. M. R., Horowitz, J. M., & Sagawa, T. (2015). Thermodynamics of information. *Nature Physics*, 11, 131–139.

Pecora, L. M., & Carroll, T. L. (1998). Master stability functions for synchronized coupled systems. *Physical Review Letters*, 80, 2109.

Peliti, L. (1985). Path integral approach to birth-death processes on a lattice. *Journal de Physique*, 46, 1469–1483.

"Phases of decodability in the surface code with unitary errors." (2024). *arXiv:2411.05785*.

Pikovsky, A., Rosenblum, M., & Kurths, J. (2001). *Synchronization: A Universal Concept in Nonlinear Sciences*. Cambridge University Press.

Podlubny, I. (1999). *Fractional Differential Equations*. Academic Press.

Pottier, N. (1985). Aging properties of an anomalously diffusing particle. *Physica A: Statistical Mechanics and its Applications*, 317, 371–382.

Prigogine, I., & Nicolis, G. (1977). *Self-Organization in Nonequilibrium Systems*. Wiley.

Qian, H. (2001). Mesoscopic nonequilibrium thermodynamics of single macromolecules and dynamic entropy-energy compensation. *Physical Review E*, 65, 016102.

Ramaswamy, S., Simha, R. A., & Toner, J. (2003). Active nematics on a substrate: giant number fluctuations and long-time tails. *Europhysics Letters*, 62, 196.

Redheffer, R. (1985). Volterra multipliers I. *SIAM Journal on Algebraic Discrete Methods*, 6, 592–611.

Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian conditioning: Variations in the effectiveness of reinforcement and nonreinforcement. In A. H. Black & W. F. Prokasy (Eds.), *Classical Conditioning II: Current Research and Theory* (pp. 64–99). Appleton-Century-Crofts.

Ruelle, D., & Takens, F. (1971). On the nature of turbulence. *Communications in Mathematical Physics*, 20, 167–192.

Sagawa, T., & Ueda, M. (2010). Generalized Jarzynski equality under nonequilibrium feedback control. *Physical Review Letters*, 104, 090602.

Schnakenberg, J. (1976). Network theory of microscopic and macroscopic behavior of master equation systems. *Reviews of Modern Physics*, 48, 571.

Seifert, U. (2012). Stochastic thermodynamics, fluctuation theorems and molecular machines. *Reports on Progress in Physics*, 75, 126001.

Sekimoto, K. (2010). *Stochastic Energetics*. Springer.

Sethna, J. P., Dahmen, K. A., & Myers, C. R. (2001). Crackling noise. *Nature*, 410, 242–250.

Shalizi, C. R., & Crutchfield, J. P. (2001). Computational mechanics: pattern and prediction, structure and simplicity. *Journal of Statistical Physics*, 104, 817–879.

Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27, 379–423, 623–656.

Shannon, C. E. (1959). Coding theorems for a discrete source with a fidelity criterion. *IRE National Convention Record*, 7, 142–163.

Sieberer, L. M., Buchhold, M., & Diehl, S. (2016). Keldysh field theory for driven open quantum systems. *Reports on Progress in Physics*, 79, 096001.

Siegman, A. E. (1986). *Lasers*. University Science Books.

Solon, A. P., Stenhammar, J., Wittkowski, R., Kardar, M., Kafri, Y., Cates, M. E., & Tailleur, J. (2015). Pressure and phase equilibria in interacting active Brownian spheres. *Physical Review Letters*, 114, 198301.

Sontag, E. D. (2003). Adaptation and regulation with signal detection implies internal model. *Systems & Control Letters*, 50, 119–126.

Stauffer, D., & Aharony, A. (1992). *Introduction to Percolation Theory* (2nd ed.). Taylor & Francis.

Still, S., Sivak, D. A., Bell, A. J., & Crooks, G. E. (2012). Thermodynamics of prediction. *Physical Review Letters*, 109, 120604.

Strogatz, S. H. (2003). *Sync: The Emerging Science of Spontaneous Order*. Hyperion.

Sun, J., Bollt, E. M., & Nishikawa, T. (2009). Master stability functions for coupled nearly identical dynamical systems. *Europhysics Letters*, 85, 60011.

Sutton, R. S., & Barto, A. G. (1998). *Reinforcement Learning: An Introduction*. MIT Press.

Takatori, S. C., & Brady, J. F. (2014). Swim stress, motion, and deformation of active matter. *Physical Review Letters*, 113, 028103.

Takens, F. (1974). Singularities of vector fields. *Publications Mathématiques de l'IHÉS*, 43, 47–100.

Takeuchi, Y. (1996). *Global Dynamical Properties of Lotka–Volterra Systems*. World Scientific.

Thom, R. (1972). *Structural Stability and Morphogenesis*. Benjamin.

Tinsley, M. R., Nkomo, S., & Showalter, K. (2012). Chimera and phase-cluster states in populations of coupled chemical oscillators. *Nature Physics*, 8, 662–665.

Toner, J., & Tu, Y. (1995). Long-range order in a two-dimensional dynamical XY model: how birds fly together. *Physical Review Letters*, 75, 4326.

Toner, J., & Tu, Y. (1998). Flocks, herds, and schools: A quantitative theory of flocking. *Physical Review E*, 58, 4828.

Turing, A. M. (1952). The chemical basis of morphogenesis. *Philosophical Transactions of the Royal Society B*, 237, 37–72.

Volterra, V. (1926). *Memorie della Reale Accademia dei Lincei*, 2, 31.

Weiss, C. O., & Vilaseca, R. (1991). *Dynamics of Lasers*. VCH Verlagsgesellschaft.

Wilson, K. G. (1975). *Reviews of Modern Physics*, 47, 773.

Wolynes, P. G., Onuchic, J. N., & Thirumalai, D. (1995). *Science*, 267, 1619.

Zwanzig, R. (1973). Nonlinear generalized Langevin equations. *Journal of Statistical Physics*, 9, 215–220.
