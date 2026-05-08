# Handoff: RFC-S thin-pass

**Status:** Planning document for the next session's RFC-S rewrite under thin-RFC discipline.
**Audience:** A future Claude (or human) coming into this work cold.
**Companion:** [Architectural Block-In v0.2](MPA_Architectural_Block-In.md) (foundational principles), [RFC-1 v0.2](../rfcs/MPA-RFC-1_Spec-Object.md) (the pattern this should mirror), [v9 compressed](../framework/v9_compressed.md) (operational source of truth), [RFC-S v0.1](../rfcs/MPA-RFC-S_Scale-Management_Block-In.md) (the heavyweight version preserved as honest-scope reference).

---

## The central insight

**Color management is a finite discipline. Scale management is an infinite discipline. Importing color management's finite engineering and patching the infinite parts with edge-case enumeration is the wrong move. Import infinity-machinery directly.**

Color management:
- Bounded gamut (everything inside human vision)
- Spectral integrals over [380nm, 780nm]
- Finite-length display chains
- Reference whites = fixed points (no flow)
- All composition happens inside a bounded universe

MPA scale management:
- $\tau_{obs}$ ranges across many decades, in principle unbounded
- Persistence-profile towers of arbitrary depth $N$
- $\epsilon < 1$ is convergence language
- Boolean limit is $D \to \infty$
- Complexity Wall is $\epsilon \to 1$
- The Compression Axiom is RG flow

Color management has no machinery for this and never needed any. RFC-S v0.1 took color management as the analog and was forced into a 5,800-word block-in projecting 170–200 pages at full resolution because every infinity-shaped problem had to be handled by case enumeration. That's the wrong total weight, distributed wrong. The framework underneath (v9) is RG-shaped; the protocol on top should be too.

The thin-pass thesis: **RG flow is the foundational structure of RFC-S, the way the spec object's six-tuple is the foundational structure of RFC-1.** Most of v0.1's volume collapses under that re-framing.

---

## Infinity-machinery available, ranked by fit

### Tier 1 — already in v9, just underexploited in v0.1

**Renormalization group flow.** Named in v9 §Compression Axiom. RG is *the* mathematics of "infinite coarse-graining as a flow." Fixed points, basins of attraction, marginal / relevant / irrelevant directions. This is the central tool RFC-S should lean on.

**Banach fixed-point theorem.** In v9 via $\epsilon < 1$. Canonical "infinite sequence converges to a unique limit because the map is a contraction." Standard, well-understood, gives uniqueness for free.

These two together cover most of the heavy lifting. v0.1 references both but doesn't *organize itself around* either.

### Tier 2 — natural extensions, import as needed

**Inverse limits / pro-objects.** Categorical machinery for "limit of a sequence of finite approximations." The persistence profile $\{(D_n, \varepsilon_n, S_n)\}_{n=0}^{N}$ is naturally a pro-object: each finite $N$ is a computable approximation; the limit is the structure that survives all ascents. Compositional by construction (inverse limits compose). Use this when RFC-S needs to talk about persistence profiles abstractly.

**Compactification.** Add limit points so the space behaves continuously at infinity. The Boolean limit is the compactification of $D$-space at $D = \infty$. The Complexity Wall is the compactification of $\epsilon$-space at $\epsilon = 1$. Microscopic limit is $\tau_{obs} = 0$; fully-coarse-grained is $\tau_{obs} = \infty$. Once compactified, these are *points in the space*, not exotic limits — and behavior at them is specified once, not as separate edge cases per intent (v0.1 §9 enumerates each).

**Asymptotic analysis.** Leading-order behavior near singular points without computing all the way to the singularity. v9 Appendix G's $\Phi_{total} = \Phi^{(0)} / (1 - \epsilon)$ is geometric-series-at-infinity. Use for behavior near compactification points where exact computation is infeasible but leading-order behavior is.

### Tier 3 — flag as available, do not import yet

**Sheaves over $\tau_{obs}$-space.** Local canonical representations at each observer position; restriction maps are auto-remaps; sheaf condition gives cross-position compatibility. Tempting because pipeline composition with type-changing transforms (v0.1 §7, the genuinely hardest section) is naturally a sheaf-theoretic problem. *Probably over-engineered for v0.2.* Flag for v0.3 if pipeline composition resists thinning. Importing sheaves now would push RFC-S back toward heavyweight against the discipline.

