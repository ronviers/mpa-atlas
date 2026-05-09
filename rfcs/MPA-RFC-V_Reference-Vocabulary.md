# MPA-RFC-V: Reference Vocabulary

**Status:** Draft v0.1 — first thin-RFC pass.
**Targets:** [v9 (compressed)](../framework/v9_compressed.md) for operational meanings.
**Companion:** All other RFCs, drivers, realizers read this for canonical labels.

---

## 0. Foundational principles

Inherits the five from the [Architectural Block-In](../architecture/MPA_Architectural_Block-In.md). RFC-V instances the *singular working-space path* (principle 4): one canonical label per concept; no synonyms within a version.

## 1. Object

The **reference vocabulary**: canonical-label registry for cross-cutting concepts plus the small set of disambiguation rules for typographically-colliding glyphs.

## 2. Cross-cutting labels

**Operators (v9 §Operators).** $C$ try-merge / $S$ hold-both / $K$ parity-XOR / $R$ reset-sever; $\Sigma = \{C, S, K, R\}$ (extended to $\{C, S, K, R, \top, \bot\}$ in the Boolean section); $\mathcal{C}$ compression operator (distinct from $C$); $\mathcal{C}_n$ level-$n$ compression operator.

**Regimes (v9 §Three typed objects).** $c$ committed ($\lambda_A \ll -D$); $s$ suspended ($|\lambda_A| \lesssim D$); $r$ reset ($\lambda_A \gg D$); $k_{\text{frust}}$ subgraph frustration (topological).

**Per-regime universality invariants (v9 §Fluctuation-dissipation signatures).**

| Symbol | Name | Regime |
|---|---|---|
| $X_c$ | suppression index | $c$ |
| $\alpha_s$ | aging exponent (CK ratio) | $s$ |
| $P_s$ | plateau height | $s$ |
| $X_r$ | FDT ratio | $r$ |
| $N_f$ | negativity index | $k_{\text{frust}}$ |

**Intents (RFC-S §3).** I1 regime-preserving; I2 drive-faithful; I3 capacity-preserving; I4 persistence-preserving; I5 signature-preserving.

**Compression-axiom symbols (v9 §Compression Axiom).** $\epsilon = \|\mathcal{C}\|_{op}$ (single-level contraction rate); $\varepsilon_n = \|\mathcal{C}_n\|_{op}$ (level-$n$); $\rho$ trail-class metric (leading-eigenmode amplitude); $\mathcal{T}$ trail-vector Banach space; $\mathcal{T}/\!\sim$ trail-class space; $\mathcal{M} = \{c, s, r\}$; $\mathcal{M}_2 = \{c, r\}$ (Boolean section).

## 3. Per-RFC labels (authority pointers)

| Domain | Authority |
|---|---|
| Spec-object fields ($V, E, \Gamma, D, \tau_{obs}, P, \langle\text{demand-envelope}\rangle$) | [RFC-1 §2](MPA-RFC-1_Spec-Object.md) |
| FDR-signature fields | [RFC-2 §2](MPA-RFC-2_FDR-Signatures.md) |
| Driver-profile fields | [RFC-S §4](MPA-RFC-S_Scale-Management.md) |
| Layer names (substrate-native / canonical / realizer-output) | [Architectural Block-In](../architecture/MPA_Architectural_Block-In.md) |

## 4. Disambiguation rules

- **$C$ vs. $\mathcal{C}$.** $C \in \Sigma$ (try-merge operator; v9 §Operators); $\mathcal{C}$ compression operator (v9 §Compression Axiom). Distinct objects, distinct categories. Typographical distinction preserved everywhere; no document may use the same glyph for both.
- **$\epsilon$ vs. $\varepsilon_n$.** $\epsilon$ — single-level (default; level 0). $\varepsilon_n$ — explicitly level-$n$. Subscript required when the level is non-zero.

## 5. Invariants

A vocabulary use is **valid** iff:

1. **Single-source.** Label matches §2 (cross-cutting) or the §3 authority pointer.
2. **No-synonyms.** No alternative label introduced for an existing concept.
3. **Disambiguation discipline.** §4 typographical conventions preserved.

## 6. Operations & falsifiers

| Operation | Action |
|---|---|
| Validate use | document → diagnostics — labels diverging from canonical-source flagged |
| Add (cross-cutting) | additive within v0.x; new label declared with canonical-source citation |
| Add (per-RFC) | per-RFC authority adds; §3 row added if cross-RFC traffic warrants |
| Rename | requires v1.0+ with coordinated migration |

A use is **invalid** if: a label diverges from §2/§3, a synonym is introduced for an existing label, or a §4 disambiguation rule is violated.

---

## Versioning

| Version | Status | Change |
|---|---|---|
| **v0.1** | **current** | First thin-RFC pass. Cross-cutting labels + disambiguation rules. Closes RFC-1 v0.2 Appendix D.3 ($C$/$\mathcal{C}$ collision) via §4. Partially closes RFC-2 v0.1 §3 inv. 2 debt-marker (per-regime invariant labels) via §2. |

**Compatibility.** Within v0.x: additive only (new labels OK; renames not). Renames require v1.0+ with coordinated migration.

## Page-budget self-check

Target: ≤1 page (CLAUDE.md table; ½ page where the object admits — RFC-V is borderline because the registry content is irreducible).

Body §0–§6 ≈ 45 lines. Versioning + self-check ≈ 10 lines. **Total ≈ 1.1 pages — marginally over the ½-page-where-admitted target, within the ≤1 page tolerance.**

**Debt-marker.** RFC-V over the ½-page form because §2 enumerates five label-domains rather than collapsing to per-RFC pointers — but the centralization is what closes RFC-1 D.3 and partially closes RFC-2 v0.1's inv. 2 debt-marker. Revert when: cross-RFC traffic on these labels drops to per-domain reads only (each label-domain is referenced from a single RFC), at which point §2 collapses to per-RFC pointers like §3.
