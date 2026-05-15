# MPA-Character: Holding Apparatus

**Status:** Rigorous derivation supporting the character-domain spec.
**Spec:** [`mpa character framework.md`](mpa%20character%20framework.md) — the operational source of truth that this apparatus derives. Spec wins over apparatus on conflict.
**Sibling spec (other domain):** [`v9_compressed.md`](v9_compressed.md) — the parallel structural-domain framework within the same MPA program. The two domains are peers. Directory map and reading order at [`README.md`](README.md).

---

The apparatus for the steady-state of holding — coherence sustained continuously against decay, with finite supply and rivalrous alternatives. The mathematics is the mathematics of dynamical systems, nonequilibrium thermodynamics, laser physics, and time-frequency analysis — character-domain mathematics worked out first for physical substrates. Adoption is direct: substrate-specific vocabulary is replaced by character-domain vocabulary, substrate-specific commitments stripped, and the apparatus stands as native. Origin note in §19.

## 1. Substrate, state space, and coherence

A holding has two layers, and the apparatus rests on the distinction.

- **Substrate.** The persistent material on which a coherence can be held. Brain tissue, a person's body and history, an institution's people and records, a ritual's stage and props. The substrate has its own **state space** — the manifold of all configurations it can be in — independent of any holding.
- **Coherence.** An *attractor* of the holder's dynamics in the substrate's state space — a region toward which trajectories converge under continuous drive — that exists only because the drive is sustained. Remove the drive and trajectories relax to a different attractor (typically a passive equilibrium with no relevant structure). The coherence is what the holding maintains as a non-trivial attractor against the substrate's tendency to relax to its passive state.

This grounds the framework's vocabulary in dynamical-systems language. **A mode is an attractor.** The substrate's **mode structure** is the set of attractors it supports under drive. **Holding amplitude** is the order parameter — distance in state space from the passive equilibrium toward the driven attractor. **Threshold** (§4) is a bifurcation point in parameter space at which the attractor structure changes.

**Three types of coherence** are distinguishable by attractor type. Each type produces different observational signatures, different intervention requirements, and different failure modes.

- *Fixed-point coherences.* The attractor is a single point or small region in state space. The holding is in a sustained steady state. A focused identity, a settled mood, an institutional culture in equilibrium, a relationship at sustained stable engagement.
- *Limit-cycle coherences.* The attractor is a closed periodic orbit. The holding cycles through a sequence of states with a stable period. Rhythmic practices (breath, meditation, daily routine), conversational ebb and flow, ritual cycles, circadian holdings, recurring relationship patterns. The natural frequency $\omega_0$ that appears in §14–§15 is the orbital frequency.
- *Strange-attractor coherences.* The attractor is a fractal set with bounded but non-periodic dynamics. The holding is sustained but never repeats exactly. Practitioner cases likely exist — long creative collaborations, long therapy, improv traditions, certain marriages, generative institutions — but qualifying as a strange-attractor coherence requires identification against technical criteria (bounded non-periodic trajectories, exponential divergence of nearby states, fractal attractor geometry), not vibes. Mathematical criteria are load-bearing; the type is real but its instances are not assumed.

The framework's prior treatment lumped these. The attractor framing separates them.

**Basin of attraction.** Each attractor has a basin: the set of substrate-states from which trajectories converge to that attractor under drive. Mode robustness reads as basin volume — a coherence is robust when many initial states lead to it. Mode boundaries are the surfaces in state space across which a perturbation switches the system from one basin to another. The basin gives substantive content to "how strong is this holding": not just amplitude or chit-rate, but how much state-space deformation the holding can absorb before perturbation escapes its basin. Basin volume is a fourth independent operating-state dimension alongside chit-rate, $Q$, and headroom (§17).

Confusing substrate with coherence — treating the coherence as a property of the substrate, or treating the substrate as part of the coherence — produces the recurring framework errors of biological reductionism (collapse to substrate) and disembodied agency (collapse from substrate).

## 2. Drives

Three rates govern any holding.

- **Supply rate $P$.** The rate at which budget is delivered to the holder. Substrate-specific in form (caloric, attentional, financial, relational), role-invariant. Thermodynamically (§3), the rate of free-energy delivery.
- **Holding rate $g$.** The rate at which the holder builds and reinforces the coherence per unit time. Depends on supply, on substrate capacity, on the coherence's current amplitude, and on competing demands.
- **Decay rate $\kappa$.** The rate at which the coherence would dissolve absent maintenance. Already a primitive; environmentally and internally determined.

The **reserve** $g - \kappa$ is the spendable surplus over baseline drift. Its dynamical reading is given in §14 (damping); its thermodynamic content in §3.

## 3. Mathematical foundations

A holding is a non-equilibrium steady state (NESS). Its operation has thermodynamic, information-theoretic, control-theoretic, and queueing-theoretic content; this section gathers all four. Cross-theme compositions (active modulation as bottleneck-optimal information processing, triage as bottleneck-optimal load handling, Lyapunov function as the formal home of what the holder preserves) are visible at one place. The thermodynamics of NESS provides the foundational layer: drives have thermodynamic content, the chit unit has a derivation rather than an assertion, and the maintenance budget is measurable in physical units (or substrate-equivalent analogues).

**Entropy production rate $\sigma$.** The thermodynamic shadow of holding. At equilibrium (passive state, no holding), $\sigma = 0$. For any sustained NESS, $\sigma > 0$ strictly. $\sigma$ is the rate at which the holder generates entropy — in the bath, in the substrate's environment, in the substrate-equivalent sink — per unit time. This is the thermodynamic content of "what is being spent": heat dissipated to maintain the non-equilibrium operating state, with a precise magnitude.

**Detailed-balance breaking.** A NESS breaks detailed balance — there are net cyclic flows in state space. This is the thermodynamic content of self-stimulation (§5) at the population level: in equilibrium, transitions are detailed-balanced and there is no net cyclic flow; in NESS, drive sustains a directed circulation through state space, and that circulation is the holding. The feedback structure (§9) is the substrate-specific carrier of this cyclic flow.

**Chit-rate as entropy production per event.** The chit unit is information-theoretically and thermodynamically equivalent in a precise sense. For a holding-vs-decay process with rates $g$ and $\kappa$, chit-rate $\log(g/\kappa)$ is the dimensionless entropy produced per holding-event:

$$\sigma_{\text{event}} = \log(g/\kappa) = \text{chit-rate}$$

The time-rate of entropy production is then:

$$\sigma = (\text{event rate}) \cdot \log(g/\kappa)$$

Same quantity in two readings: information per event (the discrimination capacity of an observer telling held-from-decayed) and entropy per event (the thermodynamic cost of holding). The chit unit is principled, not heuristic.

**Fluctuation-dissipation theorem and its violation.** In equilibrium, the response of a holding to a small probe is determined by its spontaneous fluctuations through the FDT: $\chi(\omega) \sim \beta \omega S(\omega)$. For NESS, FDT is generally broken. The integrated FDT-violation gives the entropy production rate (Harada–Sasa relation and generalizations):

$$\sigma \propto \int_0^\infty d\omega \cdot [\chi(\omega) - \chi_{\text{FDT}}(\omega)]$$

This yields a **chit-rate measurement protocol** from observation alone. By measuring (a) the autocorrelation of holding amplitude (or any local proxy) and (b) the response to small test perturbations, one computes $\sigma$ directly. For holdings with characteristic event rate, chit-rate follows. For non-oscillatory holdings, $\sigma$ alone reads the thermodynamic distance from passive equilibrium.

This is the framework's first measurement protocol that does not require imposing loads. Spontaneous fluctuations plus small probes suffice. Together with critical slowing (§16), it gives the practitioner two non-arresting empirical handles on the operating state.

**Imposed vs emergent coherence.** Two thermodynamic limits suggest a structural distinction in how a holding is maintained.

- *Imposed coherence (minimum entropy production).* In the linear-NESS regime near equilibrium, systems minimize entropy production subject to constraints (Prigogine). The holding sits at the lowest-dissipation NESS the constraints allow. *Examples:* a focus held by sheer effort, an institution maintained by external authority, an identity sustained against contrary pressure. *Intervention logic:* removing the constraint causes the holding to dissolve toward equilibrium; the coherence depends on the constraint.
- *Emergent coherence (maximum entropy production).* Far from equilibrium, the analogous selection principle is less rigorous but invoked widely in self-organization theory: systems organize to maximize entropy production. The holding's operating point is selected by the substrate's own dynamics; the structure exists because it dissipates effectively. *Examples:* ecosystems, mature creative collaborations, communities that have found their own form, generative institutions. *Intervention logic:* supporting the dissipation enables the structure; suppressing the dissipation weakens the holding even when supply remains adequate.