**Coalgebras / bisimulation.** Equivalence by observation. Trail-class equivalence is naturally bisimulation: two trails are equivalent if their observable signatures agree at every $\tau_{obs}$. Could replace the open "trail-class metric" question by characterizing equivalence topologically rather than metrically. Flag for when v9's open metric question becomes blocking.

**Operads / monads.** Recursive composition machinery. The Compression Axiom is recursive (ledger about ledger about ledger...); operads / monads handle this algebraically. Likely unnecessary unless the meta-ledger tower acquires its own algebraic structure separate from RG flow.

---

## Section-by-section thin-pass map

How each piece of v0.1 collapses under RG-thinking + thin-RFC discipline.

| v0.1 section | Words | Thin-pass treatment | Target |
|---|---|---|---|
| §1 Connection Space | ~600 | **"The fixed-point set of the RG flow."** The canonical representation isn't a region you carve out by enumerating invariants. It's defined as what is invariant under $\mathcal{C}_n$. Invariants follow from the definition. | Half page |
| §2 Gamut | ~500 | **"The image of the substrate's RG trajectory."** A substrate's gamut isn't a static multi-dimensional region with non-convex hull. It's the trajectory in canonical-representation space, parametrized by $(\tau_{obs}, D)$ and traced by the substrate's flow. Characterized by trajectory shape, not by multi-sweep enumeration. | Half page |
| §3 Rendering Intents | ~900 | **KEEP.** The five-intent enumeration is the load-bearing piece. But each intent compresses to ≤3 lines: name, preserved invariant, sacrificed invariants. **Intent-determines-mapping** rule (§4 below) eliminates per-intent prose. | One page |
| §4 Gamut Mapping Operations | ~500 | **COLLAPSE.** Each intent's mapping operation is *determined by* the invariant it preserves: scale uniformly to fit the gamut while preserving that invariant. v0.1 spent a paragraph per intent re-deriving this. Replace with one rule + table. | Few lines |
| §5 Char. vs Calibration | ~400 | **KEEP at 1/3 weight.** Distinction is good, brief. | 1/3 page |
| §6 Driver Profile | ~500 | **KEEP, schema-pointer form.** The schema is the load-bearing exchange artifact. RFC-S itemizes fields; machine-readable schema lives in a separate file. (Same pattern RFC-1 v0.2 §Appendix A uses.) | Half page |
| §7 Pipeline Composition | ~600 | **COLLAPSE under RG-flow associativity.** Operator actions ($C, S, K, R$) are intent-neutral and compose by RG-flow associativity. The "type-changing problem" is artifactual: driver and realizer are bookend transforms; everything between is RG flow. Intent-flagged transforms (driver, auto-remap, realizer) compose under the constraint that adjacent intents preserve compatible invariants — the same rule v0.1 §7.4 already states, just declared not derived. | Half page |
| §8 Round-trip Validation | ~500 | **KEEP.** Concrete protocol; load-bearing. Tighten prose. | Half page |
| §9 Edge Cases | ~600 | **COLLAPSE under compactification.** $\varepsilon \to 1$, $D \to \infty$, $D = 0$, $\tau_{obs} \to 0$, $\tau_{obs} \to \infty$, $\lambda = \pm D$ are *points* in the compactified parameter space. Behavior at compactification points is specified once per point, not as separate "edge cases" per intent. v0.1 §9 enumerates 7 cases with per-intent handling for each = ~28 case-cells of prose; thin pass produces a 7-row table. | Half page |
| §10 Operating Conditions | ~400 | **KEEP at 1/2 weight; fold into §6 driver profile.** Operating envelope is a driver-profile field, not its own section. | Few lines (in §6) |
| §11 Open Questions | ~700 | **APPENDIX.** | Half page |
| §12 Scope Estimate | ~400 | **DELETE (or preserve as honest-scope reference).** The 170–200-page projection documents what we're *not* importing. Preserved in v0.1 file as historical record per the v0.2 framing note already added. | — |
| §13 Closing | ~300 | **DELETE.** | — |

Active body target: §0 (foundational principles) + 6 sections at half a page each ≈ **3 pages**. Plus appendices: schema reference, open questions, what's deferred. **Total ≤ 5 pages**, comparable to RFC-1 v0.2. Compare to v0.1's 5,800 words projecting to 170 pages.

