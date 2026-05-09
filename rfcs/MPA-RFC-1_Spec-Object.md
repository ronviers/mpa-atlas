# MPA-RFC-1: Spec Object

**Status:** Draft v0.2 — first thin-RFC pass
**Targets:** [v9 (compressed, operational)](../framework/v9_compressed.md). The unabridged prose-and-prior-art version is at [`v9_MPA_A_Driven-Dissipative_Synthesis_with_Boolean_Limit.md`](../framework/v9_MPA_A_Driven-Dissipative_Synthesis_with_Boolean_Limit.md); refresh-from-compressed cadence; allowed to lag; not authoritative for operational lookups.
**Companion:** [Architectural Block-In v0.2](../architecture/MPA_Architectural_Block-In.md), [RFC-S v0.2](MPA-RFC-S_Scale-Management.md), [RFC-2 v0.1](MPA-RFC-2_FDR-Signatures.md), [RFC-3 v0.1](MPA-RFC-3_Consistency-Completeness.md), [RFC-V v0.1](MPA-RFC-V_Reference-Vocabulary.md), [RFC-RI v0.1](MPA-RFC-RI_Realizer-Interface.md)

---

## 0. Foundational principles

This RFC inherits five principles from the [Architectural Block-In](../architecture/MPA_Architectural_Block-In.md). Declared, not re-derived:

1. **Color-management discipline.** Three layers (substrate-native / canonical / realizer-output); transforms declared, named, versioned, swappable.
2. **Observer-driven scale management.** $\tau_{obs}$ is the camera; canonical representation is observer-relative.
3. **Demand-bounded sufficiency.** Canonical representation is sized to the demand placed on it. **The MPA is not the bottleneck.**
4. **Singular working-space path.** Within an RFC version, exactly one shape. Plurality lives in drivers, intent flags, and version succession — not at the working-space layer.
5. **Thin-RFC discipline.** Exchange surfaces are written at gross-underengineering resolution. *It was never brittle if it never broke.* Edge cases live in v9; cross-cutting decisions live in the architectural block-in; defensive enumeration lives in mechanical validation.

---

## 1. Object

A **spec object** declares, substrate-neutrally, what dynamical structure a substrate must realize. It is the artifact mpa-character emits and the artifact a driver populates. Realizer search consumes it downstream.

## 2. Shape

```
S = (V, E, Γ, D, τ_obs, P, ⟨demand-envelope⟩)
```

| Symbol | Name | Content |
|---|---|---|
| `V` | Vertex set | Trail-bearing propositions with regime targets ($c$/$s$/$r$/`*`) |
| `E` | Edge set | Pairwise shear $\gamma_{AB}$ in canonical sign convention |
| `Γ` | Subgraph flags | `prescribed_frust` / `forbidden_frust` / `unspecified` per declared subgraph |
| `D` | Drive | One of: `point` · `interval` · `schedule(τ_obs)` · `tower {D_n}` |
| `τ_obs` | Observer kernel | One of: `point` · `band` · `multi-band` |
| `P` | Persistence profile | Sequence $\{(D_n, \varepsilon_n, S_n)\}_{n=0}^{N}$ |
| `⟨demand-envelope⟩` | Demand declaration | Per object: which signatures, at which precision, at which observer positions |

