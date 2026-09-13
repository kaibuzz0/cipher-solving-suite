# Current Repository State

Last reconciled: 2026-09-13 19:18 UTC
Default branch: `main`
Reconciled default-branch head: `e61b39d26aaaf46459ac1d45a7621a5d3a1854d9`
Repository version: `v3.1.0` (README)

> This is a reconciliation snapshot. A branch/PR containing this file may have a newer commit by definition; compare material repository facts rather than treating that self-reference difference as drift.

## Verified health

- Current `main` is `e61b39d26aaaf46459ac1d45a7621a5d3a1854d9`, the merge of PR #172 (`Ops: reconcile queues after PR #171`).
- Exact-main Core validation `34747174084` and Deploy operations dashboard / Pages `34747174083` succeeded on `e61b39d26aaaf46459ac1d45a7621a5d3a1854d9`.
- Later Daily Repository Maintenance `34760836965` and Intelligence Source Report `34763291440` also succeeded on the same exact main commit.
- Source registry validates with 16 sources and canonical source-check history contains 78 checks through Aug. 29 afternoon.
- Core covers the test suite, Python compilation, source-registry/history/report validation, intelligence validation, artifact inventory, 310 migration/reproduction verification, site-data generation, maintenance diagnostics, repository-browser/tool/toolset discovery, and canonical tool visibility.
- No standalone open GitHub issue currently blocks the chronological replay lane.
- `main` remains unprotected and required status-check enforcement is disabled.

## Canonical source / integration state

- Canonical source history advances through Aug. 29 afternoon, `2026-08-29T19:40:52Z`.
- PR #148 remains the canonical Aug. 29 morning replay: five records at `2026-08-29T07:38:35Z` for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`.
- PR #171 adds exactly one later canonical record for `ethglobal-events` at `2026-08-29T19:40:52Z`, fingerprint `361c6c0ce2988ea281442a7b6b6ac8ca94574cda8074242b2d7966fed9037179`, predecessor `5b270d1af189b17c8508993b6c5ed10d6794acec5e254eee7dc77f2c2f84925c`, `change_state=changed`.
- PR #172 reconciled `docs/WORK_QUEUE.md`, `data/integration_queue.json`, `ops/CURRENT_STATE.md`, and append-only handoff state so Aug. 30 morning is the next chronological replay gate.
- The raw Aug. 29 snapshots remain preserved unchanged.

## Aug. 30 morning independent readiness check

- `intelligence/feeds/2026-08-30-source-health.json` is the next eligible snapshot at `2026-08-30T07:38:20Z`.
- Repo Integrity independently recomputed all five preserved observation SHA-256 fingerprints and they exactly match the contributed values:
  - `challenge-gov`: `0570aab0fa0e07a2a97db33360d99e65c1a97260df3b71eb88dd753bd3885a75`
  - `ctftime-upcoming`: `1867c7ba3ec559aac232f71474198bd8eef43eb9b5ce0a71689930794044510e`
  - `sherlock-bounties`: `f691382d715d50fcf471cb70e074abbbd1d00b0335a3fa4046ed2b99dbe1b986`
  - `arxiv-cryptography`: `708237551c62ad0e0e7e1b9a823dff2c946745a99c6d279ba894aaf284c00a99`
  - `ethglobal-events`: `06a6fd437851f24e1b0513421f1389620ee201851f396b5220ac04031a06310a`
- Latest canonical predecessors are, respectively, `9e063815d1081f098c97ab5981f71b4c2e94d00edba6ca61198d1d9b2e762045`, `33b5c83409f9f2704f19483a69440ce82525b23c05a7f5ef2d401ac816c0f2ce`, `6aaa4c2de88200e0be6144cb024734167d513c9c79a1b11d6f283958bbd2b19f`, `246032d40532baab6948400a0678b2421b6342024d13ae16258ac80583bb26c3`, and the Aug. 29 afternoon ETHGlobal fingerprint `361c6c0ce2988ea281442a7b6b6ac8ca94574cda8074242b2d7966fed9037179`.
- No Aug. 30 canonical write has been made by this integrity pass. The raw snapshot remains contributed evidence until the native replay is staged and validated.
- The replay scope should be exactly five history additions at `2026-08-30T07:38:20Z` and five matching registry timestamp advances, with no later-snapshot replay mixed in.

