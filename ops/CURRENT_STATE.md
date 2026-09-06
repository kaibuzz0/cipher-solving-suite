# Current Repository State

Last reconciled: 2026-09-06 19:22 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `edc07cd55e75019233d5cc1820fb355e999549ab`, the merge of PR #140 (`Ops: reconcile state after PR #138 merge`).
- Exact-main Core validation run `34020818158` completed successfully on `edc07cd55e75019233d5cc1820fb355e999549ab` across Python 3.11, 3.12, and 3.13.
- Python 3.12 collected and passed 84/84 tests. Direct-script regressions, Python compilation, source registry/history/report validation, intelligence validation, artifact inventory, 310 migration/reproduction verification, dashboard-data generation, Agent Operations parsing, repository-browser/tool/toolset discovery, and canonical tool visibility all passed.
- Exact-main Deploy operations dashboard run `34020818160` completed successfully on the same commit.
- Scheduled Daily Repository Maintenance run `34034420225` and Intelligence Source Report run `34037160807` also completed successfully on the same commit.
- The public GitHub Pages Operations Workspace is reachable and exposes the expected workspace, opportunities, intelligence, cases, tools, evidence, source-health, and Agent Operations navigation. Dynamic data correctness remains additionally covered by the green site-data and visibility regressions.
- No open repository issues currently block the chronological source-replay lane.

## Build / integration state

- Canonical source history remains through Aug. 28 afternoon at `2026-08-28T19:37:39Z`; current validation reports 72 canonical source checks across 16 registered sources.
- PR #134 (`Build: verify Aug 29 morning source replay readiness`) added only `tests/test_aug29_source_readiness.py`; it did not replay Aug. 29.
- The Aug. 29 morning raw snapshot `intelligence/feeds/2026-08-29-source-health.json` remains replay-ready under the canonical normalization contract. All five stored hashes and exact latest predecessors remain locked by deterministic regression coverage.
- Verified Aug. 29 fingerprints remain:
  - `challenge-gov`: `9e063815d1081f098c97ab5981f71b4c2e94d00edba6ca61198d1d9b2e762045`
  - `ctftime-upcoming`: `33b5c83409f9f2704f19483a69440ce82525b23c05a7f5ef2d401ac816c0f2ce`
  - `sherlock-bounties`: `6aaa4c2de88200e0be6144cb024734167d513c9c79a1b11d6f283958bbd2b19f`
  - `arxiv-cryptography`: `246032d40532baab6948400a0678b2421b6342024d13ae16258ac80583bb26c3`
  - `ethglobal-events`: `5b270d1af189b17c8508993b6c5ed10d6794acec5e254eee7dc77f2c2f84925c`
- The next canonical source write remains a separate bounded Aug. 29 morning replay: exactly five `2026-08-29T07:38:35Z` source-history records and only the five matching source-registry `last_checked_at` advances.
- The source collection report currently marks all 16 sources due because canonical registry freshness has intentionally not been advanced by later contributed snapshots. This is chronology debt, not evidence that the preserved later research files are absent.

## Current research / intelligence state

- Later research remains contributed/noncanonical evidence until chronology reaches it.
- Open research lanes remain PR #103/#106 (Aug. 31), PR #109/#112 (Sep. 1), PR #116/#120 (Sep. 2), PR #123/#125 (Sep. 3), PR #131/#136 (Sep. 4), PR #139 (Sep. 5), and PR #141 (Sep. 6).
- PR #141 (`Research: preserve Sep 6 PwnSec reschedule and Cyborg case`) is open at head `114dcfdef4999c66dd055aaa8b4c33647af1e350` from base `3568d061b8f0cd34c796f2f276fdd0cda8f1a00e`, so it is stale relative to current main even though GitHub presently reports it mergeable.
- Repo Integrity independently reopened the current PwnSec organizer and CTFtime event surfaces. The Sep. 12, 2026 14:00 UTC through Sep. 13 14:00 UTC event window, open/free registration, team limit of four, explicit Human/Cyborg leaderboards, Cyborg allowance for scripts/agents/autonomous pipelines, and the organizer rule to attack challenges rather than infrastructure are supported. CTFtime still lists prizes as TBD. These facts do not make PR #141 canonical source history and do not authorize activity outside event-provided challenges and current published rules.
- Aug. 29 afternoon, Aug. 30 morning/afternoon, and all later research remain blocked from canonical source-history advancement until Aug. 29 morning is replayed and independently verified.
- Public bounty/program/event listings remain discovery evidence only and are not authorization to test unrelated targets.
- xTech|Search 10 remains non-actionable until authoritative Army/RFI/application evidence resolves conflicting official date/state surfaces.