Many character-domain phenomena begin as imposed and become emergent through development — a cultivated practice, a deepening relationship, a maturing institution. The transition between regimes is itself a structural change worth recognizing; the system's response to the same external constraint changes qualitatively across the transition.

The MaxEP principle is less rigorous than MEP at the formal level. The framework imports the distinction at the practitioner-relevant level (different intervention logics) without claiming the mathematical status is settled.

**Trajectory thermodynamics (budget grounded).** Stochastic thermodynamics of small systems (Sekimoto, Seifert) gives operational meaning to budget at the trajectory level: work done by the holder along a holding trajectory, heat dissipated to the bath, entropy produced along the path. Large-deviation theory (Cramér; Touchette) supplies the rate functions for rare events — including spontaneous threshold-crossings and basin escapes driven by internal fluctuation rather than external load. The maintenance-budget primitive becomes measurable in physical units (or substrate-equivalent analogues), not as a metaphor. The "spent budget" is, precisely, the heat dissipated by the holder during a holding episode.

**Predictive information.** A trajectory's predictive information is the mutual information between its past and future:

$$I_{\text{pred}}(T) = I(X_{[-T, 0]}; X_{[0, T]})$$

(Bialek–Tishby–Strong). It quantifies the temporal structure compressible to a finite description — how much past determines future. For a coherence, $I_{\text{pred}}$ is positive and grows as the coherence's structure becomes visible to a longer-window observer, eventually saturating at the substrate's effective complexity. For pseudo-coherence (parallel execution, §5), $I_{\text{pred}} \approx 0$ because past and future are uncorrelated — each holding-act is independently shaped, so past does not predict future.

This is a third formal handle on the coherence/pseudo-coherence distinction, alongside the perturbation test (§5) and detailed-balance breaking (§3 above): predictive information measures the temporal compressibility of the holding's trajectory. Operationally measurable from time-series alone, no perturbation required — but data-hungry and computationally nontrivial (mutual-information estimation across time windows requires sufficient samples and care). Of the three tests, perturbation is observationally cheapest; detailed-balance breaking requires substrate-state time-series; predictive information is the most demanding.

**Transfer entropy.** Directional information flow between two stochastic processes (Schreiber). $T_{X \to Y}$ measures how much the past of $X$ reduces uncertainty about the future of $Y$ beyond what the past of $Y$ alone provides. For multi-holder situations — coupled holdings, mentor-student, parent-child, leader-follower in a team, paired identities — transfer entropy quantifies the directionality of influence. Symmetric coupling has $T_{X \to Y} \approx T_{Y \to X}$; asymmetric coupling has one direction dominant. This is the formal apparatus for "who is shaping whom" in a coupled holding, and it composes forward into multi-holder synchronization.

**Mode-pair distance via information geometry.** Different modes have different probability distributions over the substrate's state space (or trajectory space). The Fisher information metric gives a Riemannian distance between these distributions; the Kullback–Leibler divergence gives an asymmetric divergence. Together they make "how different is mode $A$ from mode $B$" a quantitative reading. Mode-shift intervention (§17 below) traverses this distance; deeper interventions cover more distance per move. The substrate's mode structure is a manifold in distribution space, with modes as points and developmental trajectories as paths through it.

**Information bottleneck and active modulation.** A holder doing active modulation (negotiated supply and active response — already in cFDR) is solving an information-theoretic optimization: at minimum cost, which information about input is preserved in the holding? The information bottleneck framework (Tishby–Pereira–Bialek) gives this its formal home. The holder's gain modulation, attention allocation, recruitment, and shedding decisions are bottleneck-optimal compressions of input information given the constraints of the held mode. Active modulation is rate-distortion optimization with the held mode as the relevant target. This connects active modulation in cFDR to a precise mathematical structure and supplies the formal foundation for control-theoretic moves (concept #7 in the queue).

**Critical coherence (self-organized to threshold).** A third operating regime, alongside imposed and emergent. Some holdings self-organize to the threshold surface itself rather than above it: they operate at near-zero reserve, in the critical region of §4, with permanently small damping rate. Self-organized criticality (Bak–Tang–Wiesenfeld; Bak–Sneppen; Drossel–Schwabl) is the formal apparatus. The substrate's dynamics drive it toward criticality without parameter tuning — slow drive, fast relaxation, scale-invariant fluctuations.

*Examples:* edge-of-burnout attention, brittle relationships at sustained brinkmanship, certain forms of long-running creative work that operate at maximum sensitivity, ecologies poised at the edge of regime shift, addictions in tenuous remission, organizations operating at the edge of viability. *Intervention logic:* moving the holding off-threshold (either above or below) qualitatively changes its character — critical operation is its own regime, not a transitional state on the way to collapse.

**Empirical signatures of critical coherence.** Distinct from stable far-from-equilibrium operation; detectable from time-series alone:

- *Power-law event-size distribution.* Fluctuation events (avalanches, perturbation responses, spontaneous transitions) follow $P(s) \sim s^{-\tau}$ for some critical exponent $\tau$ — no characteristic event size. Small fluctuations are common; large fluctuations rare but inevitable.
- *$1/f$ spectrum.* The fluctuation spectrum follows $S(f) \sim 1/f^\alpha$, distinct from the Lorentzian spectrum of stable holdings (which has a characteristic $\Gamma$) or the white-noise spectrum of pseudo-coherence.
- *Punctuated dynamics.* Long quiet periods interrupted by events of varying magnitude. Visible in time-series at any window length (scale invariance).
- *Permanent critical-slowing-like signatures.* Because the system lives at threshold, $\Gamma$ is permanently small, autocorrelation decays slowly, variance is large. The signatures of approach to collapse (§16) are *diagnostic of critical operation* in this regime, not of approach.

These signatures distinguish critical coherence from imposed and emergent regimes — and from approach-to-collapse situations of stable holdings — which is empirically actionable.

**Functional reading: critical coherence as adaptive operating-point.** Critical operation is not always pathology. At the critical state, holdings can have maximum information-processing capacity per unit dissipation, maximum sensitivity to weak signals, maximum dynamic range, and maximum adaptability (results from neuronal-avalanche literature, ecological criticality, edge-of-chaos computation). Some substrates may be self-organized to criticality for these functional reasons. The tradeoff: critical operation is fragile to large fluctuations by definition. The same statistics that give criticality its information-processing benefits produce occasional system-spanning avalanches.

The SOC framing makes precise the practitioner intuition that operating "on the edge" can be maximally responsive while being maximally vulnerable. The two are not separable trade-offs — they are the same fact about critical states.

**Controllability and observability.** Structural properties of the holder-substrate pair from control theory. *Controllability:* can the holder, given enough time and budget, drive the substrate to any state in its mode structure? Some modes may be present but uncontrollable — they exist as attractors but no active modulation reaches them from the current operating mode. *Observability:* can the holder, given enough observation, infer which mode is currently held? Some states may be indistinguishable from observation alone — present but unreadable without additional probes. Both are decidable from the dynamics; both have practitioner content. A holder operating with limited controllability is choosing among a subset of modes, not the full mode structure. A holder operating with limited observability cannot diagnose which mode they are in, which complicates every other diagnostic in the apparatus.

**Internal model principle.** A controller that perfectly rejects a class of disturbances must contain a model of those disturbances (Francis–Wonham; Sontag). For character-domain holdings: a holder that rejects a class of perturbations contains an internal model of those perturbations — anticipatory rather than reactive. This formalizes "anticipatory holding" — knowing what kinds of perturbation to expect and being prepared. Maps to: experienced practitioners who hold steady through anticipated disruptions, mature institutions that absorb predictable shocks, identities resilient to known threats. The internal model is part of what the holder *is* — it is the substrate of anticipatory capacity, and acquiring it is part of the imposed→emergent transition (§7).

**Dual control: exploration vs exploitation.** Active modulation faces a fundamental tradeoff (Feldbaum; Wittenmark). The holder must simultaneously: (a) gather information about the substrate's mode structure and current operating point (exploration), and (b) operate on current knowledge (exploitation). The two are in tension — exploring perturbs the holding; exploitation neglects information. The dual-control balance varies with developmental phase (§7): in incipient modes, exploration dominates; in mature modes, exploitation; the transition between phases is, in part, the shifting of the dual-control balance. Apparatus from optimal control (Gittins index, Bayesian dual control, multi-armed bandit theory) provides quantitative tools for the tradeoff.

**Load as process: arrival rate, service rate, utilization.** Loads in character domain (§4 of framework) have so far been treated as conditions; queueing-theoretic content adds the discrete-event reading. A holding receives load events at rate $\lambda$ and processes them at rate $\mu$. The utilization $\rho = \lambda/\mu$ is the fraction of holder capacity engaged with load processing. Stability requires $\rho < 1$ — the holder must on average process faster than load arrives. $\lambda$, $\mu$, $\rho$ compose with existing primitives but are properties of load-handling rather than steady-state operation: a holding can have any $\rho$ at any chit-rate, $Q$, headroom, or basin volume. Three new rates that join the apparatus's load side rather than its operation side.

