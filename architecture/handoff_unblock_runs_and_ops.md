# Handoff: unblock runs + operations work

**Status:** Planning document for clearing the blockers preventing the operations-manual + runs/libraries handoffs from completing.
**Audience:** A future Claude (or human) clearing the path before substantive operations work begins.
**Companion:** [handoff_operations_manual.md](handoff_operations_manual.md), [handoff_runs_and_libraries.md](handoff_runs_and_libraries.md).

---

## Goal

Identify and clear concrete blockers that prevent the operations manual or the runs/libraries work from being completed cleanly. One blocker is acute; the rest are soft and individually deferrable.

---

## Acute blocker — mpa-atlas uncommitted state

mpa-bridge hardcodes paths to mpa-atlas content (`H:/mpa-atlas/rfcs/`, `H:/mpa-atlas/reference-drivers/`, `H:/mpa-atlas/framework/v9_compressed.md`) that the tool reads at runtime. As of 2026-05-08 the state in mpa-atlas is:

**Modified, tracked:**
- `README.md`
- `architecture/MPA_Architectural_Block-In.md`
- `framework/v9_compressed.md`
- `rfcs/MPA-RFC-1_Spec-Object.md`

**Untracked:**
- `architecture/handoff_habit-extinction_reference-driver.md`
- `architecture/handoff_protocol-tool.md` (the spec mpa-bridge implements)
- `architecture/handoff_schema_files.md`
- `architecture/handoff_v9_architectural-backport.md`
- `reference-drivers/` (the driver registry mpa-bridge reads at runtime)
- `rfcs/MPA-RFC-2_FDR-Signatures.md`
- `rfcs/MPA-RFC-3_Consistency-Completeness.md`
- `rfcs/MPA-RFC-RI_Realizer-Interface.md`
- `rfcs/MPA-RFC-S_Scale-Management.md`
- `rfcs/MPA-RFC-V_Reference-Vocabulary.md`

The schemas at `mpa-atlas/schema/*.json` were committed (commit `2f3e27f`); everything else above is local-only. Anyone cloning mpa-atlas from GitHub right now gets the schemas and RFC-1 v0.1 (pre-thin), but **not** the v0.2 RFCs the schemas depend on, **not** the reference driver mpa-bridge expects, and **not** the protocol-tool handoff that is the operative spec.

This blocks both parallel handoffs:
- The **operations manual** can't credibly document the tool until the artifacts the tool reads are version-controlled.
- **Runs and libraries** is fundamentally non-reproducible until the same.

### What needs to happen

1. **Verify consistency** (read-pass, no edits unless something obvious is broken). Cross-references resolve, principles consistent across the modified files and the new untracked RFCs, no half-finished sections from prior aborted sessions.

2. **Decide commit grouping.** Three reasonable shapes:
   - **One big commit** — "v0.2 protocol body + reference driver + handoffs." Fast; collapses provenance.
   - **Per-artifact** — one commit per RFC, one for v9 promotion, one for block-in updates, one for reference driver, one per handoff. ~10 commits. Preserves provenance; tedious.
   - **Bundled by topic** — (a) thin-pass RFC sequence (RFC-2, 3, S, RI, V together), (b) v9 + block-in + RFC-1 updates, (c) reference driver + handoffs. ~3 commits.

   **Recommendation:** option (c). Bundles tell the right story (thin-pass landed → framework rigor consolidated → operational scaffolding shipped) without per-artifact archaeology cost.

3. **Run the gitleaks pre-commit hook on each commit.** Hook is installed at `H:/mpa-atlas/.git/hooks/pre-commit` (this session). Should pass — no secrets in any of these files — but verify.

4. **Push.** mpa-atlas remote is `github.com/ronviers/mpa-atlas`. Public.

5. **Update RFC Appendix A "(forthcoming)" annotations.** Each of RFC-1, RFC-2, RFC-S, RFC-RI's Appendix A says "(forthcoming)" next to the schema path. The schemas exist now (commit `2f3e27f`). Drop the "(forthcoming)" tag in a small follow-up commit. Trivial; ~2 minutes.