---

## What's still hard

Honest enumeration of where infinity-machinery doesn't fully solve the problem.

**1. Auto-remap as function vs. as generator.** v0.1 §6 specifies auto-remap as a finite remap function the driver provides. Under RG-thinking, the cleaner formulation is: the driver specifies the *infinitesimal* (tangent-flow) rule for how things change with small kernel-width changes; finite remaps are integrated. Compactifies the problem from "specify a function" to "specify a generator." But: drivers may not be able to write infinitesimal rules cleanly in all substrate classes, and integration may not be analytically tractable. **Open question for the rewrite:** does RFC-S commit to infinitesimal form, finite form, or admit both?

**2. Pipeline composition with intent-flagged transforms.** RG composition is associative for intent-neutral transforms. Intent-flagged transforms (driver, auto-remap, realizer) are chosen by the user and their composition might not be associative. v0.1 §7.4 states a compatibility rule (adjacent intents preserve compatible invariants) without deriving it. RG-thinking reframes the question — *what* invariants are compatible follows from RG flow's preserved structure — but doesn't fully solve which intent compositions are admissible. **Open question:** does the thin pass need a small composition-rules table, or can it punt to "two intents are compatible iff their preserved invariant sets union without conflict"?

**3. Trail-class metric, still open in v9.** RG-thinking softens the problem (you can do RG with a topology, not necessarily a metric — convergence works without distance). But picking *which* topology is its own choice. The thin pass should probably leave this as-is in v9's open-questions list; the architectural commitment is "topological, not metric, until forced otherwise."

**4. Behavioral substrates and evolving substrates.** Color management has no analogs; infinity-machinery doesn't directly help. v0.1 §10.3 candidly flags "evolving substrates may need framework extension." **Recommendation:** out of scope for RFC-S. Eventually a separate RFC-Beh or extension axis. The thin pass should mention this only as a deferred boundary, not try to handle it.

**5. The five-intent set.** Probably right; possibly off-by-one or off-by-many. v0.1 was honest about this. **Recommendation:** thin pass commits to five and uses RFC versioning to revise if a sixth proves necessary. *Singular working-space path* says one shape per version; revising the intent set is a version event.

---

## Recommended work order for the next session

Aim for one session, 3-5 pages of RFC-S v0.2, draft quality.

**Step 1 — orient (10 min).**
- Read this handoff.
- Read [v9 compressed](../framework/v9_compressed.md) cover-to-cover (it's dense; ~12KB).
- Read [RFC-1 v0.2](../rfcs/MPA-RFC-1_Spec-Object.md) for the template pattern.
- Skim [RFC-S v0.1](../rfcs/MPA-RFC-S_Scale-Management_Block-In.md) — do *not* read carefully; it will pull you toward standards-body weight. Read only what the section-map table above flags as KEEP.

**Step 2 — confirm or revise the central import (5 min).**
- The central thesis is "RG flow as the foundational structure." Is it right? If you find a stronger candidate (compactification first? Banach first?), change it before writing.
- Specifically check: does RG flow handle the auto-remap question well, or is sheaves needed? My current read is RG handles it for v0.2; sheaves are reserve.

**Step 3 — write §0 foundational principles (5 min).**
Mirror RFC-1 v0.2 §0. Inherit the same five principles. Add one RFC-S-specific principle:

> **6. RG flow as foundational structure.** Canonical representation is the fixed-point set of the RG flow defined by the Compression Axiom. Gamuts, transforms, intents, edge cases all reference the flow rather than re-deriving from finite engineering analogs.

**Step 4 — write the body (45 min).** Six sections, ~half a page each:

1. **Canonical representation.** Fixed-point set of RG flow. Pointer to v9 §Compression Axiom for the formal statement.
2. **Substrate gamut.** Image of substrate's RG trajectory in canonical space, parametrized by $(\tau_{obs}, D)$.
3. **Intents.** Five-intent table: name | preserved invariant | sacrificed invariants | use case. Three lines per intent. One sentence on intent-determines-mapping.
4. **Driver profile.** Field enumeration; schema in separate file; operating envelope folded in.
5. **Round-trip validation.** Protocol steps; per-intent metrics by reference.
6. **Behavior at compactification points.** Table: $\varepsilon \to 1$, $D \to \infty$, $D = 0$, $\tau_{obs} \to 0$, $\tau_{obs} \to \infty$, $\lambda = \pm D$. One row per point: physical interpretation, default policy, intent overrides.

**Step 5 — appendices (15 min).**
- Appendix A: schema reference (pointer to file, like RFC-1).
- Appendix B: open questions (ports the relevant subset from v0.1 §11; trail-class topology vs metric; auto-remap form).
- Appendix C: what's deferred (behavioral / evolving substrates → future RFC; sheaves available but not imported).

**Step 6 — page-budget self-check (5 min).**
Count printed pages. Target ≤ 5. If over: cut prose, not content. If much under: good, but check that no load-bearing piece was dropped (the five intents, the round-trip protocol, the schema).

**Step 7 — debt-markers (5 min).**
For any section that resisted thinning, write a one-line debt-marker: "this section runs X lines past target because [force]; revert when [force passes]." Most-likely candidate: pipeline composition / intent compatibility, if the simple rule doesn't cover the cases.

**Total time budget: ~90 min** for a draft RFC-S v0.2. v0.1 took (presumably) several sessions; the thin pass should fit in one because the work is *removing*, not *adding*.

---

## Failure modes to watch for

**The pull toward heavyweight.** RFC-S v0.1 is well-written and persuasive. Reading it carefully will pull the next session back toward "but we *do* need to enumerate gamut topology for non-convex cases." Resist. The pull is real because v0.1's author was being responsible at standards-body weight; thin-RFC is a different responsibility (responsibility for not pre-committing to weight that hasn't been earned).