**Backlog and backpressure.** When load arrives faster than the holder processes, backlog accumulates as an unprocessed-load state distinct from the operating amplitude. The visible operation can look fine — chit-rate, $Q$, headroom all healthy — while the backlog grows. Backlog is a load-side state worth tracking; it signals approach to heavy-traffic regime (below) before any operating-state reading does. Little's law gives the formal relation: $L = \lambda W$ — average backlog equals arrival rate times average wait — and is robust across queue disciplines and service distributions.

**Heavy-traffic regime as a distinct failure mode.** When $\rho \to 1$, queue length and wait time scale as $\sim 1/(1-\rho)$ (Kingman; Whitt). The holder is technically processing every load that arrives, but the backlog dominates: response times diverge, accumulated load consumes attention, the system is stable but never catches up. Distinct from fraying — in heavy-traffic, capacity meets average load *exactly*, so the holding does not collapse, it accumulates. Practitioner experience: "drowning" — competently handling each day's input while the backlog grows toward unbounded. This is a new failure mode in the unified taxonomy: site = load-handling, mechanism = $\rho$ approaching 1, signature = response-time divergence with operating-state readings unchanged.

**Triage and priority queues as load-handling active modulation.** Active modulation at the load-handling layer is queueing-theoretic: the holder cannot process all arrivals at full attention, so it prioritizes — high-priority loads served first or pre-emptively, low-priority deferred or dropped. This is information-bottleneck-optimal compression (§3 above) applied at the load-side: which load information is preserved at full attention, which compressed, which discarded. Triage decisions follow the bottleneck criterion (preserve relevance for the held mode). Pre-emption — high-priority load interrupting current processing — is a queueing-theoretic operation distinct from continuous active modulation. A holder operating without explicit triage typically operates with implicit FIFO, which is rarely optimal under non-uniform load priorities.

**Self-exciting load (Hawkes processes).** Character-domain load events are not Poissonian. They are self-exciting: one event raises the probability of subsequent events (Hawkes; Ogata). A bad day primes the next; a crisis spawns related crises; trauma compounds. The mathematical apparatus is well-developed (Hawkes processes, branching processes, marked point processes). For character-domain holdings, this matters because load arrives in bursts: bursts of high $\rho$ alternate with quiet periods of low $\rho$, and the holder must handle the burst without losing the holding and recover before the next burst. Non-stationary queueing theory (Whitt; Massey) treats this rigorously. The Hawkes structure connects to large-deviation theory (§3 above): the rate function for a burst exceeding a given size determines how rare large bursts are.

## 4. Threshold and bifurcation

The condition $g = \kappa$ separates two qualitatively different operating regimes.

- **Below threshold ($g < \kappa$):** pseudo-coherence. Activity occurs but does not sustain itself.
- **At threshold ($g \approx \kappa$):** critical region. Fluctuations slow; the holder hovers between regimes.
- **Above threshold ($g > \kappa$):** coherence. The pattern feeds back on itself and is sustained.

In dynamical-systems language (§1), threshold is the **bifurcation surface** at which a non-trivial driven attractor appears (from below) or disappears (from above). In thermodynamic language (§3), threshold is the surface at which entropy production becomes positive — where the substrate transitions from passive equilibrium to maintained NESS. The threshold is in general a smoothed crossover, not a sharp non-analytic point.

**Bifurcation typology.** Different bifurcation types produce different threshold dynamics, different transition signatures, and different critical-slowing exponents (§16).

- *Saddle-node:* an attractor pair appears or disappears at threshold. Sharp transition with hysteresis; subcritical onset.
- *Pitchfork (supercritical):* symmetric mode-splitting; smooth onset, no hysteresis.
- *Pitchfork (subcritical):* same symmetry breaking but with a jump at onset and hysteresis on retreat.
- *Hopf:* a fixed-point attractor becomes a limit cycle at threshold. The bifurcation underlying onset of rhythmic coherences from steady-state ones.
- *Period-doubling:* a limit cycle bifurcates to a period-doubled cycle; cascade gives a route to chaos.
- *Crisis:* sudden change in strange-attractor structure.

The bifurcation type at a given threshold is a property of the substrate-in-mode, not of the holder. It determines what kind of transition is approached at collapse and what empirical signature its critical slowing carries. Bifurcation typology is the framework's analytic classification of transitions.

Critical coherences (§3) operate ON the threshold surface rather than above or below it. The threshold serves as their operating point rather than as a boundary they cross — a distinct regime that requires its own treatment.

## 5. Pseudo-coherence and coherence

The threshold separates two kinds of activity that look similar from outside but operate differently.

- **Pseudo-coherence: parallel execution.** Each holding-act is independently shaped by the form of the coherence but does not feed back on the others. Going through the motions. The form is correct; the self-reinforcement is absent.
- **Coherence: self-stimulation.** Each holding-act is shaped by the existing pattern and reinforces it. The pattern's existence is what governs the next act. Self-amplifying.

In attractor language (§1): coherence is operation on a non-trivial driven attractor with a populated basin; pseudo-coherence is parallel-executing activity that has not formed an attractor. In thermodynamic language (§3): coherence is a NESS with broken detailed balance and net cyclic flow; pseudo-coherence is parallel activity at or near detailed balance with no sustained directional flow.

This distinction has an operational test independent of internal access: perturbation. Genuine coherence absorbs perturbation and continues; pseudo-coherence breaks because each act does not know about the others. The test recovers the practitioner's commitment-vs-performance distinction without resort to claims about interiority.

## 6. Holding amplitude

The order parameter of the operation. The magnitude of the coherence currently held — formally, the distance in state space from the passive equilibrium toward the driven attractor.

- Zero below threshold (no driven attractor exists).
- Finite and growing above threshold, until limited by saturation (§8).
- Distinct from both supply rate and holding rate; a slow-supply high-Q coherence and a fast-supply low-Q coherence may show the same amplitude.

## 7. Modes and mode structure

A **mode** is an attractor of the holder's dynamics under drive (§1) — a specific coherence-shape that a substrate can support, with its own threshold (bifurcation), gain function, saturation profile, basin of attraction, and damping characteristics.

The **mode structure** of a context is the set of attractors that context admits under drive. Some substrates support few modes (specialized institutions, focused practices); others many (general-purpose minds, broad communities). Mode structure is a property of the substrate's state space and dynamics, not of any individual holding.

A holder operating in mode $M$ maintains $M$. The same holder, in the same substrate, in mode $M'$, would maintain $M'$. The mode is which coherence is being held; the substrate is what could in principle be held.

**Multistability.** When a substrate's mode structure includes multiple attractors at the same parameter values, the substrate is multistable. The current operating mode depends on history — which basin the system was initialized in or pushed into. Multistability is distinct from mode competition (§10): multistability is structural multiplicity in the attractor set; mode competition is the dynamics of contention between modes for shared supply.

**Mode structure as itself a dissipative structure.** Mode structure is not a pre-existing fact. The set of attractors a substrate supports is an emergent product of the substrate's history under drive — formed through the same far-from-equilibrium dynamics that produce convection cells, chemical oscillations, and biological pattern formation. Spontaneous symmetry breaking, fluctuation amplification, and stabilization of patterns that effectively dissipate produce the substrate's mode set. The apparatus has been presupposing mode structure; dissipative-structures theory supplies how mode structure arises.

**Developmental phases of a mode.** A mode passes through phases distinguishable in principle from the time-series of holding amplitude and its statistics:

- *Incipient.* The mode is forming. Multiple competing patterns may exist below their joint thresholds; fluctuations have not yet stabilized one. Trajectories are sensitive to small perturbations; the eventual mode structure depends on which fluctuation grows first. Practitioner observation: high variance, no settled identity, exploratory behavior.
- *Established.* The mode operates as a stable attractor with a populated basin. Chit-rate, $Q$, headroom are defined and measurable. The apparatus's other sections describe behavior in this phase.
- *Mature.* Saturation slope is moderate, basin is wide, the mode has accumulated supporting feedback structure (institutional memory, narrative scaffolding, neural plasticity). Recovery from large perturbation is robust.
- *Declining.* Drive recedes, supply substrate erodes, or competing modes capture supply. Reserve shrinks; basin narrows. Critical slowing detectable; the mode is on its way to a transition or collapse.
- *Vestigial.* The mode is no longer reliably operating, but some trace remains in the substrate (residual feedback structure, atrophied basin). Recovery may or may not be possible with renewed drive depending on whether the supporting feedback structure has decayed beyond recovery.

These phases are not categorical. A substrate can have modes in different phases simultaneously; modes can move between phases.

