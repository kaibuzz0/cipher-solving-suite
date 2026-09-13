# Current Repository State

Last reconciled: 2026-09-13 08:11 UTC
Default branch: `main`
Reconciled default-branch head: `584fa02155392f7b024bbc024f02bac1ed2ec0bf`
Repository version: `v3.1.0` (README)

> This is a reconciliation snapshot. A branch/PR containing this file may have a newer commit by definition; compare material repository facts rather than treating that self-reference difference as drift.

## Verified health

- Current `main` is `584fa02155392f7b024bbc024f02bac1ed2ec0bf`, the merge of PR #171 (`Replay Aug 29 afternoon source health`).
- PR #171 exact repaired head `caefbab72d6630081d70925d9ab59c3949967508` passed Core validation `34746920680`, Intelligence Source Report `34746920645`, and Daily Repository Maintenance `34746920669`; there were no review threads and GitHub reported the PR mergeable.
- Exact-main Core validation `34746964346` and Deploy operations dashboard / Pages `34746964352` succeeded on merge commit `584fa02155392f7b024bbc024f02bac1ed2ec0bf`.
- Source registry validates with 16 sources and source-check history with 78 checks.
- Core covers the test suite, Python compilation, source-registry/history/report validation, intelligence validation, artifact inventory, 310 migration/reproduction verification, site-data generation, maintenance diagnostics, repository-browser/tool/toolset discovery, and canonical tool visibility.
- No standalone open GitHub issue currently blocks the chronological replay lane.

## Canonical source / integration state

- Canonical source history now advances through Aug. 29 afternoon, `2026-08-29T19:40:52Z`.
- PR #148 remains the canonical Aug. 29 morning replay: five records at `2026-08-29T07:38:35Z` for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`.
- PR #171 adds exactly one later canonical record for `ethglobal-events` at `2026-08-29T19:40:52Z`, fingerprint `361c6c0ce2988ea281442a7b6b6ac8ca94574cda8074242b2d7966fed9037179`, predecessor `5b270d1af189b17c8508993b6c5ed10d6794acec5e254eee7dc77f2c2f84925c`, `change_state=changed`.
- Only `ethglobal-events.last_checked_at` advances to `2026-08-29T19:40:52Z`; the other Aug. 29 morning source timestamps remain `2026-08-29T07:38:35Z`.
- The raw `intelligence/feeds/2026-08-29-afternoon-source-health.json` snapshot is unchanged.
- The replay was produced by repository-native workflow run `34746769854`, which executed `scripts/source_check_history.py replay-snapshot`, validated history and registry, ran `tests/test_aug29_afternoon_source_readiness.py`, and asserted the exact one-record/one-registry scope.
- `data/integration_queue.json` marks the Aug. 29 morning/afternoon lane integrated while preserving its prior provenance and chronology notes.
- Aug. 30 morning is now the next canonical replay gate. Later merged or open Sep. research remains contributed/noncanonical and must not skip that chronology.

## Regression found and repaired during PR #171

- First exact-head Core run `34746859968` failed all matrix lanes only because `tests/test_aug29_source_readiness.py` incorrectly required every Aug. 29 morning registry timestamp to remain permanently equal to `2026-08-29T07:38:35Z`.
- The replay itself, source-registry validation, source-history validation, source report, intelligence validation, site-data generation, maintenance, 310 checks, and 85 of 86 tests were already passing in that failed run.
- The test was repaired without weakening protected morning evidence: exact Aug. 29 morning fingerprints and predecessor assertions remain unchanged, while registry freshness must now equal each source's latest canonical history timestamp. This permits legitimate later replay records while still rejecting stale registry state.
- After that repair, exact-head Core `34746920680`, Source Report `34746920645`, and Maintenance `34746920669` all succeeded before merge.

## Concurrent / stale contribution state

