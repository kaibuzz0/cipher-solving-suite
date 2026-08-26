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
| P2 | in-progress | Add link health and catalog freshness checks | build-agent | PR #50 replayed PR #44's source-health observations. PR #60 canonically replayed the former PR #47 snapshot at `2026-08-22T19:42:58Z`. PR #63 preserved the former PR #49 raw `2026-08-23T07:42:04Z` snapshot byte-for-byte, and PR #67 canonically replayed its four exact observations after independent hash/predecessor verification; final head `ab0dc86d...` passed Core `32946337938`, Source Report `32946337917`, and Daily Maintenance `32946337928`, then merged as `f7bbeabd...`. Post-merge Core `33004864258` and Pages `33004864246` also succeeded. Next: reconcile PR #52; PR #56, #62, and #66 follow in chronology/source-overlap order. |
| P2 | todo | Add optional news/RSS adapters with cached timestamped output | unclaimed | Keep network failures non-destructive |
| P2 | in-progress | Inventory legacy solver modules and document inputs/outputs/dependencies | build-agent | PR #39 integrated the portable 310 password-candidate solver, PR #42 integrated the portable character-region locator, PR #45 added a non-destructive reproduction verifier, and PR #53 merged the portable `btc310-image-analyzer` with deterministic direct-script tests, explicit-output-only derived outputs, canonical registration and an `experimental` claim boundary. Preserve root legacy files until reference/provenance review is complete. Next 310 work should prioritize external provenance for `310_challenge.png` or another hash-preserving legacy/root-artifact item rather than duplicating the analyzer. |

## Completed

| Completed | Work | Evidence |
|---|---|---|
| 2026-08-26 | Canonically replay former PR #49 / merged PR #63 Aug. 23 source observations | PR #67; raw blob SHA `2c5eeaa8...` preserved; all four fingerprints and predecessor links independently verified; final head `ab0dc86d...` passed Core `32946337938`, Source Report `32946337917`, and Daily Maintenance `32946337928`; merged as `f7bbeabd...`; post-merge Core `33004864258` and Pages `33004864246` succeeded |
| 2026-08-26 | Reconcile post-PR63 coordination state before canonical replay | PR #65; exact head `de560d89...` passed Core `32943027517` and Daily Maintenance `32943027263`; merged as `ace1b5ea...` |
| 2026-08-26 | Reconcile former PR #49 raw source snapshot onto current main without advancing source freshness | PR #63; raw blob SHA `2c5eeaa8...` matches original PR #49 byte-for-byte; final head `e5c74f0c...` passed Core `32893463550` on Python 3.11/3.12/3.13 and Daily Maintenance `32893463621`; merged as `0ef952cb...`; post-merge Core `32942362583` and Pages `32942362528` succeeded |
| 2026-08-25 | Replay merged PR #58 / former PR #47 source-health observations canonically | PR #60; final head `5433788c...` passed Core `32825016825` on Python 3.11/3.12/3.13, Source Report `32825016797`, and Daily Maintenance `32825016794`; merged as `7d354e22...`; post-merge Core `32888885708` and Pages `32888885847` succeeded |
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
