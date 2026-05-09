# Handoff: operations manual for mpa-bridge

**Status:** Planning document for the operations manual — user-facing how-to-use guide for [mpa-bridge](https://github.com/ronviers/mpa-bridge).
**Audience:** A future Claude (or human) who needs to run mpa-bridge against real specs / drivers / data and document the experience for future runs.
**Companion:** [handoff_protocol-tool.md](handoff_protocol-tool.md) (the spec for mpa-bridge), [handoff_runs_and_libraries.md](handoff_runs_and_libraries.md) (the parallel handoff that stress-tests the manual).

---

## Goal

Produce `mpa-bridge/docs/operations.md` — the user-facing operations manual. README says what mpa-bridge **is**; `docs/status.md` says what's **working**; `operations.md` says **how to use it**.

Read by: someone with a real spec / driver / unknown data, who needs to know which subcommand to run and how to interpret the output.

## Where it lives

`H:/mpa-bridge/docs/operations.md`. Linked from README under a "How to use" section that supersedes the current minimal usage block.

## What the manual contains

Six sections, in this order:

1. **Quickstart.** Install (`pip install -e .`), config (`ANTHROPIC_API_KEY` presence, schemas at `H:/mpa-atlas/schema/`, cache at `D:/Cache/mpa-bridge/`), one canonical first-run command and what to expect on stdout / stderr.

2. **Subcommand reference.** For each of `validate`, `constellation`, `compile`, `round-trip`, `discover`, `gap-report`, `vocab`: signature, required inputs, where outputs go, exit-code convention (0 = clean, 1 = errors found, 2 = bad usage), one minimal worked example.

3. **Workflows.** Three composed scenarios to start:
   - **"I have a new substrate."** `discover` → either `compile` (driver fits) or `gap-report` (driver missing).
   - **"I have a spec and want to certify a substrate."** `validate spec` → `compile` → `constellation` → `round-trip`.
   - **"I'm authoring an RFC or driver."** `vocab` against the canonical-label registry; iterate.

4. **Diagnostic codes.** Table mapping every code (`SCHEMA.<kind>`, `RFC1.INV.<n>`, `RFC3.C<n>`, `RFC3.K<n>`, `RFC-S5.*`, `RFCV.S<n>.<tag>`, `BRIDGE.<TAG>`) to meaning, severity, and (where relevant) the RFC section it references. Tests assert on these codes; CI consumes them; users grep them.

5. **Cache management + grading.** What lives in `D:/Cache/mpa-bridge/`, how to inspect a record (`jq`, `python -m json.tool`), how to clear stale entries, how to use cache files as run logs for after-the-fact grading. The cache *is* the run log — not a separate telemetry surface.

6. **Determinism + when to trust what.** Which surfaces are mechanical (1, 2, 4, 7 — same input, same output) vs. Claude-assisted (3, 5, 6 — local-cached but stochastic on cache miss). CI should consume only mechanical-surface verdicts. Synthesis surfaces are advisory and gradable.

## Out of scope

- **Library-API reference** (programmatic use of `mpa_bridge` as a Python module). Separate doc when it becomes wanted.
- **Architecture / internals.** Lives in `mpa-bridge/CLAUDE.md` and per-module docstrings.
- **Contribution guide.** Defer until external contributors exist.

## Failure modes to watch

- **Re-narrating the README.** README says what; operations manual says how. If a section reads like a feature list, rewrite it as a workflow.
- **Code listings without expected output.** Every worked example shows the command AND the expected stdout/stderr on the canonical fixture. Without expected output, "I ran the command" doesn't tell the reader if their run is healthy.
- **Diagnostic-code table that drifts.** The table must match what `src/mpa_bridge/` actually emits. Cheapest enforcement: a smoke script that runs the full suite, collects emitted codes, and diffs against the table. Worth doing as a follow-up; not blocking v0.1 of the manual.

## Effort estimate

Half a day for a tight first pass. The diagnostic-codes section is the largest single piece — every code that ships should be listed with one-line meaning. Workflows section needs a real worked example per scenario, ideally drawn from the runs/libraries handoff once that work begins.

## Why this matters

Without an operations manual, every new run requires the user (or a future Claude) to read source or trial-and-error their way through. The tool ships seven components with subtle composition rules (validators-stay-mechanical / synthesis-uses-Claude / cache-as-log / schemas-are-source-of-structural-truth). Surfacing those in one document is the difference between "tool exists" and "tool is reusable across sessions and people."

## Related

- [`handoff_runs_and_libraries.md`](handoff_runs_and_libraries.md) — the parallel handoff. Operations manual makes runs reproducible; runs stress-test the manual.
- [`handoff_protocol-tool.md`](handoff_protocol-tool.md) — the spec mpa-bridge implements; the operations manual is the spec's reader-side companion.
