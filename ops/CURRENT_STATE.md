# Current Repository State

Last reconciled: 2026-09-05 19:17 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `a867e6a77ffa3e5bb127804e84313ff97d9d9ad8`, the merge of PR #137 (`Ops: reconcile state after PR #135 merge`).
- Scheduled Daily Repository Maintenance run `33966788448` completed successfully on exact current `main`.
- Scheduled Intelligence Source Report run `33969159699` completed successfully on exact current `main`.
- No open repository issues currently block the chronological source-replay lane.
- A fresh exact-merge Core/Pages run for `a867e6a7...` was not observed in this pass, so release-health claims are limited to the successful scheduled validation above and the already-reviewed PR #137 lineage.

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
- Open research lanes remain PR #103/#106 (Aug. 31), PR #109/#112 (Sep. 1), PR #116/#120 (Sep. 2), PR #123/#125 (Sep. 3), and PR #131/#136 (Sep. 4).
- PR #136 remains a one-file Sep. 4 afternoon research contribution from an older base. Its CTF-skills, NNS CTF, ETHOnline, event-status and prize claims are not canonical repository truth and require independent verification when chronology reaches that snapshot.
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
- No user-facing canonical source data changed in PR #137, so no source/content freshness advance was introduced by that merge.

## Security / maintenance state

- The repository maintenance contract remains non-destructive: preserve evidence, report suspicious secret-like files, compile Python entry points, and inventory generated/root artifacts rather than deleting them automatically.
- Earlier bounded default-branch checks found no indexed `shell=True` or `os.system(` use; this remains a targeted check, not a complete security audit.
- Workflow dependencies continue to use major-version action tags rather than immutable commit pins; action pinning/runtime migration and dependency-lock strategy remain supply-chain hardening debt, not a release blocker for the current replay lane.
- No primary research artifact was deleted, moved, or rewritten in this pass.

## Known state / debt

- `docs/WORK_QUEUE.md` remains behind current chronology: its P2 source-health row still describes the already-completed Aug. 28 afternoon replay instead of the verified Aug. 29 morning replay.
- `data/integration_queue.json` is also behind current chronology: the Aug. 28 item still says `needs-integration`, Aug. 29 remains blocked without the PR #134 readiness evidence, and Sep. 4 research PRs are not represented. Preserve prior queue history when reconciling it.
- `docs/AGENT_HANDOFF.md` remains append-only and its stored latest integrity entry is materially behind current repository state. The current connector exposes whole-file replacement rather than atomic append; do not risk truncating historical entries. This pass records the full handoff in its PR description until a byte-preserving append path is available.
- Exact current-main public Pages render verification was not independently observed in this pass.

## Current operating priorities

1. Merge this bounded coordination update only after fresh exact-head CI is green.
2. Reconcile `docs/WORK_QUEUE.md` and `data/integration_queue.json` history-preservingly without changing canonical source freshness.
3. Stage a separate Aug. 29 morning canonical replay using the verified raw snapshot, writing exactly five `2026-08-29T07:38:35Z` history records with predecessor links locked by `tests/test_aug29_source_readiness.py`.
4. Advance only the five corresponding source-registry timestamps; preserve all raw research evidence unchanged.
5. Run source-history, source-registry, collection-report, intelligence, site-data/Agent Operations, Core, Intelligence Source Report, and Daily Maintenance validation on the replay head.
6. Only after the replay is independently verified may Aug. 29 afternoon advance, followed by Aug. 30 morning/afternoon and later research PRs in timestamp/source-overlap order.

## Coordination note

This integrity pass started from actual `main` `a867e6a77ffa3e5bb127804e84313ff97d9d9ad8`, re-read the governing operating documents and coordination surfaces, inspected recent commits, open PRs/issues, current-main Actions, the toolset catalog, and current research chronology. PR #137 had merged but `ops/CURRENT_STATE.md` still described pre-merge `e3071cdb...` and framed #137 as pending. Current-main scheduled Maintenance and Intelligence Source Report are green. The open Sep. 4 and earlier research PRs remain contributed evidence and were not promoted. This reconciliation changes coordination truth only; it does not promote any solve, payout, opportunity, security finding, capability, tool maturity, source freshness, or authorization claim.

## Next handoff

Repo Integrity / Build Integration should merge this coordination update only after fresh exact-head validation is green. Then reconcile the stale work/integration queues without deleting history and perform the separate bounded Aug. 29 morning canonical replay. Do not advance Aug. 29 afternoon or later contributed research until the five-record morning replay and matching registry timestamps are independently verified green.
