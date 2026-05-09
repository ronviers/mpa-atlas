# MPA-RFC-3: Consistency & Completeness

**Status:** Draft v0.1 — first thin-RFC pass.
**Targets:** All other RFCs. Specifies cross-artifact predicates beyond what each per-RFC §3 carries.
**Companion:** [RFC-1](MPA-RFC-1_Spec-Object.md), [RFC-2](MPA-RFC-2_FDR-Signatures.md), [RFC-S](MPA-RFC-S_Scale-Management.md), [RFC-V](MPA-RFC-V_Reference-Vocabulary.md), [RFC-RI](MPA-RFC-RI_Realizer-Interface.md), [Architectural Block-In](../architecture/MPA_Architectural_Block-In.md).

---

## 0. Foundational principles

Inherits the five from the [Architectural Block-In](../architecture/MPA_Architectural_Block-In.md). RFC-3 instances *singular working-space path* (4) at the cross-artifact layer: one consistency / completeness rule per predicate; no synonymous rules across RFCs.

## 1. Object

A **constellation** is the set of artifacts {spec object, driver profile, signatures, $R_\text{doc}$} jointly required to compile, realize, and validate a spec. RFC-3 specifies the predicates that span artifact boundaries — predicates no single RFC owns.

## 2. Shape

A consistency rule is `(name, predicate, scope)`:
- `name`: stable label (C# for consistency, K# for completeness).
- `predicate`: boolean function over named artifacts.
- `scope`: which artifacts the predicate spans.

Predicates use canonical labels from [RFC-V](MPA-RFC-V_Reference-Vocabulary.md). Per-artifact internal invariants (each RFC's own §3) are not duplicated here.

## 3. Consistency rules

| # | Rule | Scope |
|---|---|---|
| C1 | spec's $(\tau_{obs}, D)$ ⊆ driver's `gamut` ranges | RFC-1 §2 + RFC-S §4 |
| C2 | spec's $V/E/\Gamma$ types ∈ driver's `gamut.trail_class_support` | RFC-1 §2 + RFC-S §4 |
| C3 | $R_\text{doc}$'s `intent` ∈ driver's supported intents | RFC-RI §2 + RFC-S §4 |
| C4 | $R_\text{doc}$'s `realizer_class_target` = driver's `substrate_class` | RFC-RI §2 + RFC-S §4 |
| C5 | spec's persistence depth $N$ ≤ driver's `gamut.persistence_depth` $N(S)$ | RFC-1 §2 + RFC-S §4 |

## 4. Completeness rules

| # | Rule | Scope |
|---|---|---|
| K1 | every spec-object element ($V$, $E$, declared $\Gamma$) has a `signature_targets` entry in $R_\text{doc}$ | RFC-1 §2 + RFC-2 §2 + RFC-RI §2 |

## 5. Invariants

A constellation is **valid** iff:

1. **Independent validity.** Each artifact is independently valid per its own RFC's §3.
2. **Cross-artifact consistency.** All C# (§3) and K# (§4) predicates hold.

## 6. Operations

| Operation | Signature |
|---|---|
| Validate constellation | $(\text{spec}, \text{driver}, R_\text{doc}, \text{signatures}) \to \text{diagnostics}[]$ — runs C# and K# predicates |
| Mechanical-only | every predicate is computable from artifact contents alone; no human judgment |

## 7. Falsifiers

- Any C# or K# predicate fails.
- Any artifact independently invalid per its own RFC §3.

## 8. Pointer

| What | Where |
|---|---|
| Per-artifact internal invariants | each RFC's §3 |
| Canonical labels in predicates | [RFC-V §2](MPA-RFC-V_Reference-Vocabulary.md) |
| Mechanical-validation discipline | Architectural Block-In §"Where the rigor actually lives" |

---

## Versioning

| Version | Status | Change |
|---|---|---|
| **v0.1** | **current** | First thin-RFC pass. C1–C5 + K1 cover the cross-artifact predicates currently in scope across RFC-1 / RFC-2 / RFC-S / RFC-RI. Closes RFC-RI v0.1 §3 inv. 3 + inv. 5 collapse condition. |

**Compatibility.** Within v0.x: additive only (new C# / K# rules ok; renames not). Renames require v1.0+ with coordinated migration.

## Page-budget self-check

Target: ≤1 page (CLAUDE.md table).

Body §0–§8 ≈ 42 lines. Versioning + self-check ≈ 8 lines. **Total ≈ 1.0 page. Pass.**

No debt-marker. The discipline holds: cross-artifact predicates that no single RFC owns live here at half-page weight.
