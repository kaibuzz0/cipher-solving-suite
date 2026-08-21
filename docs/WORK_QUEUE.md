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
| P1 | in-progress | Add verified live opportunity/news adapters | build-agent | PR #37 merged the first bounded official-source opportunity adapter for the NIH challenge index. It emits PR #34 provenance evidence, supports deterministic fixtures, fails non-destructively, and refuses to invent deadline times from date-only source text. Remaining work is additional official-source adapters and richer eligibility/prize/submission evidence where sources support it. |
| P2 | in-progress | Add link health and catalog freshness checks | build-agent | PR #24 merged deterministic URL/source-migration diagnostics, PR #27 merged deterministic submission-phase/deadline evaluation, PR #31 merged the canonical tool-visibility regression contract, PR #34 merged evidence preservation/normalization with SHA-256 provenance, and PR #37 merged a bounded NIH source-acquisition layer. Broader freshness still needs additional source-specific adapters and evidence beyond simple status/deadline fields. |
| P2 | todo | Add optional news/RSS adapters with cached timestamped output | unclaimed | Keep network failures non-destructive |
| P2 | in-progress | Inventory legacy solver modules and document inputs/outputs/dependencies | build-agent | PR #39 integrated a deterministic case-local replacement for the broken root 310 brute-force path. The current `agent/310-character-locator-20260821` branch similarly contains the root `char_locator.py` assumptions by adding a portable case-local edge-density analyzer with dependency-free P2 fixtures, lazy Pillow support for PNG/JPEG, explicit-output behavior, direct-script tests, case linkage and canonical tool registration. Preserve the root legacy file until reference/provenance review is complete; continue module-by-module after independent verification. |

## Completed

| Completed | Work | Evidence |
|---|---|---|
| 2026-08-19 | Verify canonical user-visible tool discovery across registry, repository browser, Pages/workspace, and Command Site snapshot | PR #31; `tests/test_tool_visibility_contract.py`; final head `be1d8ed...` passed Core `32231110295` and Daily Maintenance `32231110259`; merged as `a872b71...` |
| 2026-08-17 | Add case index/dashboard integration | `scripts/build_site_data.py` scans `research/active-puzzles/*/case.json`; Pages packages `site-data/cases.json`; `site/app.js` renders Active Cases |
| 2026-08-16 | Establish multi-agent operating structure and dashboard | PR #1; `AGENTS.md`, `site/`, `docs/` |
| 2026-08-16 | Add deterministic unit tests for core command-line tools | `tests/test_core.py`, Core validation workflow |
| 2026-08-16 | Reconcile README and executable version/capability claims | `README.md`, `suite.py` |
| 2026-08-16 | Replace simulated opportunity scanner behavior with truthful catalog snapshots | `tools/scanning/opportunity_scanner.py` |
| 2026-08-16 | Build case-template workflow for new puzzles/challenges | `docs/CASE_WORKFLOW.md`, `scripts/new_case.py`, tests |
| 2026-08-16 | Make README the front-door navigation/workflow map | README quick navigation + dashboard reciprocal links |