**Misidentifying the load-bearing pieces.** The five intents are load-bearing because they're the user-facing surface. The schema is load-bearing because it's the exchange artifact. Round-trip validation is load-bearing because it's the only mechanical check. *Everything else can be thinned.* If you find yourself protecting v0.1 prose that isn't one of these three, ask why.

**Math envy.** Once you start importing infinity-machinery, the temptation is to import more than needed. Sheaves are seductive. Operads are seductive. Resist. Tier 1 (RG, Banach) handles v0.2; Tier 2 (inverse limits, compactification, asymptotics) handles edge formulations; Tier 3 is reserve. If you find yourself reaching for Tier 3, ask: is this earning its weight, or is it ornamentation? Thin-RFC discipline says ornamentation is a cost, not a free upgrade.

**Pipeline composition resistance.** This is the section most likely to push past target. If after 30 minutes it still resists, that is data — pay the debt-marker, accept ~6 pages instead of ≤5, and flag pipeline composition as the place v0.3 might need sheaves. Don't fight to keep it thin if the math doesn't allow it.

---

## What success looks like

A draft RFC-S v0.2 that:

- Lives at `H:/mpa-atlas/rfcs/MPA-RFC-S_Scale-Management.md` (drop the "Block-In" suffix; this *is* the spec, not its block-in)
- Runs ≤ 5 pages including appendices
- Carries a foundational-principles section that names RG flow as foundational
- Compresses 13 v0.1 sections to 6 active sections + 3 brief appendices
- Preserves the five-intent enumeration intact (it's load-bearing)
- Replaces edge-case enumeration with a compactification-points table
- Points at v9 compressed for all RG-flow rigor (zero re-derivation)
- Carries an explicit page-budget self-check at the end
- Names every debt-marker explicitly, with revert conditions

Plus: v0.1 stays in repo as `MPA-RFC-S_Scale-Management_Block-In.md` (its current name), preserved as the honest-scope reference. The next session does not delete it, does not edit it. Two files, one operational and one historical, mirroring how v9 compressed and v9 unabridged now relate.

---

## What this handoff *does not* commit to

- That RG flow is definitely the right import. (My read is yes; the next session should sanity-check before writing.)
- That five intents is the right number. (Probably yes; revisable via version succession if proven wrong.)
- That ≤ 5 pages is achievable for RFC-S. (Probably yes for v0.2; pipeline composition is the candidate to break the budget.)
- That the next session can do all of this in 90 minutes. (Optimistic; budget for 2x.)

If any of these turn out wrong, that's data, and the right response is to update *this* handoff document for the session after, not to abandon thin-RFC discipline.