## Concurrent / stale contribution state

- PR #170 is Sep. 13 research-only work based on pre-PR171 main. It does not itself advance canonical source freshness and must reconcile current `main` before integration.
- PR #161 and PR #163 remain stale-base research contributions and require current-main reconciliation before merge.
- Older open research PRs remain contributed evidence lanes and must be reconciled only when chronology/source-overlap order permits.
- No open research PR may leapfrog the Aug. 30 morning replay gate merely because its external facts are newer.

## Toolset / case / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Shared tool registration remains canonical in `data/tools.json`; normal tools/toolsets/cases/intelligence/evidence must surface through canonical registries/manifests/site-data builders rather than bespoke `site/index.html` edits.
- Structured active cases remain `20260816-310-btc-challenge` and `20260906-pwnsec-ctf-2026`.
- The 310 case remains internal evidence only and does not establish an external puzzle solve, private key, payout, or provenance of `310_challenge.png`.
- PwnSec remains authorization-bounded; repository evidence does not establish participant registration/team/faction state.

## Security / maintenance state

- Preserve all primary evidence, hashes, provenance, and research artifacts. Do not delete or relocate evidence silently.
- Bounded code search in this pass found no indexed `shell=True`, `os.system(`, or literal `BEGIN PRIVATE KEY` matches; this is a spot check, not a comprehensive secret/static-analysis audit.
- GitHub Actions still use major-version action tags rather than immutable commit SHAs, and CI installs broad dependency ranges rather than a lockfile. Supply-chain drift remains a hardening debt.
- `main` remains unprotected with required status-check enforcement disabled; release discipline depends on workflow verification and review practice.
- Legacy root truthfulness debt remains in `QUICK_START_REAL_MONEY.sh` and `TOOLS_AUDIT.md`; preserve history and reconcile those claims separately.

## Coordination state

- `docs/WORK_QUEUE.md` and `data/integration_queue.json` agree that Aug. 30 morning is next and Aug. 29 morning/afternoon are integrated.
- The latest append-only handoff records the post-PR171 queue synchronization but predates the actual PR #172 merge and this Aug. 30 independent readiness verification. The write interface available to this pass requires whole-file replacement, so the journal was not risked from partial retrieval; this PR description carries the complete handoff until an append-safe/full-file path is available.

## Current operating priorities

1. Stage only the Aug. 30 morning native replay from `intelligence/feeds/2026-08-30-source-health.json`; do not mix Aug. 30 afternoon or later Sep. research.
2. Require deterministic replay/readiness assertions for all five hashes, exact latest predecessors, five-record/five-registry scope, idempotence, and registry non-rewind behavior.
3. Require source-history/registry validation, Core matrix, Intelligence Source Report, Daily Maintenance, Agent Operations/site-data compatibility, semantic diff review, and no unresolved review threads before merge.
4. Require post-merge exact-main Core and Pages success before advancing to Aug. 30 afternoon.
5. Reconcile later research PRs only after current-main conflict review and according to chronology/source overlap.
6. Continue supply-chain/action pinning and legacy root truthfulness cleanup only as separate bounded objectives that preserve evidence.

## Next handoff

Current `main` is `e61b39d26aaaf46459ac1d45a7621a5d3a1854d9`, the merge of PR #172. Exact-main Core `34747174084`, Pages `34747174083`, later Daily Maintenance `34760836965`, and Intelligence Source Report `34763291440` are green. The Aug. 30 morning raw snapshot has now passed independent fingerprint and predecessor verification for all five observations, but no canonical write was made in this pass. The exact next action is to stage only that five-record/five-registry native replay, add deterministic readiness coverage if needed, and repeat the full exact-head plus post-merge validation chain before Aug. 30 afternoon is considered.