**Fluctuation-driven mode selection.** During incipient phase, multiple modes may be possible from the same starting substrate under the same drive. Which mode emerges depends on which fluctuation grows first. This is variation-and-selection at the level of mode formation, distinct from mode competition (§10) which operates between established modes contending for supply. Mode formation is path-dependent at the developmental level: different developmental histories produce different mode structures from the same starting substrate under the same drive.

**Hierarchy of substrates.** Established modes can themselves serve as substrates for higher-order modes. Institutional standard practices (level-1 modes) become the substrate on which institutional culture (level-2 modes) forms. Concept-modes in a neural substrate become the substrate on which theory or identity modes form. Ritual cycles (level-1) become the substrate on which collective meaning (level-2) sustains.

The hierarchy is not strictly nested — modes at different levels can share substrate, interact, compete — but there is a partial order: higher-level modes presuppose lower-level mode structure. Failures at one level can disable structures at the level above.

**The imposed→emergent transition formalized.** §3 distinguished imposed (constraint-dependent, MEP-like) from emergent (self-organized, MaxEP-like) coherence and noted that many phenomena begin imposed and become emergent through development. The mechanism is now explicit: repeated imposition of a holding modifies the substrate's mode structure — Hebbian-like plasticity for neural substrates, habit formation for behavioral, ritual entrainment for collective, institutional memory for organizational. After enough development, the substrate's attractor set includes the previously-imposed mode as a stable attractor with its own basin. The holding then becomes self-sustaining without the original constraint.

The transition is detectable: the system's response to removal of the original constraint changes qualitatively. Before, removing the constraint dissolves the holding. After, it does not. This is the framework's first formal account of "becoming emergent" — a developmental change in the substrate's mode structure, not just a change in operating regime.

## 8. Saturation and headroom

**Saturation** is the mechanism by which a successful coherence consumes the substrate that enables it. As holding amplitude grows, the supply substrate is depleted. The institution that succeeds consumes the loose attention that produced its founding. The identity that consolidates exhausts the slots that defined it. The conversation that deepens exhausts the surface available for return.

Saturation is dual-roled.

- **Stabilizing role:** mild saturation pulls $g$ down to match $\kappa$ at a stable operating amplitude. This is what makes coherences stop growing once they reach their natural size — what gives the attractor its location in state space.
- **Failure-mode role:** excessive saturation depletes the substrate-of-supply itself, eventually starving the operation. Distinct from fraying (load excess) and from collapse (decay surge).

**Headroom $s$** is the local slope of the substrate's saturation curve at the operating point. Technically, $s = -\partial g/\partial a$ at the operating amplitude. Operationally, $s$ reads as the inverse of operating slack — *how tightly the substrate is operating at this amplitude*. Large $s$: narrow headroom (steep local saturation, small amplitude excursions cause large gain drops, the substrate is locally tight). Small $s$: wide headroom (gentle local saturation, room for amplitude growth before saturation tightens, the substrate is locally loose). Headroom is independent of $g$ and $\kappa$ — a substrate can have any saturation slope at any net-rate.

Headroom is load-bearing: it sets the dynamical reading of reserve (§14), it appears in the uncertainty relation (§15), and it is one of the operating-state dimensions (§17).

The graded outcomes extend to:

> continued holding · visible strain · fraying · **saturation** · transition · collapse

## 9. Feedback structure (the holding loop)

The structural condition that returns maintenance through itself across time. By what mechanism does this holding-act inform the next?

Substrate-specific in form: synaptic recurrence in neural substrates, narrative repetition in personal identity, ritual cycle in collective practice, institutional memory in organizations, conversation history in dialog. Role-invariant: in every case, the loop is what makes self-stimulation (§5) possible — and, thermodynamically, what carries the cyclic flow that breaks detailed balance (§3).

The feedback structure is *part of* what is being held. It does not pre-exist the operation as a fixed cavity; it is constructed and maintained by the operation, and it dissolves when the operation does. This is the clearest break from the photonic case: in a laser the cavity geometry persists when the mode does not; in character domain the holding loop is itself a coherence requiring its own maintenance.

The feedback structure can fail independently of the mode it carries. A relationship can lose its narrative even when both parties remain; an institution can lose its memory even with all its people in place; a practice can lose its ritual even with all the props. Loss of feedback structure is a distinct failure mode from loss of supply or excess of decay.

## 10. Mode competition

Rivalrous coherences contend for shared supply. The framework already names this as counter-load; the apparatus adds a regime classification.

In attractor language (§1): mode competition is the dynamics of trajectories near basin boundaries between competing attractors. Each mode has a basin; under contention for supply, the basins themselves shrink and shift. Three regimes:

- **Winner-take-all.** A single basin dominates the state space; competing modes are pushed below threshold (their attractors disappear or become unreachable). Maps to focused commitment, single-tracked attention, monolithic identity.
- **Cooperative coexistence (mode locking).** Multiple attractors coexist; the joint dynamics produces a higher-order attractor — a "locked" configuration — more stable than the individual modes alone. Maps to integrated identity, ensemble coherence, group flow.
- **Mode hopping.** Trajectories repeatedly cross basin boundaries; no stable winner; the system chaotically alternates between modes. Maps to identity vacillation, indecision regimes, organizational thrash.

Which regime obtains depends on the coupling structure between modes (cooperative vs antagonistic), the relative thresholds, the supply margin above threshold, and the basin-volume ratios. All three regimes are stable operating conditions in their own right, not pathologies of one another.

## 11. Mode locking and multi-holder coherence

The coordination mechanism behind cooperative coexistence. Phase relations across coexisting holdings become locked, and the locked configuration is more stable than the unlocked.

This is the technical concept underlying the practitioner phenomena of flow states (multiple sub-coherences locking into a single sustained operation), ensemble coherence (musicians, surgical teams, sports teams), group entrainment (collective mood, shared rhythm), and the "click" of well-functioning teams. The locking is not metaphor; it is the same phenomenon that produces ultrashort pulses in lasers and synchronized firing in coupled oscillators.

Mode locking is empirically detectable through phase-relationship measurements that don't require arresting the operation: synchrony in time-series, cross-coherence in spectral analysis, drift correlations across modes.

**Synchronization order parameter.** For a system of $N$ coupled holdings (or $N$ sub-coherences within a multi-holder system) with phases $\theta_i$:

$$r e^{i\psi} = \frac{1}{N} \sum_{j=1}^{N} e^{i\theta_j}$$

$r$ is the synchronization order parameter (Kuramoto). $r = 0$ is fully incoherent (random phase relations); $r = 1$ is fully synchronized (all phases equal); intermediate values measure partial sync. $\psi$ is the mean phase. The order parameter is operationally measurable from time-series of holding-amplitude proxies for each component, and gives the framework its first quantitative measure of multi-holder coherence.

**Critical coupling.** A new threshold beyond the within-mode bifurcation thresholds (§4). For coupled holdings with natural frequencies $\omega_i$ drawn from a distribution $g(\omega)$ and pairwise coupling strength $K$, sync emerges via continuous phase transition at:

$$K_c = \frac{2}{\pi g(\omega_{\text{mean}})}$$

(simplest Kuramoto case). Below $K_c$: incoherent multi-holder operation, $r \approx 0$. Above $K_c$: synchronized, $r$ grows from zero. The critical coupling has its own critical slowing and order-parameter scaling near $K_c$, distinct from the within-mode bifurcation thresholds. Multi-holder coherences therefore have their own threshold surface: not just whether each individual mode is held, but whether they synchronize.

**Phase locking vs frequency locking.** Two synchronization regimes within the cooperative classification:

- *Phase-locked.* All oscillators have the same instantaneous frequency AND fixed phase relations. The strongest form of sync. Maps to tight ensemble coherence, deep flow states, fully integrated team operation.
- *Frequency-locked.* All oscillators have the same average frequency but phase relations drift slowly. Looser sync. Maps to long-running collaboration with autonomous sub-roles, parallel institutions with shared cycles, paired holdings with independent rhythms.

**Partial sync and chimera states.** Some sub-coherences synchronize while others remain incoherent in the same multi-holder system (Kuramoto–Battogtokh; Abrams–Strogatz). Chimera regimes are *not* transitional states — they are stable operating conditions in their own right under generic conditions of asymmetric or non-uniform coupling. Maps to: a team where some members are deeply locked while others operate autonomously; an institution where some sub-units coordinate while others run independently; a relationship where some dimensions sync and others don't. Refinement of the cooperative-coexistence regime in §9.

**Network topology of coupling.** Which holders couple to which determines the synchronization structure. Random graphs, scale-free networks, small-world networks, regular lattices have different critical couplings and different sync patterns. Real multi-holder coherences have structured coupling — people talk to specific people, sub-units interact with specific sub-units — and the topology shapes who can synchronize with whom. The master stability function (Pecora–Carroll) gives stability conditions for synchronized states on networks; the apparatus is well-developed for analyzing whether a given coupling network can sustain a given sync regime.