### Effort estimate

~30 minutes total. The bundling decision is the only judgment-heavy step; everything else is mechanical.

---

## Soft blockers — not acute, worth surfacing

### A. ANTHROPIC_API_KEY in registry only

The key is in `HKCU\Environment` (Windows registry) but **not** in the cross-OS keystore at `~/.config/mpc/keys.env` per global CLAUDE.md. `mpa-bridge` handles a registry fallback (`assist._ensure_api_key`), so the tool works on Windows. But: WSL Python can't read the Windows registry, and a machine rebuild loses the registry-only state silently.

**Fix:** create the keystore file per the [GWS1_Profiler README](H:\GWS1_Profiler\README.md) format. ~10 minutes. Not blocking — but every day this stays uncreated, the rebuild risk persists.

### B. No CI for either repo

Tests pass locally. Push triggers nothing. Schema validation happens only when a human runs the round-trip script.

**Fix:** add `.github/workflows/test.yml` to mpa-bridge that runs `pytest -q` on push/PR; add a schema-validation workflow to mpa-atlas. ~15 minutes each. Not blocking — local discipline is fine for now — but worth filing once the runs/libraries work begins producing artifacts that need protection.

### C. Compile prompt's I1..I5 mapping is unverified

`compile` produces R_docs that pass the structural validator. Whether `canonical_snapshot`'s intent projection actually reflects RFC-S §3 mapping rules (e.g., "scale uniformly under I1") is currently **uncheckable beyond shape**. The validator-as-gatekeeper pattern catches structural errors, not semantic-mapping errors.

**Fix:** the runs/libraries work itself surfaces this — compile under each intent against a known-correct hand-built reference, compare the diffs. The unblock here is *recognizing the gap*, not closing it. Closing happens via runs.

### D. Compile cites RFCs that may not exist

Observed in the smoke gap-report run (cache `6c9ea8d9...json`): Haiku cited "RFC-S §3 restricted-access protocol (Appendix B.2)" which does not exist in RFC-S. Same risk surface in `compile`'s output.

**Fix:** tighten the SYSTEM_PROMPT in `gap_report.py` and `compile_.py` with a "do not invent section numbers; quote verbatim or omit" rule. Or post-validate by extracting cited RFC references and grep-checking. ~15 minutes for the prompt fix; defer the post-validator until runs surface a real harm case.

---

## What this handoff does NOT do

- **Authoring the operations manual or running cases.** Other two handoffs.
- **Generating the habit-extinction reference driver.** Tracked separately at [handoff_habit-extinction_reference-driver.md](handoff_habit-extinction_reference-driver.md).
- **Modifying the seven mpa-bridge components.** v0.1 ships; further changes wait for runs to surface concrete needs.
- **Expanding mpa-bridge surface area** (new commands, new components). Out of scope until runs justify.

## Why this matters

`handoff_operations_manual.md` and `handoff_runs_and_libraries.md` cannot land cleanly while their input artifacts are uncommitted local state. This handoff is the precondition; ~30 minutes of work that unblocks ~2 days of substantive work.

The soft blockers are a separate question — none of them block the parallel handoffs, but each represents a small fragility that compounds. Address them when convenient; they're listed here so a future session has the inventory in one place.

## Related

- [`handoff_operations_manual.md`](handoff_operations_manual.md) — first parallel handoff.
- [`handoff_runs_and_libraries.md`](handoff_runs_and_libraries.md) — second parallel handoff.
- [`handoff_protocol-tool.md`](handoff_protocol-tool.md) — defines mpa-bridge; one of the artifacts to be committed under the acute blocker.
- Global CLAUDE.md (`C:\Users\ronviers\.claude\CLAUDE.md`) — documents the registry / keystore / CI conventions referenced in soft blockers A and B.
