# Handoff: runs and working libraries

**Status:** Planning document for accumulating real-case experience and a working library of example artifacts via [mpa-bridge](https://github.com/ronviers/mpa-bridge).
**Audience:** A future Claude (or human) running mpa-bridge against real cases (substrates, specs, data) and capturing the results as durable artifacts.
**Companion:** [handoff_operations_manual.md](handoff_operations_manual.md) (must land first for runs to be reproducible), [handoff_protocol-tool.md](handoff_protocol-tool.md).

---

## Goal

Move mpa-bridge from "passes its smoke tests" to "has been used on real cases, has a library of worked examples, has accumulated friction notes." Two concrete deliverables:

1. **Examples library** at `mpa-bridge/examples/<case-name>/` — real-flavored specs, R_docs, signatures, gap reports, organized by case.
2. **Case studies** at `mpa-bridge/docs/cases/<case-name>.md` — narrative writeups: what was attempted, what worked, what surfaced.

The thin-RFC discipline holds because the framework hasn't been stressed by real implementers (1 author per artifact). The tool's discipline holds because it hasn't been stressed by real cases. Runs are how we find out which scaffolding is correctly thin vs. brittle. Working libraries are how future sessions get cheaper — they start with concrete examples instead of synthesizing from scratch.

## Where it lives

```
H:/mpa-bridge/
├── examples/
│   ├── surface-code/         # spec, compiled R_docs per intent, signatures, notes
│   ├── habit-extinction/     # when the driver lands (v0.2 trigger)
│   └── unknown-data/         # cases driving gap-report
└── docs/
    ├── cases/
    │   ├── surface-code-walkthrough.md
    │   └── ...
    └── friction.md           # running list of awkward surfaces, missing affordances
```

## Round 1 cases (concrete starting set)

Each is independently runnable; can be tackled in parallel by separate sessions.

1. **Surface-code QEC end-to-end.** Build a real spec from v9 §FDR (the surface-code identification paragraph) and the surface-code reference driver. Compile under each of I1..I5. Validate the resulting constellation. Run round-trip against synthetic identity measurements. Write up: did each intent compile cleanly? Were the I2/I3/I4 `RFC-S5.METRIC_NA` infos surfaced as expected? Where did Sonnet need prompt help?

2. **Cross-substrate gap report.** Take 3–5 substrate descriptions from the existing `mpc-*` repos (mpc-glass aging, mpc-brain habit-extinction, mpc-quantum syndrome streams, mpc-sat XOR). Run `gap-report` on each. Compare what the gap reporter named as missing vs. what's actually pinned in the corresponding `mpc-*` repo's driver-in-progress. Write up: where did the LLM see what we already know? Where did it miss?

3. **Discover ranking calibration.** Run `discover` on the same 3–5 substrate descriptions plus a synthetic mismatch. Verify the ranking matches intuition (each `mpc-*` substrate's data scores high on its own driver, low on others; the synthetic mismatch scores low across the board). Write up: ranking calibration.

4. **Vocabulary check pass.** Run `vocab` on every RFC, the architectural block-in, `v9_compressed.md`, and the handoff documents. Catalog the false-positive rate vs. real catches. Tighten the regex rules in `vocabulary.py` based on actual experience rather than anticipated need.

## Per-case directory structure

```
examples/<case-name>/
├── README.md           # one paragraph: what is this case
├── spec.json           # the spec object (when applicable)
├── driver.json         # the driver profile (or pointer to mpa-atlas/reference-drivers/)
├── intent_<I1..I5>/
│   ├── compiled.json   # output of compile under this intent
│   ├── round_trip.txt  # output of round-trip vs identity measured
│   └── notes.md        # what was learned for this intent
└── gap_report.md       # if run, the gap-report output verbatim
```

Each case study lives at `docs/cases/<case-name>.md` and points back to its `examples/<case-name>/` directory.

## Friction log + fixture promotion

- `mpa-bridge/docs/friction.md` — running list of awkward surfaces, prompt failures, missing affordances. Each entry: trigger condition, what happened, suggested fix (or "deferred — needed v0.2").
- When a real-case artifact stabilizes (compiles cleanly, validates, round-trips), promote a sanitized copy to `tests/fixtures/` so the test suite gets richer beyond minimal-valid.

## Failure modes to watch

- **Producing artifacts the tool can't ingest.** Every example file is regression-testable: `python -m mpa_bridge validate <file>` returns rc=0. If a hand-written example fails the validator, the example is wrong, OR it's revealing a real validator gap → file in `friction.md`.
- **Case studies that just narrate the tool output.** A case study adds insight: where the LLM missed, where the prompt had to be guided, what the validator caught that the LLM produced wrong, where the discipline held vs. wobbled. Pure "I ran X and got Y" is not a case study.
- **Letting the cache bloat without grading.** Each case produces a brief grade in its case study — was the LLM output good? What would be improved? The user explicitly committed to grade-after-the-fact at the assist surface's design (memory: `feedback_thin_modern_engineering.md`). Case studies are where grading lives.
- **Promoting artifacts to fixtures without sanitizing.** If a real spec is from a substrate-specific working repo, double-check no proprietary or ungeneralized content leaks into `tests/fixtures/`.

## Out of scope

- **Building substrate-implementation drivers.** That's `mpc-*` repo work. Runs use what's already there; they don't create new drivers.
- **API benchmarking / latency tuning.** v0.1 explicitly resists 2026-not-2022 over-engineering (memory: `feedback_thin_modern_engineering.md`).
- **Public publication of examples.** Internal first; if any case becomes worth sharing externally, separate decision.

## Effort estimate

- Round 1 cases (the four above): ~1–2 days to run + write up.
- Each subsequent case as new substrates land: ~half-day.
- `friction.md` + fixture promotion: ongoing, integrated into each case.

## Why this matters

The DBS-backward arm of mpa-bridge (components 5, 6) and the DBS-forward synthesis arm (component 3) are *only as good as their LLM calls*. Determining how good those calls actually are requires running them on cases where the answer is partly known (from existing `mpc-*` work) and grading. Without runs, the tool's claim to operationalize demand-bounded sufficiency is unstressed.

The library that accumulates is also the on-ramp for any future contributor: real specs to read, real R_docs to compare against, real gap reports to learn from. The framework's *peel, not scrape* discipline (architectural block-in §5, *origin*) needs concrete cases to peel against.

## Related

- [`handoff_operations_manual.md`](handoff_operations_manual.md) — must land first.
- [`handoff_habit-extinction_reference-driver.md`](handoff_habit-extinction_reference-driver.md) — when habit-extinction lands, cross-substrate cases (item 2) get richer; v0.2 trigger.
- [`handoff_protocol-tool.md`](handoff_protocol-tool.md) §"Completion criteria" — v0.1 / v0.2 readiness gates that runs validate or surface gaps in.

## Inherited soft blockers

The unblock handoff (deleted on completion of the acute blocker, 2026-05-08) flagged three soft blockers that runs absorb rather than close:

- **No CI on either repo.** Add `pytest -q` to mpa-bridge and schema-validation to mpa-atlas once runs produce artifacts that benefit from CI protection.
- **Compile prompt's I1..I5 mapping is unverified.** Round-trip against hand-built reference per intent surfaces this; closing happens via runs, not by adding more prose.
- **Compile may cite RFC sections that don't exist.** Tighten `compile_.py` SYSTEM_PROMPT with "do not invent section numbers; quote verbatim or omit"; or post-validate by extracting cited RFC references and grep-checking. Defer the post-validator until runs surface a real harm case.
