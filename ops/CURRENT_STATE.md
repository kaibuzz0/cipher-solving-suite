# Current Repository State

Last reconciled: 2026-09-07 07:26 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `a9526e36315ac82ad0d47c38db59c46d12d32e23`, the merge of PR #142 (`Ops: reconcile state after PR #140 merge`).
- Exact-main Core validation run `34056517338` completed successfully on `a9526e36315ac82ad0d47c38db59c46d12d32e23` across Python 3.11, 3.12, and 3.13.
- All three matrix jobs passed the test suite, Python compilation, source registry/history/report validation, intelligence validation, artifact inventory, both 310 verification stages, dashboard-data generation, maintenance, diagnostics uploads, validation summary, and final failure gate.
- Exact-main Deploy operations dashboard run `34056517311` completed successfully on the same commit.
- No open repository issues currently block the chronological source-replay lane.

## Build / integration state

- Canonical source history remains through Aug. 28 afternoon at `2026-08-28T19:37:39Z`.
- PR #134 (`Build: verify Aug 29 morning source replay readiness`) added deterministic readiness coverage only; it did not replay Aug. 29.
- The Aug. 29 morning raw snapshot `intelligence/feeds/2026-08-29-source-health.json` remains replay-ready under the canonical normalization contract. All five stored hashes and exact latest predecessors remain locked by deterministic regression coverage.
- Verified Aug. 29 fingerprints remain:
  - `challenge-gov`: `9e063815d1081f098c97ab5981f71b4c2e94d00edba6ca61198d1d9b2e762045`
  - `ctftime-upcoming`: `33b5c83409f9f2704f19483a69440ce82525b23c05a7f5ef2d401ac816c0f2ce`
  - `sherlock-bounties`: `6aaa4c2de88200e0be6144cb024734167d513c9c79a1b11d6f283958bbd2b19f`
  - `arxiv-cryptography`: `246032d40532baab6948400a0678b2421b6342024d13ae16258ac80583bb26c3`
  - `ethglobal-events`: `5b270d1af189b17c8508993b6c5ed10d6794acec5e254eee7dc77f2c2f84925c`
- The next canonical source write remains a separate bounded Aug. 29 morning replay: exactly five `2026-08-29T07:38:35Z` source-history records and only the five matching source-registry `last_checked_at` advances.
- Aug. 29 afternoon, Aug. 30 morning/afternoon, and all later research remain blocked from canonical source-history advancement until Aug. 29 morning is replayed and independently verified.

## Current research / intelligence state

- Later research remains contributed/noncanonical evidence until chronology reaches it.
- Open research lanes remain PR #103/#106 (Aug. 31), PR #109/#112 (Sep. 1), PR #116/#120 (Sep. 2), PR #123/#125 (Sep. 3), PR #131/#136 (Sep. 4), PR #139 (Sep. 5), and PR #141 (Sep. 6).
- PR #141 (`Research: preserve Sep 6 PwnSec reschedule and Cyborg case`) remains open from the older `3568d061...` base and is therefore stale relative to current main even if GitHub reports it mergeable. Its event/rule/case claims remain contributed evidence until reconciled at the correct chronology point.
- Public bounty/program/event listings remain discovery evidence only and are not authorization to test unrelated targets.
- xTech|Search 10 remains non-actionable until authoritative Army/RFI/application evidence resolves conflicting official date/state surfaces.

## 310 case / artifact state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal extraction reproducibility remains verified; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, payout, or puzzle solve.
- Known artifact migration/orphan/duplicate debt remains preservation work. Do not delete or relocate primary evidence without preserving hashes, provenance, references, and reproducibility.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Exact-main CI validates canonical tool discovery, repository-browser/tool/toolset paths, generated dashboard data, and Agent Operations parsing.
- Normal tools/toolsets/cases/intelligence/evidence remain required to flow through canonical registries/manifests/site-data builders rather than bespoke HTML.

## Security / maintenance state

- Previous bounded default-branch checks found no indexed `shell=True`, `os.system(`, or `subprocess.run(` occurrences. This remains a targeted check rather than a complete security audit.
- Exact-main Core compilation and maintenance stages are green for the documented Python entrypoints and portable 310 tools included by CI.
- Workflow dependencies continue to use major-version action tags such as `actions/checkout@v4`, `actions/setup-python@v5`, and `actions/upload-artifact@v4` rather than immutable commit pins. Action pinning/runtime migration and stronger dependency locking remain supply-chain hardening debt, not a release blocker for this coordination-only pass.
- No primary research artifact, source-history record, source-registry timestamp, tool maturity label, case status, opportunity status, or authorization boundary was changed by this reconciliation.

## Known coordination debt

- `docs/WORK_QUEUE.md` remains behind chronology: its P2 source-health row still describes the already-completed Aug. 28 afternoon replay rather than the verified Aug. 29 morning replay.
- `data/integration_queue.json` remains behind chronology: its file-level `updated_at` is Sep. 4 and the Aug. 28 lane is not fully reconciled to later replay/readiness work. Preserve prior queue history when repairing it.
- `docs/AGENT_HANDOFF.md` is materially stale: the stored append-only journal still ends with the Aug. 26 PR #67 integrity entry. The available contents mutation replaces the whole file rather than appending atomically; do not risk truncating or subtly rewriting the historical journal during a bounded coordination repair.
- PR #141 must be reconciled with whatever current `main` exists when its chronology point arrives. Preserve compatible Sep. 6 research/case work but do not let it advance canonical source history past the Aug. 29 gate.

## Current operating priorities

1. Merge this bounded post-PR142 coordination update only after fresh exact-head CI is green.
2. Reconcile `docs/WORK_QUEUE.md`, `data/integration_queue.json`, and the append-only handoff history without deleting or rewriting prior provenance.
3. Stage a separate Aug. 29 morning canonical replay using the verified raw snapshot, writing exactly five `2026-08-29T07:38:35Z` history records with predecessor links locked by `tests/test_aug29_source_readiness.py`.
4. Advance only the five corresponding source-registry timestamps; preserve all raw research evidence unchanged.
5. Run source-history, source-registry, collection-report, intelligence, site-data/Agent Operations, Core, Intelligence Source Report, and Daily Maintenance validation on the replay head.
6. Only after the replay is independently verified may Aug. 29 afternoon advance, followed by Aug. 30 morning/afternoon and later research PRs in timestamp/source-overlap order.
7. Reconcile PR #141 at its chronology point and independently re-verify any time-sensitive event/rule claims before participation or promotion.

## Coordination note

This integrity pass began from actual default-branch commit `a9526e36315ac82ad0d47c38db59c46d12d32e23`, re-read README/governance/automation/maintenance/current-state/work-queue/integration-queue/toolset surfaces, inspected the latest available append-only handoff entries, recent commits, open PRs/issues, and exact-main Actions. PR #142 had merged but `ops/CURRENT_STATE.md` still described pre-merge `edc07cd...`, creating a concrete coordination mismatch. Exact-main Core and Pages runs are green. This reconciliation changes coordination truth only; it does not promote a solve, payout, security finding, tool maturity, source freshness, or authorization claim.

## Next handoff

Repo Integrity / Build Integration should merge this coordination update only after fresh exact-head validation is green. Then perform a history-preserving work-queue/integration-queue/handoff reconciliation and the separate bounded Aug. 29 morning canonical replay. Do not advance Aug. 29 afternoon or later contributed research until the five-record morning replay and matching registry timestamps are independently verified green.