**Sync-breaking transitions.** As coupling decreases, decay rises, or natural-frequency dispersion grows, sync breaks via specific routes:

- *Phase-slip:* order parameter $r$ drops continuously; some oscillators drift out of phase before others.
- *Chimera formation:* sync fragments into coexisting synchronous and incoherent sub-populations.
- *Cluster splitting:* the synchronized population splits into multiple smaller synchronized clusters.
- *Sudden desync:* order parameter drops discontinuously (subcritical transition with hysteresis).

Each route has empirical signatures observable from the time-series of multi-holder amplitude or its proxies, and each implies a different intervention to restore sync.

**Generalized synchronization.** Two systems can be functionally synchronized without literal phase locking — the state of one is a deterministic function of the state of the other (Rulkov et al.; Kocarev–Parlitz). Useful for cases where coupled holdings are not oscillating but are functionally aligned: a mentor-student pair where the student's responses are determined by but not synchronous with the mentor's; a partnership where one's actions follow predictably from the other's without literal coordination. Generalized sync requires measurement protocols beyond phase-relationship analysis (mutual prediction tests, transfer entropy from §3, recurrence-network methods).

**Active constituents and recursive multi-holder coherence.** The framework's recursive case: each constituent of a multi-holder coherence is itself a holding (an attractor under drive — a level-1 mode in the hierarchy of §7). Active matter physics gives the formal apparatus. The constituents are *active* in the technical sense — each is a sustained NESS with its own metabolism of supply, decay, and holding. Their collective dynamics (sync, flocking, phase separation) emerges from their interactions, but is qualitatively different from couplings between passive oscillators because each constituent has its own active properties. This is the typical case for character-domain multi-holder coherences (a community of held identities, a team of held roles, an institution of held practices), not the special case.

**Non-reciprocal coupling.** $A \to B$ different from $B \to A$. The Kuramoto framework above assumes reciprocal coupling; active-matter physics generalizes (Fruchart–Vitelli; Saha–Sharma–Golestanian) to the asymmetric case. Non-reciprocal coupling is generic in character-domain multi-holder situations: power asymmetry, attention asymmetry, parent-child, mentor-student, leader-follower, predator-prey-like dynamics, status-asymmetric pairs. Non-reciprocal sync produces phenomena absent from the reciprocal case:

- *Traveling-wave sync.* Phase relations are locked but not stationary; the sync pattern travels through the network.
- *Oscillatory sync states.* The system has no fixed-point sync but oscillates between sync configurations with a regular period.
- *Exceptional points.* Parameter values where the sync structure becomes singular; small perturbations near exceptional points have outsized effects on collective behavior.

These regimes are stable in their own right under non-reciprocal coupling, not pathologies of failed reciprocal sync.

**Flocking and collective alignment.** Collective coordination without explicit central direction. The Vicsek model (Vicsek et al.) and Toner–Tu equations describe how local alignment rules among active constituents produce long-range collective motion. For character domain: collective belief alignment, shared mood, group purpose alignment, cultural drift — coordination at the scale of the community without anyone explicitly coordinating. The transition from disordered to ordered (the flocking transition) is an active phase transition with its own critical behavior, and it can produce long-range order even where equilibrium-physics analogues would forbid it (active matter circumvents the Mermin–Wagner theorem in low dimensions).

**Active phase transitions.** Collective transitions in active matter are qualitatively different from equilibrium phase transitions — different critical exponents, different spatial structures, different response to noise (Toner–Tu; Marchetti et al.). For character-domain multi-holder coherences: collective transitions between modes (a group breaking up, an institution restructuring, a community shifting culture) work differently than passive collapses because the constituents are themselves active. The collective transition involves coordinated changes in the constituents' active properties, not just rearrangement of passive states. Practitioner content: interventions that succeed at the constituent level may not succeed at the collective level if the active phase-transition structure is not engaged.

**Topological defects in alignment fields.** Singularities in alignment fields (disclinations, vortices) where the local order parameter is undefined. In active matter, defects self-propel and have non-trivial dynamics that reorganize the global structure (Doostmohammadi et al.; DeCamp et al.). For character-domain multi-holder situations: structural "defects" in alignment — members holding orthogonal positions, dissenters, contrarians, paradoxes — may have their own emergent dynamics distinct from the bulk. The defect dynamics can be productive (they drive reorganization, generate creative friction) or destructive (they puncture coherence, fragment the group). The active-matter apparatus suggests that defects are not merely disturbances but structural features with their own roles, often essential to the system's ability to reorganize.

## 12. Coherence time

The holding-time over which the coherence remains identifiable as itself.

Sharp coherences have small drift rate and long coherence time; broad coherences have large drift rate and short coherence time. Two coherences can have the same amplitude (§6) and very different coherence times.

For character-domain analysis: a long-coherence-time identity is one that remains recognizable across years; a short-coherence-time mood is recognizable for an afternoon; a working memory is shorter still. Coherence time is the natural scale at which the holding is operating, and it sets the timescale for any intervention.

## 13. Q (quality factor)

The efficiency of holding. Up to a frequency factor: $Q$ = sustained coherence / per-cycle dissipation. For oscillatory holdings, $Q = \omega_0 / (2\Gamma)$ where $\Gamma$ is the damping rate (§14). $Q$ is the dimensionless reading of damping; the formal conjugate-variable result connecting them is in §15.

Two coherences with the same chit-rate may have very different $Q$. The chit-rate $\log(g/\kappa)$ is the *net-rate* reading of an operation; $Q$ is its *per-budget-unit* (or per-cycle) reading. Both are needed.

## 14. Damping

A holding has a stable operating point determined by the balance of $g$, $\kappa$, and saturation. **Damping** is the rate $\Gamma$ at which fluctuations from that operating point decay. In dynamical-systems language, $\Gamma$ is the relaxation rate of the linearization around the attractor — the magnitude of the leading eigenvalue of the Jacobian of the dynamics at the attractor.

For small fluctuations $\delta a$ in holding amplitude near the operating point:

$$\delta a(t) \sim e^{-\Gamma t}$$

In the simplest (saturation-dominated) case, $\Gamma$ scales with the reserve and headroom:

$$\Gamma \approx |g - \kappa| \cdot s$$

The reserve is therefore the *dynamical* reading of responsiveness, modulated by headroom. Two holdings with the same chit-rate but different reserves recover from perturbation at different rates; two holdings with the same reserve but different headroom likewise.

**Sign of damping at threshold.** Below threshold, $\Gamma > 0$ pulls amplitude perturbations back to zero (no coherence). Above threshold, $\Gamma > 0$ pulls amplitude perturbations back to the finite operating amplitude (saturation does the pulling). At threshold, $\Gamma \to 0$. The threshold surface is where damping changes which attractor it pulls toward, with a critical region of vanishing damping between.

**Three regimes for oscillatory holdings.** Some coherences have rhythmic structure with a natural frequency $\omega_0$ (limit-cycle attractors, §1). For these, damping interacts with $\omega_0$ to produce three qualitatively different return dynamics:

- *Underdamped* ($\Gamma < \omega_0$): the holding oscillates while settling. Overshoot, swing, healthy variability. Maps to rhythmic life, conversational ebb-flow, normal emotional range.
- *Critically damped* ($\Gamma \approx \omega_0$): settles fastest without overshoot. Maps to efficient practice, well-tuned response.
- *Overdamped* ($\Gamma > \omega_0$): settles slowly without overshoot. Sluggish recovery; characteristic of sclerosis, depressive flattening, organizational stuck-ness.

Each regime is a stable operating mode in its own right; the practitioner's question is which regime is appropriate to the coherence in question.

**Asymmetric damping in active systems.** Active holdings have damping that depends on the direction of perturbation. Excess amplitude (over-engagement, hyper-vigilance) and deficit amplitude (drift, distraction, drain) typically relax at different rates, and the asymmetry is substrate- and mode-specific. Practitioners observe this directly: it is harder to recover from one direction than the other for a given holding. Structural physics tends to symmetric damping by construction; character-domain damping does not.

**Overdamping as a failure mode.** A coherence can retain its operating point yet lose the capacity to respond fluidly to perturbation. The holding is technically intact; its responsiveness is degraded. Phenomenologically: rigidity, sclerosis, depressive flattening, organizational stuck-ness, ritual that has ceased to breathe. This is a failure mode distinct from those named so far. It belongs in the unified taxonomy as **overdamping (responsiveness loss)** — site: dynamics, mechanism: damping rate exceeds the natural frequency of the holding's operation. Intervention is unique: not more supply, not less load, but a restoration of damping itself, often through deliberate variation, perturbation-with-recovery, reduction of substrate-load, or substrate change.

