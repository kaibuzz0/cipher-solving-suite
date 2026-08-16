# Repository Maintenance Policy

## Purpose

Keep this repository usable by multiple agents over long periods without losing provenance, duplicating work, or confusing demonstrations with live capabilities.

## Repository lanes

Use these logical lanes when adding or moving work:

- `solvers/` — reusable solving engines and algorithms.
- `tools/` — operator utilities, scanners, trackers, generators, and helpers.
- `research/` — target-independent research, documented opportunities, and analysis notes.
- `workspace/active/` — active case folders and temporary working material.
- `workspace/archive/` — completed/closed work retained for reproducibility.
- `intelligence/feeds/` — time-stamped machine-readable discovery feeds.
- `tests/` — deterministic regression tests and fixtures.
- `docs/` — architecture, runbooks, agent handoffs, and operational policy.
- `artifacts/` — generated results that must be retained but are not source code.

Avoid adding generated images, binary extracts, scan outputs, or one-off challenge files directly to the repository root.

## Definition of done

A change is complete only when all applicable items are true:

1. The objective is documented.
2. Scope/authorization is recorded for security-related target work.
3. Source code and generated artifacts are separated.
4. Tests or reproducible verification steps exist.
5. Claims in docs match observed behavior.
6. No secrets are committed.
7. The agent handoff log is updated.
8. The next action is explicit.

## Capability labels

Use these labels consistently in documentation and output:

- **implemented** — code exists.
- **tested** — automated or reproducible verification passed.
- **live** — successfully exercised against the stated current external source.
- **experimental** — incomplete or research quality.
- **simulated** — uses fixtures, mock data, or hard-coded examples.
- **deprecated** — retained for compatibility/history but should not be extended.

Do not use `production-ready` as a substitute for these labels.

## Agent work queue

Prefer GitHub Issues for durable tasks. Each issue should contain:

- problem statement,
- evidence,
- acceptance criteria,
- authorization/scope notes when security testing is involved,
- priority,
- dependencies,
- verification plan.

Agents should claim one issue at a time and link their PR to it.

## Daily maintenance cycle

The scheduled workflow runs once per day and may also be run manually. It should remain cheap and deterministic.

Daily checks:

- required governance files exist,
- Python entry points compile,
- obvious version drift is reported,
- root-level generated artifacts are inventoried,
- suspicious secret-like filenames are reported,
- handoff log exists,
- reports are uploaded as workflow artifacts.

The check is intentionally non-destructive. Agents fix findings through normal branches and PRs.

## Suggested recurring agent roles

**Maintainer:** triage issues/PRs, version drift, docs, CI health, and repository layout.

**Research agent:** identify legitimate CTF, puzzle, hackathon, audit, and bounty opportunities; record dates, rules, source URLs, payout evidence, and authorization boundaries.

**Solver agent:** improve reusable algorithms against local fixtures/challenges and add regression tests.

**Verifier agent:** independently reproduce claimed solves and capability statements; reject unverifiable claims.

**Archivist agent:** organize completed work, preserve provenance, deduplicate generated artifacts, and keep handoffs/search indexes clean.

No agent should both create a high-impact claim and be its only verifier.
