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
| P1 | todo | Add case index/dashboard integration | unclaimed | Read `research/active-puzzles/*/case.json` and surface active cases without duplicating metadata |
| P2 | in-progress | Add link health and catalog freshness checks | build-agent | PR #24 adds deterministic URL inventory, source-migration replay, and bounded live link diagnostics; independent integrity review and broader catalog freshness/age policy remain |
| P2 | todo | Add optional news/RSS adapters with cached timestamped output | unclaimed | Keep network failures non-destructive |
| P2 | todo | Inventory legacy solver modules and document inputs/outputs/dependencies | unclaimed | Build tool registry before refactoring or deleting anything |

## Completed

| Completed | Work | Evidence |
|---|---|---|
| 2026-08-16 | Establish multi-agent operating structure and dashboard | PR #1; `AGENTS.md`, `site/`, `docs/` |
| 2026-08-16 | Add deterministic unit tests for core command-line tools | `tests/test_core.py`, Core validation workflow |
| 2026-08-16 | Reconcile README and executable version/capability claims | `README.md`, `suite.py` |
| 2026-08-16 | Replace simulated opportunity scanner behavior with truthful catalog snapshots | `tools/scanning/opportunity_scanner.py` |
| 2026-08-16 | Build case-template workflow for new puzzles/challenges | `docs/CASE_WORKFLOW.md`, `scripts/new_case.py`, tests |
| 2026-08-16 | Make README the front-door navigation/workflow map | README quick navigation + dashboard reciprocal links |