- PR #170 is Sep. 13 research-only work originally based on pre-PR171 main. It does not itself advance canonical source freshness and must reconcile current `main` before integration if its base becomes stale.
- PR #168 is merged research evidence; its xTech, ETHOnline, Code4rena, and PwnSec claims remain noncanonical source-replay evidence.
- PR #161 and PR #163 remain stale-base research contributions and require current-main reconciliation before merge.
- Older open research PRs remain contributed evidence lanes and must be reconciled only when chronology/source overlap order permits.

## Toolset / case / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Shared tool registration remains canonical in `data/tools.json`; `source-history` remains verified and the 310 solver/analyzer/reproduction tools remain explicitly `experimental`.
- Structured active cases remain `20260816-310-btc-challenge` and `20260906-pwnsec-ctf-2026`.
- The 310 case remains internal evidence only and does not establish an external puzzle solve, private key, payout, or provenance of `310_challenge.png`.
- PwnSec remains authorization-bounded; repository evidence does not establish participant registration/team/faction state.
- User-facing repository state continues through generated site data; normal additions must not require bespoke `site/index.html` edits.

## Security / maintenance state

- Preserve all primary evidence, hashes, provenance, and research artifacts. Do not delete or relocate evidence silently.
- Current artifact inventory remains preservation-sensitive; cleanup must remain hash/provenance preserving.
- GitHub Actions still use major-version action tags (`actions/checkout@v4`, `actions/setup-python@v5`, `actions/upload-artifact@v4`) rather than immutable commit SHAs. Hosted runners warn that Node-20-targeting actions are being forced onto Node 24; immutable pinning/major-version refresh remains supply-chain hardening debt.
- CI installs broad dependency ranges rather than a lockfile, so dependency drift remains possible.
- `main` remains unprotected with required status-check enforcement disabled; release discipline depends on workflow verification and review practice.
- Legacy root truthfulness debt remains in `QUICK_START_REAL_MONEY.sh` and `TOOLS_AUDIT.md`; preserve history and reconcile those claims separately.

## Coordination drift requiring follow-up

- `docs/AGENT_HANDOFF.md`, `docs/WORK_QUEUE.md`, and `data/integration_queue.json` are reconciled on this branch to the merged PR #171 state and Aug. 30 morning next gate.
- Open research PRs must be reconciled from current `main` and rerun through validation before merge.

## Current operating priorities

1. Independently inspect the Aug. 30 morning source-health snapshot(s) and recompute every protected fingerprint and predecessor against canonical Aug. 29 afternoon history.
2. If Aug. 30 morning is valid, stage only its bounded chronological replay through the repository-native replay command; do not skip to later Sep. research.
3. Require source-history/registry validation, deterministic replay/readiness coverage, Core matrix, Intelligence Source Report, Daily Maintenance, Agent Operations/site-data compatibility, semantic diff review, and no unresolved review threads before merge.
4. Require post-merge exact-main Core and Pages success before advancing the next chronology gate.
5. Reconcile later research PRs only after current-main conflict review and according to chronology/source overlap.
6. Continue supply-chain/action pinning and legacy root truthfulness cleanup only as separate bounded objectives that preserve evidence.

## Next handoff

Current `main` is `584fa02155392f7b024bbc024f02bac1ed2ec0bf`. PR #171 made Aug. 29 afternoon canonical with exactly one ETHGlobal history addition and one matching registry timestamp advance, preserving the raw snapshot. Native replay run `34746769854` succeeded. Initial exact-head Core `34746859968` exposed an over-strict morning-registry regression; `tests/test_aug29_source_readiness.py` was repaired so exact morning evidence remains protected while registry freshness follows latest canonical history. Repaired exact-head Core `34746920680`, Source Report `34746920645`, and Maintenance `34746920669` succeeded. Post-merge Core `34746964346` and Pages `34746964352` also succeeded. Aug. 30 morning is the next chronology gate; later Sep. research remains noncanonical until the chronological replay chain reaches it.
