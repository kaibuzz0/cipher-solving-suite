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
| P2 | in-progress | Add link health and catalog freshness checks | build-agent | PR #50 replayed PR #44's source-health observations. The current build branch `build/replay-pr58-source-health-20260825` now replays the merged PR #58 snapshot's exact `2026-08-22T19:42:58Z` observations into canonical source history and registry freshness. Next: require fresh Core/source/site-data validation and merge if green, then reconcile PR #49 at `2026-08-23T07:42:04Z`; PR #52 and PR #56 remain later blocked research lanes. |
| P2 | todo | Add optional news/RSS adapters with cached timestamped output | unclaimed | Keep network failures non-destructive |
| P2 | in-progress | Inventory legacy solver modules and document inputs/outputs/dependencies | build-agent | PR #39 integrated the portable 310 password-candidate solver, PR #42 integrated the portable character-region locator, PR #45 added a non-destructive reproduction verifier, and PR #53 merged the portable `btc310-image-analyzer` with deterministic direct-script tests, explicit-only derived outputs, canonical registration and an `experimental` claim boundary. Preserve root legacy files until reference/provenance review is complete. Next 310 work should prioritize external provenance for `310_challenge.png` or another hash-preserving legacy/root-artifact item rather than duplicating the analyzer. |

## Completed

| Completed | Work | Evidence |
|---|---|---|
| 2026-08-25 | Reconcile post-PR58 integrity coordination state | PR #59; merged as `3b0d7f6a...`; preserved exact PR #58 replay next action and PR #56/#57 collision resolution |
| 2026-08-25 | Reconcile stale PR #47 evidence onto current main and repair Agent Operations parsing | PR #58; raw snapshot blob SHA `1b391117...` matched original PR #47; final head `3e45ebbc...` passed Core `32821238771` and Daily Maintenance `32821238864`; merged as `e08d64b8...` |
| 2026-08-24 | Reconcile post-PR53 coordination state | PR #55; exact head `4a813414...` passed Core `32767868389` and Daily Maintenance `32767868466`; merged as `551c7e97...` |
| 2026-08-24 | Reconcile and integrate the portable 310 image analyzer onto current main | PR #53; final head `3f8ac546...` passed Core `32663349865` on Python 3.11/3.12/3.13 and Daily Maintenance `32663349853`; merged as `73fa9fa...`; canonical `btc310-image-analyzer` remains `experimental` |
| 2026-08-19 | Verify canonical user-visible tool discovery across registry, repository browser, Pages/workspace, and Command Site snapshot | PR #31; `tests/test_tool_visibility_contract.py`; final head `be1d8ed...` passed Core `32231110295` and Daily Maintenance `32231110259`; merged as `a872b71...` |
| 2026-08-17 | Add case index/dashboard integration | `scripts/build_site_data.py` scans `research/active-puzzles/*/case.json`; Pages packages `site-data/cases.json`; `site/app.js` renders Active Cases |
| 2026-08-16 | Establish multi-agent operating structure and dashboard | PR #1; `AGENTS.md`, `site/`, `docs/` |
| 2026-08-16 | Add deterministic unit tests for core command-line tools | `tests/test_core.py`, Core validation workflow |
| 2026-08-16 | Reconcile README and executable version/capability claims | `README.md`, `suite.py` |
| 2026-08-16 | Replace simulated opportunity scanner behavior with truthful catalog snapshots | `tools/scanning/opportunity_scanner.py` |
| 2026-08-16 | Build case-template workflow for new puzzles/challenges | `docs/CASE_WORKFLOW.md`, `scripts/new_case.py`, tests |
| 2026-08-16 | Make README the front-door navigation/workflow map | README quick navigation + dashboard reciprocal links |