**Underdamping as a fragility, not a failure.** Healthy oscillatory holdings are mildly underdamped; this is not pathology. Excessive underdamping — large overshoot, ringing into instability, oscillations that drive the system through threshold from above — is severity within the healthy regime, not a categorically different mechanism. It is treated as severity dynamics, not as a separate failure mode.

**Lyapunov function and stability.** The dynamical-systems statement of "what is being preserved." A Lyapunov function $V(x)$ is positive definite, vanishes at the attractor, and decreases along trajectories: $\dot{V} \leq 0$ with equality only at the attractor. For character-domain holdings, $V$ formalizes the abstract objective the active modulation pulls toward — what the holder is keeping low. The damping rate $\Gamma$ corresponds to the local rate at which $V$ decreases near the attractor; basin volume corresponds to the level set $\{x : V(x) \leq V_{\max}\}$. Lyapunov analysis provides the formal apparatus for stability proofs and basin-of-attraction estimates, and gives the holder's "objective function" precise mathematical content distinct from chit-rate, $Q$, headroom, and basin volume — it is the function whose level sets *are* the basin structure. The framework's basin volume is the volume of $V$'s sub-level set; the framework's reserve is $V$'s value at the attractor; the framework's damping is $V$'s decay rate.

## 15. Selectivity–responsiveness uncertainty

Time-bandwidth uncertainty applied to holdings. A character-domain instance of the same Fourier-conjugacy that underlies the energy-time uncertainty principle in quantum mechanics.

For a holding's temporal trajectory — the time-series of its amplitude or any local proxy — the spectral width $\Delta\omega$ and the response timescale $\Delta t$ satisfy:

$$\Delta\omega \cdot \Delta t \geq 1/2$$

This is a fixed mathematical bound. **Selectivity** (a narrow spectral feature, $\Delta\omega$ small — a sharply identifiable holding) and **responsiveness** (a fast response, $\Delta t$ small — fast recovery and adaptation) are conjugate. They cannot both be maximized.

For oscillatory holdings with natural frequency $\omega_0$ and Lorentzian response, the bound is saturated:

$$Q \cdot \Gamma = \omega_0/2$$

The result is rigorous, not analogical. The conjugacy is the same time-frequency duality that gives the Fourier transform its uncertainty structure. In quantum mechanics, $E = \hbar\omega$ converts time-frequency uncertainty into time-energy uncertainty $\Delta E \cdot \Delta t \geq \hbar/2$. The character-domain reading is the same conjugacy applied to the holding's temporal trajectory: the framework's first formal uncertainty result, a Heisenberg-style conjugate-variable bound rather than a heuristic constraint.

**Practitioner content.** A holding cannot simultaneously be highly selective (long-coherent, sharply identified, durable) and highly responsive (fast-recovering, plastic, adaptive). Moves that sharpen a coherence necessarily reduce its responsiveness; moves that broaden it necessarily sacrifice precision for recovery speed. The tradeoff is mathematical, not empirical, not substrate-specific, and not eliminable by clever practice.

The two readings practitioners use directly:

- *Choose what to optimize.* A coherence that needs to be precisely identifiable and durable must accept slow recovery. A coherence that needs to recover fast must accept lower selectivity.
- *Distrust apparent exceptions.* A holding that *appears* both highly selective and highly responsive is operating in a regime the uncertainty relation rules out. The appearance has one of three sources: partial selectivity (plurality with sharp components), partial responsiveness (selectively responsive), or decorative precision (high-amplitude pseudo-coherence rather than genuine selectivity).

## 16. Critical slowing

A special case of the dynamics in §14. As a coherence approaches its threshold from above — decay rising, supply falling, headroom narrowing, or any combination — the reserve $g - \kappa$ shrinks, $\Gamma \to 0$, and the relaxation time $\tau_{relax} = 1/\Gamma$ diverges. The system "drags" before letting go.

The *shape* of the divergence depends on the bifurcation type at the threshold (§4):

- *Saddle-node:* $\Gamma \sim |g - \kappa|^{1/2}$ — square-root scaling. Sharp, sudden transitions show this.
- *Pitchfork (supercritical):* $\Gamma \sim |g - \kappa|$ — linear scaling. Smooth-onset bifurcations show this.
- *Hopf:* $\Gamma \sim |g - \kappa|$ for the radial mode (amplitude direction); the angular mode (phase direction) is neutrally damped and shows constant fluctuation timescale.
- *Subcritical bifurcations:* often discontinuous. Critical slowing on approach but jump on retreat; hysteresis observable.

These are the framework's first quantitative empirical signatures of bifurcation type. A coherence approaching collapse can be classified — saddle-node, pitchfork, Hopf — by the scaling exponent of its critical slowing.

Empirically detectable in any time-series of the holding amplitude or its proxies: autocorrelation decays more slowly, variance grows, response to test perturbations widens, low-frequency spectral weight grows. Universal across substrates carrying a threshold-driven coherence; the scaling exponent is the mode-specific signature within the universal phenomenon.

**Distinguishing critical-slowing-on-approach from critical operation.** The signatures here characterize a stable holding *approaching* threshold from above. Critical coherences (§3) show the same signatures *permanently* — they live at the threshold rather than approaching it. Distinguishing the two cases requires longer time-series: approach-to-collapse signatures intensify monotonically as collapse nears, while critical-coherence signatures are stationary. The two regimes converge in the limit and are operationally distinguishable from temporal trend, not from instantaneous spectrum alone.

## 17. Composition with existing primitives

The apparatus enters MPA-Character with the following compositions:

- **chit-rate** $= \log(g/\kappa)$. Net-rate reading. Information-theoretic and thermodynamic content: entropy production per holding-event (§3). Foundational, not heuristic.
- **Entropy production rate $\sigma$.** Time-rate of entropy production at the population level. $\sigma > 0$ defines the holding state; $\sigma = 0$ is passive equilibrium.
- **$Q$.** Per-cycle (per-budget-unit) reading. Dimensionless reading of damping (§13, §14).
- **Headroom $s$.** Operating-slack reading.
- **Basin volume.** Mode-robustness reading.
- **Reserve** $= g - \kappa$. Spendable surplus, governs robustness to short-term shocks; enters the dynamical reading of responsiveness via $\Gamma \approx |g-\kappa| \cdot s$.
- **Damping rate $\Gamma$.** Linear-stability eigenvalue of the dynamics around the attractor. Vanishes at threshold (critical slowing).
- **Threshold = bifurcation surface = $\sigma$-onset surface.** Onset of genuine coherence; surface from above which collapse is approached. The bifurcation type at this surface determines the threshold's local shape and the critical-slowing exponent.
- **Coherence as attractor under drive (§1) and as NESS with broken detailed balance (§3).** Two readings of the same operating object, dynamical and thermodynamic.
- **Three coherence types.** Fixed-point, limit-cycle, strange-attractor.
- **Three coherence regimes (§3).** Imposed (minimum entropy production, depends on constraint), emergent (maximum entropy production, self-organized), critical (self-organized to threshold, operates with permanently small $\Gamma$). Cut across the three types.
- **Counter-load** is already a primitive; mode competition is its formalization with regime classification (basin dynamics).
- **Multistability** is structural multiplicity in the attractor set, distinct from mode competition.
- **Graded outcomes** extend to: holding · strain · fraying · **saturation** · transition · collapse, with **overdamping** as an off-axis failure mode.
- **Six operational interventions:** decay reduction, supply increase, gain modification, efficiency improvement, headroom modification, mode-shift (basin modification).
- **Mode structure as dissipative structure (§7).** The substrate's attractor set is itself emergent under drive, not pre-existing. Mode formation is a developmental process with phases (incipient, established, mature, declining, vestigial) and is path-dependent through fluctuation-driven mode selection.
- **Hierarchy of substrate-mode levels (§7).** Established modes serve as substrates for higher-order modes; partial order, not strict nesting.
- **Imposed→emergent transition (§7, §3).** Mechanism: repeated imposed holding develops the substrate's mode structure until the held mode becomes a stable attractor; thereafter the holding sustains without the original constraint.
- **Predictive information $I_{\text{pred}}$ (§3).** Mutual information between past and future of a holding's trajectory. Positive for coherences; near zero for pseudo-coherence. A third formal handle on the coherence/pseudo-coherence distinction, operationally measurable from time-series.
- **Transfer entropy $T_{X \to Y}$ (§3).** Directional information flow between coupled holdings or processes. Quantifies asymmetry of influence in multi-holder situations.
- **Mode-pair distance (§3).** Information-geometric distance (Fisher metric, KL divergence) between mode-distributions. Quantifies dissimilarity of modes; mode-shift interventions traverse this distance.
- **Information bottleneck for active modulation (§3).** Active modulation is rate-distortion optimization with the held mode as the relevant target.
- **Synchronization order parameter $r$ (§10).** Quantitative measure of multi-holder coherence. $r=0$ incoherent, $r=1$ full sync, intermediate partial sync.
- **Critical coupling $K_c$ (§10).** Threshold for multi-holder synchronization, distinct from within-mode bifurcation thresholds.
- **Sync regimes (§10).** Phase-locked, frequency-locked, chimera (partial sync), generalized (functional alignment without phase locking). Refinements of the cooperative-coexistence regime in §9.
- **Coupling network topology (§10).** Determines who can synchronize with whom; the master stability function gives stability conditions for synchronized states on networks.
- **Lyapunov function $V(x)$ (§14).** Formal home of "what the holder preserves"; level sets are the basin structure, decay rate is damping, sub-level sets give basin volume.
- **Controllability and observability (§3).** Structural properties of the holder-substrate pair: which modes are reachable by active modulation, which are distinguishable from observation.
- **Internal model (§3).** A holder rejecting a class of disturbances contains a model of those disturbances; anticipatory holding given precise content.
- **Dual control balance (§3).** Exploration vs exploitation tradeoff in active modulation; varies with developmental phase.
- **Recursive multi-holder coherence (§10).** Multi-holder coherences with active constituents (each constituent is itself a holding); the typical case in character domain.
- **Non-reciprocal coupling regimes (§10).** Traveling-wave sync, oscillatory sync states, exceptional points — sync regimes specific to asymmetric coupling.
- **Flocking and active phase transitions (§10).** Collective alignment from local rules; active phase transitions distinct from equilibrium ones.
- **Topological defects (§10).** Singularities in alignment fields with their own emergent dynamics; dissenters, contrarians, paradoxes as structural features.
- **Load-as-process rates (§3).** Arrival rate $\lambda$, service rate $\mu$, utilization $\rho = \lambda/\mu$. Load-side complement to operating-state readings.
- **Backlog (§3).** Unprocessed-load state distinct from operating amplitude. Little's law $L = \lambda W$ relates average backlog to arrival rate and average wait.
- **Heavy-traffic regime (§3).** $\rho \to 1$ produces unbounded backlog growth even though processing keeps up with arrival on average. New failure mode: drowning.
- **Triage (§3).** Information-bottleneck-optimal load prioritization; the load-handling face of active modulation.
- **Self-exciting load processes (§3).** Hawkes processes for bursty, self-correlated load arrivals; the realistic load model for most character-domain situations.

