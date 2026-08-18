# Shared Work Queue

This is the human-readable queue for AI agents. GitHub issues may mirror larger tasks; this file is the fast handoff surface inside the repository.

## Rules

- Claim one item at a time by adding your agent name and UTC timestamp.
- Do not claim work already assigned unless the previous agent explicitly releases it.
- Each completed item must link to evidence: commit/PR, tests, report, or reproducible command.
- Security targets require an official scope/rules URL before any testing.
- New opportunities must record when they were checked. Do not copy prize claims without a current official source.
- Start from `README.md` for navigation before creating new paths or duplicate tools.

## Priority queue

| Priority | State | Work | Owner | Evidence / Next step |
|---|---|---|---|---|
| P1 | todo | Inventory and relocate generated root artifacts without losing evidence | unclaimed | Preserve hashes, provenance, and research references before moving anything |
| P1 | todo | Add verified live opportunity/news adapters | unclaimed | Use official feeds/APIs/RSS where possible; cache timestamped results and label failures |
| P2 | in-progress | Add link health and catalog freshness checks | build-agent | PR #24 merged deterministic URL/source-migration diagnostics; `agent/build-actionable-freshness-20260818` adds deterministic submission-phase/deadline evaluation. Independent CI/integrity verification is still required before this broader item can close. |
| P2 | todo | Add optional news/RSS adapters with cached timestamped output | unclaimed | Keep network failures non-destructive |
| P2 | todo | Inventory legacy solver modules and document inputs/outputs/dependencies | unclaimed | Build tool registry before refactoring or deleting anything |

## Completed

| Completed | Work | Evidence |
|---|---|---|
| 2026-08-17 | Add case index/dashboard integration | `scripts/build_site_data.py` scans `research/active-puzzles/*/case.json`; Pages packages `site-data/cases.json`; `site/app.js` renders Active Cases |
| 2026-08-16 | Establish multi-agent operating structure and dashboard | PR #1; `AGENTS.md`, `site/`, `docs/` |
| 2026-08-16 | Add deterministic unit tests for core command-line tools | `tests/test_core.py`, Core validation workflow |
| 2026-08-16 | Reconcile README and executable version/capability claims | `README.md`, `suite.py` |
| 2026-08-16 | Replace simulated opportunity scanner behavior with truthful catalog snapshots | `tools/scanning/opportunity_scanner.py` |
| 2026-08-16 | Build case-template workflow for new puzzles/challenges | `docs/CASE_WORKFLOW.md`, `scripts/new_case.py`, tests |
| 2026-08-16 | Make README the front-door navigation/workflow map | README quick navigation + dashboard reciprocal links |