## 310 case / artifact state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal extraction reproducibility remains verified; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, payout, or puzzle solve.
- Exact-main artifact inventory remains valid at 40 items / 31,760,807 bytes, with 10 duplicate groups and 11 orphaned items. Migration states remain 12 generated outputs, 20 duplicates, seven needing case links, one `PRIMARY EVIDENCE — DO NOT MOVE YET`, zero safe-to-organize, and zero unknown-provenance items.
- Maintenance still reports 12 generated image artifacts at repository root. Preserve hashes/references before any relocation; no artifact was deleted or moved in this pass.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Exact-main tests confirm `repo-factory` discovery, bounded repository-browser previews, status counts, canonical user-visible tool flow to the Command Site snapshot, user-visible tool-source discovery, and Pages/workspace consumption of `data/tools.json`.
- Agent Operations parsing tests confirm the generated snapshot can parse the priority queue, current state, handoffs, and integration queue.
- Normal tools/toolsets/cases/intelligence/evidence remain required to flow through canonical registries/manifests/site-data builders rather than bespoke HTML.

## Security / maintenance state

- Fresh bounded default-branch searches found no indexed `shell=True`, `os.system(`, or `subprocess.run(` occurrences. This is a targeted check, not a complete security audit.
- The exact-main maintenance report status is `ok`; its only reported finding is the known generated-files-at-repository-root warning.
- Core and maintenance compilation checks are green for the documented Python entrypoints and the portable 310 tools included by CI.
- Workflow dependencies continue to use major-version action tags (`actions/checkout@v4`, `actions/setup-python@v5`, `actions/upload-artifact@v4`) rather than immutable commit pins. The Sep. 6 Core logs also warn that Node 20-targeting actions are being forced onto Node 24. Immutable action pinning/runtime migration and a stronger dependency-lock strategy remain supply-chain hardening debt, not a release blocker for this coordination-only pass.
- No suspicious secret-like filename finding was emitted by exact-main maintenance, and no primary research artifact was rewritten by this pass.

## Known coordination debt

- `docs/WORK_QUEUE.md` remains behind current chronology: its P2 source-health row still describes the already-completed Aug. 28 afternoon replay rather than the verified Aug. 29 morning replay.
- `data/integration_queue.json` is also behind current chronology: its file-level `updated_at` is Sep. 4, the Aug. 28 item is still represented as needing integration despite later replays, and later research/readiness lanes are incomplete. Preserve prior queue history when reconciling it.
- `docs/AGENT_HANDOFF.md` is materially stale: the stored append-only journal currently ends with the Aug. 26 PR #67 integrity entry. The complete blob can be read, but the available contents mutation replaces the entire file rather than appending atomically; do not risk truncating or subtly rewriting the historical journal during a bounded coordination repair.
- PR #141 must be reconciled with current main before merge. Preserve its compatible Sep. 6 research/case work, but do not let it advance canonical source history past the Aug. 29 gate.

## Current operating priorities

1. Merge this bounded coordination update only after fresh exact-head CI is green.
2. Reconcile `docs/WORK_QUEUE.md`, `data/integration_queue.json`, and the append-only handoff history without deleting or rewriting prior provenance.
3. Stage a separate Aug. 29 morning canonical replay using the verified raw snapshot, writing exactly five `2026-08-29T07:38:35Z` history records with predecessor links locked by `tests/test_aug29_source_readiness.py`.
4. Advance only the five corresponding source-registry timestamps; preserve all raw research evidence unchanged.
5. Run source-history, source-registry, collection-report, intelligence, site-data/Agent Operations, Core, Intelligence Source Report, and Daily Maintenance validation on the replay head.
6. Only after the replay is independently verified may Aug. 29 afternoon advance, followed by Aug. 30 morning/afternoon and later research PRs in timestamp/source-overlap order.
7. Reconcile PR #141 onto whatever current main exists when its chronology point arrives, preserving the independently supported PwnSec event/rule evidence while re-verifying the organizer rules immediately before any event participation.

## Coordination note

This integrity pass began from actual default-branch commit `edc07cd55e75019233d5cc1820fb355e999549ab`, re-read README/governance/automation/maintenance/current-state/work-queue/integration-queue/toolset surfaces, retrieved the append-only handoff journal, inspected recent commits/open PRs/issues and exact-main Actions, independently reopened the public Pages workspace, and independently checked the material PwnSec claims introduced by PR #141. PR #140 had merged but `ops/CURRENT_STATE.md` still described pre-merge `3568d061...`, creating a concrete coordination mismatch. This reconciliation changes coordination truth only; it does not promote a solve, payout, security finding, tool maturity, source freshness, or authorization claim.

## Next handoff

Repo Integrity / Build Integration should merge this coordination update only after fresh exact-head validation is green. Then perform a history-preserving queue/handoff reconciliation and the separate bounded Aug. 29 morning canonical replay. Do not advance Aug. 29 afternoon or later contributed research until the five-record morning replay and matching registry timestamps are independently verified green.