**Operating-state dimensions.** Basin volume, chit-rate, $Q$, and headroom are orthogonal: any combination is realizable. Specifying the operating state of a holding requires all four, plus an indication of which coherence regime (imposed, emergent, or critical). Basin volume is logically prior — it characterizes the substrate's mode structure rather than within-mode operating state — and leads the list; the others are within-mode readings. The chit-rate alone is insufficient; operational state characterization is intrinsically multi-dimensional.

## 18. Phenomena named for the first time

The apparatus names several phenomena the framework had no vocabulary for previously.

- **Coherence as attractor under drive.** Rigorous dynamical-systems definition.
- **Coherence as NESS with broken detailed balance.** Rigorous thermodynamic definition. Equivalent to the dynamical-systems definition; two readings of the same operating object.
- **Three types of coherence.** Fixed-point, limit-cycle, strange-attractor.
- **Two coherence regimes.** Imposed (MEP-like, constraint-dependent) vs emergent (MaxEP-like, self-organized).
- **Basin of attraction.** Mode robustness as basin volume.
- **Bifurcation typology of thresholds.** Saddle-node, pitchfork, Hopf, period-doubling, crisis.
- **Bifurcation-type-specific critical-slowing exponents.** First quantitative empirical signature distinguishing transition types.
- **Multistability vs mode competition.** Structural multiplicity vs dynamic contention.
- **Pseudo-coherence vs coherence as parallel-execution vs self-stimulation.** Operational, perturbation-testable. Pseudo-coherence as activity at or near detailed balance; coherence as NESS with cyclic flow.
- **Saturation as a failure mode distinct from fraying.** Success-induced exhaustion of substrate-of-supply.
- **Headroom $s$ as an independent operating-state dimension.** Operating-slack reading.
- **Mode-competition regimes (winner-take-all / cooperative / hopping).**
- **Mode locking as the technical core of flow.**
- **$Q$ as an efficiency reading distinct from chit-rate.**
- **Damping rate $\Gamma$ as the dynamical reading of reserve and headroom.**
- **Underdamped / critical / overdamped regimes for oscillatory holdings.**
- **Asymmetric damping in active systems.**
- **Selectivity–responsiveness uncertainty.** Heisenberg-style formal uncertainty result.
- **Overdamping as a failure mode.** Coherence intact but responsiveness lost.
- **Loss of feedback structure as a failure mode.**
- **Supply creep.** Sustained holding gradually depletes the substrate-of-supply at constant load.
- **Chit unit's principled foundation.** Chit-rate = entropy production per holding-event; the unit is information-theoretically and thermodynamically grounded, not asserted.
- **Chit-rate measurement protocol via FDT-violation.** The integrated FDT-violation gives entropy production rate; combined with event rate, gives chit-rate. Spontaneous fluctuations + small probes suffice; no load-imposition required.
- **Trajectory-level budget grounding.** Maintenance budget = heat dissipated by holder along the trajectory. Measurable in physical units.
- **Mode structure as itself a dissipative structure.** The substrate's attractor set is an emergent product of its history under drive, not a pre-existing fact.
- **Developmental phases of a mode.** Incipient, established, mature, declining, vestigial. Operational vocabulary distinguishing developmental states.
- **Fluctuation-driven mode selection.** Variation-and-selection at the level of mode formation, distinct from mode competition between established modes. Path-dependence at the developmental level.
- **Hierarchy of substrate-mode levels.** Modes-as-substrates for higher-order modes; partial order across levels.
- **The imposed→emergent transition mechanism.** Developmental change in the substrate's mode structure that converts a constraint-dependent holding into a stable attractor. Detectable by qualitative change in response to constraint removal.
- **Predictive information as a formal handle on coherence vs pseudo-coherence.** $I_{\text{pred}} = I(\text{past}; \text{future})$; positive for coherences, near zero for pseudo-coherence. A third operational test alongside perturbation and detailed-balance breaking.
- **Transfer entropy for directional influence in coupled holdings.** Formal apparatus for "who is shaping whom" in mentor-student, parent-child, paired, or team configurations.
- **Mode-pair distance via information geometry.** Quantitative dissimilarity between modes; the substrate's mode structure as a manifold in distribution space.
- **Information bottleneck as the formal home of active modulation.** Active modulation is rate-distortion optimization; cFDR's "the holder shapes its own response" gets precise mathematical content.
- **Synchronization order parameter for multi-holder coherence.** Quantitative measure where mode-locking was previously qualitative.
- **Critical coupling as a meta-threshold.** A new threshold for multi-holder operation, beyond the within-mode bifurcation thresholds.
- **Chimera states as a stable partial-sync regime.** Some sub-coherences synchronize while others remain incoherent; not a transitional state.
- **Network topology of coupling as a determinant of sync structure.** Which holders couple to which determines who can synchronize with whom.
- **Sync-breaking transition routes.** Phase-slip, chimera formation, cluster splitting, sudden desync — each with its own empirical signature and intervention.
- **Generalized synchronization for functionally-aligned coupled holdings.** Functional alignment without literal phase locking.
- **Critical coherence as a third operating regime.** Self-organized to threshold; operates at near-zero reserve permanently. Distinct from imposed and emergent. Empirically distinguished by power-law event statistics, $1/f$ spectrum, and punctuated dynamics.
- **SOC-derived empirical signatures.** Power-law event-size distributions, $1/f$ spectra, punctuated dynamics, scale-invariant fluctuations — measurable from time-series alone.
- **Functional adaptive value of critical operation.** Maximum information-processing capacity, sensitivity to weak signals, dynamic range, and adaptability per unit dissipation; tradeoff is fragility to large fluctuations. Operating "on the edge" is precise, not metaphor.
- **Distinguishing critical operation from approach-to-collapse.** Both show critical-slowing-like signatures; distinguishable from temporal trend (approach intensifies, critical is stationary).
- **Lyapunov function as the holder's objective.** The function whose level sets are the basin, decay rate is damping; gives "what is being preserved" precise mathematical content distinct from operating-state readings.
- **Controllability and observability as structural properties of the holder-substrate pair.** Some modes are present but uncontrollable; some states are present but unobservable. Decidable from dynamics.
- **Internal model principle for anticipatory holding.** A holder rejecting a class of disturbances contains an internal model of them. Anticipatory capacity is part of what the holder is.
- **Dual control balance varying with developmental phase.** Exploration in incipient modes, exploitation in mature; phase transitions involve shifting the dual-control balance.
- **Recursive multi-holder coherence with active constituents.** The typical character-domain case where each constituent of a multi-holder coherence is itself a holding.
- **Non-reciprocal sync regimes.** Traveling-wave sync, oscillatory sync, exceptional points — distinctive to asymmetric coupling, common in power/attention/status-asymmetric pairings.
- **Flocking as collective alignment without central direction.** Coordination at community scale from local rules among active constituents.
- **Active phase transitions.** Qualitatively different from equilibrium phase transitions because constituents are themselves active.
- **Topological defects in alignment as structural features.** Dissenters, contrarians, paradoxes have emergent dynamics that drive reorganization or fragment coherence; not mere disturbances.
- **Load as process: arrival rate $\lambda$, service rate $\mu$, utilization $\rho$.** Discrete-event reading of load that complements the load-as-condition apparatus.
- **Backlog as a load-side state.** Distinct from operating-state readings; signals heavy-traffic approach before operating state degrades.
- **Heavy-traffic (drowning) as a distinct failure mode.** $\rho \to 1$ produces unbounded backlog without instantaneous capacity overrun.
- **Triage as information-bottleneck-optimal load handling.** Active modulation at the load-side; explicit triage outperforms implicit FIFO.
- **Self-exciting loads via Hawkes processes.** Bursty, self-correlated load is the realistic model; stationary Poisson is structural-physics convenience.

