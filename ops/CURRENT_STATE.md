# Current Repository State

Last reconciled: 2026-09-06 07:22 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `3568d061b8f0cd34c796f2f276fdd0cda8f1a00e`, the merge of PR #138 (`Ops: reconcile state after PR #137 merge`).
- Exact-merge Core validation run `33988712288` completed successfully on `3568d061b8f0cd34c796f2f276fdd0cda8f1a00e`.
- Exact-merge Deploy operations dashboard run `33988712403` completed successfully on the same commit.
- No open repository issue currently blocks the chronological source-replay lane.
- Release-health claims in this snapshot are limited to observed GitHub Actions and repository-side validation; a fresh independent browser render was not established in this pass.

## Build / integration state

- Canonical source history remains through Aug. 28 afternoon at `2026-08-28T19:37:39Z`.
- PR #134 (`Build: verify Aug 29 morning source replay readiness`) added only `tests/test_aug29_source_readiness.py`; it did not replay Aug. 29.
- The Aug. 29 morning raw snapshot `intelligence/feeds/2026-08-29-source-health.json` remains replay-ready under the canonical normalization contract. All five stored hashes and exact latest predecessors are locked by deterministic regression coverage.
- Verified Aug. 29 fingerprints remain:
  - `challenge-gov`: `9e063815d1081f098c97ab5981f71b4c2e94d00edba6ca61198d1d9b2e762045`
  - `ctftime-upcoming`: `33b5c83409f9f2704f19483a69440ce82525b23c05a7f5ef2d401ac816c0f2ce`
  - `sherlock-bounties`: `6aaa4c2de88200e0be6144cb024734167d513c9c79a1b11d6f283958bbd2b19f`
  - `arxiv-cryptography`: `246032d40532baab6948400a0678b2421b6342024d13ae16258ac80583bb26c3`
  - `ethglobal-events`: `5b270d1af189b17c8508993b6c5ed10d6794acec5e254eee7dc77f2c2f84925c`
- The next canonical source write remains a separate bounded Aug. 29 morning replay: exactly five `2026-08-29T07:38:35Z` source-history records and only the five matching source-registry `last_checked_at` advances.

## Current research / intelligence state

- Later research remains contributed/noncanonical evidence until chronology reaches it.
- Open research lanes remain PR #103/#106 (Aug. 31), PR #109/#112 (Sep. 1), PR #116/#120 (Sep. 2), PR #123/#125 (Sep. 3), PR #131/#136 (Sep. 4), and PR #139 (Sep. 5).
- PR #139 is a one-file Sep. 5 research contribution at head `87dbeb3aee68b45cd9b31c4ef11c2cc2075d5cf3`. It was opened from pre-PR138 main `a867e6a77ffa3e5bb127804e84313ff97d9d9ad8`; GitHub currently reports it mergeable, but its arXiv authorization-memory benchmark claims, TFC CTF status/qualification claims, and ETHOnline prize/actionability claims remain contributed evidence and require independent verification when chronology reaches Sep. 5.
- Aug. 29 afternoon, Aug. 30 morning/afternoon, and all later research remain blocked until Aug. 29 morning is canonically replayed and verified.
- Public bounty/program/event listings remain discovery evidence only and are not authorization to test any target.
- xTech|Search 10 remains non-actionable until authoritative Army/RFI/application evidence resolves conflicting official date/state surfaces.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, payout, or puzzle solve.
- Root legacy/generated artifacts remain preservation debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Canonical tools, toolsets, cases, source health, repository data, relationship views, and Agent Operations are expected to flow through registries/manifests/site-data builders rather than bespoke HTML.
- No user-facing canonical source data changed in PR #138, so no source/content freshness advance was introduced by that merge.

## Security / maintenance state

- The repository maintenance contract remains non-destructive: preserve evidence, report suspicious secret-like files, compile Python entry points, and inventory generated/root artifacts rather than deleting them automatically.
- Earlier bounded default-branch checks found no indexed `shell=True` or `os.system(` use; this remains a targeted check, not a complete security audit.
- Workflow dependencies continue to use major-version action tags rather than immutable commit pins; action pinning/runtime migration and dependency-lock strategy remain supply-chain hardening debt, not a release blocker for the current replay lane.
- No primary research artifact was deleted, moved, or rewritten in this pass.

## Known state / debt

- `docs/WORK_QUEUE.md` remains behind current chronology: its P2 source-health row still describes the already-completed Aug. 28 afternoon replay instead of the verified Aug. 29 morning replay.
- `data/integration_queue.json` is also behind current chronology: the Aug. 28 item still says `needs-integration`, Aug. 29 remains blocked without the PR #134 readiness evidence, and Sep. 4/Sep. 5 research lanes are not fully represented. Preserve prior queue history when reconciling it.
- `docs/AGENT_HANDOFF.md` remains append-only and its stored latest integrity entry is materially behind current repository state. The connected contents writer performs whole-file replacement rather than atomic append; do not risk truncating historical entries. This pass records the complete handoff in its PR description until a byte-preserving append path is available.
- A fresh independent public Pages browser render was not established in this pass; exact-merge Pages workflow success is verified.

## Current operating priorities

1. Merge this bounded coordination update only after fresh exact-head CI is green.
2. Reconcile `docs/WORK_QUEUE.md` and `data/integration_queue.json` history-preservingly without changing canonical source freshness.
3. Stage a separate Aug. 29 morning canonical replay using the verified raw snapshot, writing exactly five `2026-08-29T07:38:35Z` history records with predecessor links locked by `tests/test_aug29_source_readiness.py`.
4. Advance only the five corresponding source-registry timestamps; preserve all raw research evidence unchanged.
5. Run source-history, source-registry, collection-report, intelligence, site-data/Agent Operations, Core, Intelligence Source Report, and Daily Maintenance validation on the replay head.
6. Only after the replay is independently verified may Aug. 29 afternoon advance, followed by Aug. 30 morning/afternoon and later research PRs in timestamp/source-overlap order.

## Coordination note

This integrity pass started from actual `main` `3568d061b8f0cd34c796f2f276fdd0cda8f1a00e`, re-read README/governance/automation/maintenance/current-state/work-queue/integration-queue surfaces, inspected the stored handoff tail, open PRs, exact-main Actions, and the toolset catalog. PR #138 had merged but `ops/CURRENT_STATE.md` still described pre-merge `a867e6a7...`. Exact-main Core and Pages are green. PR #139 is newer contributed research from the pre-PR138 base and was not promoted. This reconciliation changes coordination truth only; it does not promote any solve, payout, opportunity, security finding, capability, tool maturity, source freshness, or authorization claim.

## Next handoff

Repo Integrity / Build Integration should merge this coordination update only after fresh exact-head validation is green. Then reconcile the stale work/integration queues without deleting history and perform the separate bounded Aug. 29 morning canonical replay. Do not advance Aug. 29 afternoon or later contributed research until the five-record morning replay and matching registry timestamps are independently verified green.