The schema is canonical: a payload conforming to the schema is a valid spec object by definition. The schema itself is in [Appendix A](#appendix-a-schema).

## 3. Invariants

A spec object is **valid** iff all of:

1. **Type-closure.** Every vertex / edge / subgraph references types defined in v9 §Operators and §Composite catalogue.
2. **Sign-canonicity.** All $\gamma$ values use canonical spec-layer sign ($\gamma<0$ cooperative, $\gamma\approx 0$ orthogonal, $\gamma>0$ conflicting). Substrate-native sign inversions happen at the driver layer, never inside the spec object. (See v9 Appendix F.1 for the Markovian-substrate convention.)
3. **Observer-relativity.** All quantities read at the declared $\tau_{obs}$. Multi-band declarations name each band explicitly.
4. **Scale-monotonicity.** Vertex regimes follow $c \to s \to r$ as $\tau_{obs}$ widens (no inverse transitions). $\gamma$ does not strengthen at wider $\tau_{obs}$.
5. **Capacity-respect.** $|\Gamma^*| \le \sqrt{2D / \alpha\,\gamma_{\min}\,d_{\text{avg}}}$ at the operating point (v9 §Capacity).
6. **Tower-convergence.** When $P$ declares $N \ge 1$ ascents, $\varepsilon_n < 1$ at each ascent — *or* the spec explicitly declares a Complexity Wall at ascent $n$ (v9 Appendix G).
7. **Demand-envelope-declaration.** Every spec object carries a non-empty demand envelope. The framework promises no resolution beyond what the envelope demands.

## 4. Operations

| Operation | Signature | Preserves |
|---|---|---|
| Validate | $S \to \{\text{valid}, \text{diagnostics}[]\}$ | Invariants 1–7 |
| Theorem-9 mechanical check | $S \to \text{diagnostics}[]$ | Joint-commitment feasibility per edge ($\gamma_{AB}>0 \wedge D < \gamma_{AB}$ flagged; v9 Theorem 9) |
| Capacity check | $S \to \text{diagnostics}[]$ | Invariant 5 at operating point |
| Compile to realizer targets | $S \times \text{intent-flag} \to \text{realizer-interface-document}$ | Per [RFC-RI](MPA-RFC-RI_Realizer-Interface.md) |

Operations are intent-neutral except compilation, which carries an intent declared at the realizer-interface boundary (RFC-RI). Operator actions on the canonical representation ($C, S, K, R$ from v9 §Operators) are intent-neutral by construction — they preserve canonical-representation invariants because the algebra is closed.

## 5. Falsifiers

A spec object is **invalid** if any of:

- Schema violation (Appendix A).
- Sign-convention violation ($\gamma$ supplied in non-canonical sign).
- Cross-band non-monotonicity (vertex transitions $r \to c$, or $\gamma$ strengthens with $\tau_{obs}$ widening).
- Subgraph flag conflict (`prescribed_frust` and `forbidden_frust` on overlapping members).
- Drive form / persistence profile mismatch (`tower` form $D$ without paired persistence profile, or vice versa).
- Missing or empty demand envelope.

Diagnostics from operations §4 surface other conditions (Theorem-9 joint-commitment infeasibility, capacity overrun) as **flags, not necessarily failures** — a spec author may intend the regime; the diagnostic surfaces it for resolution.

## 6. Pointer

[v9 (compressed)](../framework/v9_compressed.md) carries the formal derivation. Sections in the compressed file:

| What | Where |
|---|---|
| Vertex regime semantics ($c$/$s$/$r$, $\lambda$ axis) | §Three typed objects |
| Operator algebra $\Sigma = \{C, S, K, R\}$ | §Operators |
| Composite catalogue | §Composite catalogue |
| Capacity bound | §Capacity |
| FDR signatures per regime / subgraph | §Fluctuation-dissipation signatures |
| Substrate-conditional reading rules | §Substrate-conditional reading rules |
| Compression Axiom / meta-ledger flow | §Compression Axiom / meta-ledger flow |
| Tower convergence / Complexity Wall | §Compression Axiom (Convergent Tower paragraph) |
| Joint-commitment threshold (Theorem 9) | §Deformation calculus (Theorem 9 row) |

---

## Appendix A: Schema

Schema is the canonical exchange shape. The full machine-readable schema lives at [`schema/spec-object.v0.2.json`](../schema/spec-object.v0.2.json) as a JSON Schema document. The schema declaration encodes the table in §2 plus per-field type constraints; it is the single source of truth for what a valid payload looks like. Any prose interpretation of the schema in this document is non-authoritative; the schema file is.

```
vertex      = { id, trail_vector_type, regime_target, lambda?, local_drive?, band_keying? }
edge        = { id, endpoints, shear, reciprocity, band_keying? }
subgraph    = { id, members, flag, k_frust_value?, band_keying? }
drive       = { form, value | range | schedule | tower }
tau_obs     = { form, value | band | multi_band, units }
persistence = { tower: [ { D_n, ε_n, S_n } ... ] }
demand      = { per_object: [ { object_id, signatures_required, precision, observer_positions } ... ] }
```

## Appendix B: Demand envelope

Every spec object declares, per object, the signatures required and the precision asked for at each observer position. The framework — and any driver calibrated against this RFC — commits to no fidelity beyond what the envelope declares.

This is the operational consequence of demand-bounded sufficiency. Drivers calibrate against an envelope; mpa-character emits envelopes sized to the spec author's actual demands. The envelope is *the* place where "enough, no more" is encoded as a deliberate design commitment rather than an implicit policy.

The envelope's internal structure is left thin pending RFC-2 (signatures contract) — once RFC-2 fixes the signature shape, the envelope's `signatures_required` and `precision` fields canonicalize against it.

## Appendix C: What this RFC does not specify

- FDR-signature measurement protocols → RFC-2
- Cross-field consistency invariants beyond §3 → RFC-3
- Realizer-interface document format and intent-flag enumeration → RFC-RI
- Substrate-conditional reading rules → drivers (v9 Appendix F is the canonical surface-code reference)
- Trail-class metric → open in v9; deferred until RFC-3 needs it concretely

## Appendix D: Open

Items the next revision absorbs as needed:

1. $\lambda = \pm D$ boundary behavior — sharp at the spec layer; FDR behavior at the boundary is RFC-2's.
2. Trail-vector cross-vertex compatibility under operator $C$ — explicit declaration required on type mismatch; default-merge on type match. More permissive defaults, if any, deferred.
3. Local-drive combinator in overlapping mentor-pump regions. Pointwise max is the working assumption; substrate evidence may revise.

(Closures: trail-class metric in v9 §Compression Axiom — $\rho([A],[B]) = \lim_n \epsilon^{-n}\|\mathcal{C}^n(d_A-d_B)\|$, distinct from $\varepsilon_n = \|\mathcal{C}_n\|_{op}$. $C$ vs. $\mathcal{C}$ notation collision in [RFC-V v0.1 §4](MPA-RFC-V_Reference-Vocabulary.md).)

---

## Versioning

| Version | Status | Change |
|---|---|---|
| v0.1 | superseded | Initial draft, standards-body shape (~400 lines) |
| **v0.2** | **current** | Rewrite under thin-RFC discipline. Foundational principles section. Six-field template applied. Demand envelope promoted to invariant. Sub-2-page target. |

**Compatibility.** Any future change to the spec-object tuple (adding / removing fields) requires a v1.0+ revision with explicit migration notes. Drivers declare which RFC-1 version they target; cross-version compatibility is not assumed.

## Page-budget self-check

Target: ≤3 pages for the spec object (the foundational, fully-fielded object — the heaviest RFC in the sequence). Body §0–§6 runs ~95 lines (≈2 pages); appendices A–D add ~50 lines (≈1 page). **Pass.**

For comparison: v0.1 ran ~400 lines and was still incomplete in the foundational-principles dimension. v0.2 carries strictly more architectural content in 38% of the prose, by removing re-derivation, [Provisional] tags, and defensive enumeration that v9 (rigor) and the architectural block-in (cross-cutting decisions) carry instead.

The remaining RFCs (RFC-2 / RFC-3 / RFC-V / RFC-RI) target ≤1 page each — half a page where the object admits it. The spec object is the only RFC where ≤3 is the right target, because it is the foundational object. Growth past these targets in any RFC carries a debt-marker naming the force that pushed past brevity, with a revert-when-force-passes commitment.