## 19. Origin note

The mathematics adopted in this document is the mathematics of dynamical systems, nonequilibrium thermodynamics, laser physics, and time-frequency analysis. All four are character-domain mathematics worked out first for physical substrates.

Adjacent established machinery extending this apparatus:

- **Dynamical systems and bifurcation theory** (Strogatz; Kuznetsov; Guckenheimer–Holmes; Arnold) — the foundation for attractors, basins, bifurcations, linear stability, and the typology of transitions in driven systems.
- **Stochastic thermodynamics and fluctuation theorems** (Seifert; Sekimoto; Jarzynski; Crooks) — fluctuation theorems, entropy production, trajectory thermodynamics. The natural home of §3 and the rigorous foundation of every thermodynamic claim.
- **Predictive information** (Bialek–Tishby–Strong) — the temporal-compressibility measure for stochastic processes; underlies the third formal handle on coherence in §3.
- **Transfer entropy** (Schreiber) — directional information flow; underlies the multi-holder coupling treatment in §3.
- **Information geometry** (Amari–Nagaoka) — Fisher metric on probability distributions; underlies the mode-pair distance in §3.
- **Information bottleneck** (Tishby–Pereira–Bialek) — rate-distortion optimization with relevance constraints; the formal home of active modulation in §3.
- **Synchronization theory and the Kuramoto model** (Kuramoto; Strogatz; Pikovsky–Rosenblum–Kurths; Acebrón et al.) — the mathematical foundation of §10. Order parameters, critical coupling, sync regimes, network sync, sync-breaking transitions.
- **Master stability function** (Pecora–Carroll) — stability conditions for synchronized states on networks.
- **Chimera states** (Kuramoto–Battogtokh; Abrams–Strogatz) — coexisting synchronous and incoherent sub-populations.
- **Generalized synchronization** (Rulkov et al.; Kocarev–Parlitz) — functional alignment without literal phase locking.
- **Self-organized criticality** (Bak–Tang–Wiesenfeld; Bak–Sneppen; Drossel–Schwabl; Jensen) — driven-dissipative systems organizing to a critical state without parameter tuning. Power-law event statistics, $1/f$ spectra, scale-invariant fluctuations. The mathematical foundation of critical coherence in §3.
- **Edge-of-chaos and information-processing-at-criticality** (Langton; Beggs–Plenz; Mora–Bialek) — functional reading of critical operation; results connecting criticality to maximal information capacity.
- **Lyapunov stability theory** (Lyapunov; Khalil; Sontag) — the formal apparatus for stability of nonlinear systems; the natural mathematical home of "what the holder preserves" in §14.
- **Internal model principle** (Francis–Wonham; Sontag) — a controller that rejects a class of disturbances must contain a model of them; the formal foundation of anticipatory holding in §3.
- **Dual control and Bayesian adaptive control** (Feldbaum; Wittenmark; Gittins) — exploration-vs-exploitation tradeoff in feedback control; the formal foundation of dual-control balance in §3.
- **Queueing theory** (Erlang; Kingman; Whitt; Kleinrock) — discrete-event arrival/service processes, utilization, Little's law, heavy-traffic regimes. The mathematical foundation of load-as-process treatment in §3.
- **Hawkes processes and self-exciting point processes** (Hawkes; Ogata; Bauwens–Hautsch) — bursty self-correlated event streams; the realistic load model for character-domain situations.
- **Non-stationary queueing theory** (Whitt; Massey; Mandelbaum) — rigorous treatment of time-varying arrival and service rates.
- **Fluctuation-dissipation theorem and its violation** (Harada–Sasa; Cugliandolo–Kurchan) — the operational content of §3's measurement protocol; relates spontaneous fluctuations and response in NESS.
- **Large-deviation theory** (Cramér; Touchette; Donsker–Varadhan) — rate functions for rare events in stochastic systems; the natural home of fluctuation-driven basin-escape and spontaneous threshold-crossings.
- **Nonequilibrium steady-state theory and Prigogine's minimum-entropy-production principle** — the linear-NESS regime; the imposed-coherence pole.
- **Self-organization and maximum-entropy-production theories** — the proposed selection principle for far-from-equilibrium organized states; the emergent-coherence pole. Less rigorous than MEP at the formal level.
- **Dissipative-structures theory** (Prigogine; Nicolis–Prigogine; Glansdorff–Prigogine) — far-from-equilibrium pattern formation, symmetry breaking under drive, fluctuation amplification, hierarchy of dissipative structures. The natural mathematical home of mode-formation content in §7.
- **Driven-dissipative non-equilibrium steady states** (Sieberer–Buchhold–Diehl) — the modern formalism for open systems whose operating structure is defined by the operation itself.
- **Haken's theory of laser threshold and synergetics** — second-order phase-transition treatment of threshold; provides the universal critical-slowing apparatus.
- **Time-frequency analysis and quantum-mechanical uncertainty relations** — the mathematical core of §15.
- **Sub- and super-radiance in cavity QED** — formalizes the structured-but-uncoupled vs structured-and-coupled distinction underlying §5.
- **Hebbian / BCM plasticity, synaptic tagging** — use-dependent gain modulation at the biological substrate.
- **Active-matter physics** (Marchetti et al.; Vicsek et al.; Toner–Tu; Ramaswamy) — collective dynamics of active constituents; flocking, active phase transitions, long-range order from local rules. The natural setting for recursive multi-holder coherences.
- **Non-reciprocal phase transitions** (Fruchart–Vitelli; Saha–Sharma–Golestanian) — sync regimes specific to asymmetric coupling; traveling waves, oscillatory sync, exceptional points.
- **Topological defects in active matter** (Doostmohammadi et al.; DeCamp et al.; Aranson) — self-propelled singularities in alignment fields; structural features with emergent dynamics.
- **Closed-loop and model-predictive control** — already imported in cFDR for active modulation of response.

These references are pointers, not dependencies.

## 20. Open items

Steady-state operation, its dynamics, and its thermodynamic foundation are now in the apparatus's scope. Open items:

- **Response to imposed load.** Handled by cFDR. Unified treatment in §7.2 of the framework spec, now informed by attractor framing and basin language.
- **Strange-attractor coherences as a populated class.** The type is mathematically forced by the bifurcation typology; whether practitioner-relevant cases meet the technical criteria (bounded non-periodic trajectories, exponential divergence, fractal geometry) is open and requires identification, not assumption.
- **Empirical methods for distinguishing developmental phases.** Mode formation is now formalized (§7) with phases (incipient/established/mature/declining/vestigial), but reliable empirical identification of phase from time-series and substrate observation is open.
- **Severity dynamics.** How healthy regimes (e.g., underdamping) tip into pathological extremes through severity within the regime.
- **MaxEP rigor.** The maximum-entropy-production principle invoked in §3 for emergent coherence is less rigorous than MEP at the formal level. Whether it can be tightened, replaced, or limited to specific sub-cases is open.
- **Empirical validation of FDT-violation measurement protocol.** §3's protocol is operationally specified but not yet validated on real character-domain holdings. First validation case is itself a contribution.
- **Composition of supply creep, fatigue, and saturation as supply-side failure modes.** Three substrate-of-supply degradations; whether they share recovery dynamics is open.
- **Failure-mode taxonomy consolidation.** The unified taxonomy (framework §7.4) has eight entries and a parallel four-entry taxonomy at the multi-holder sync-breaking level. A multi-axis classification is noted (site / mechanism / time scale), but a deeper consolidation — identifying shared structure that subsumes or unifies entries — remains open.
