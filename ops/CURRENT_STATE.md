# Current Repository State

Last reconciled: 2026-09-04 14:17 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `8992891ad511a508509161e4fa976f37030be6d8`, the merge of PR #134 (`Build: verify Aug 29 morning source replay readiness`).
- PR #134 final head `6b98c06e5a116728d3cec29fef7625c5787f7b0b` passed Core validation `33851613891` across the Python matrix and Daily Repository Maintenance `33851613886` before merge.
- On the exact merge commit `8992891ad511a508509161e4fa976f37030be6d8`, scheduled Daily Repository Maintenance `33878566616` and Intelligence Source Report `33884266301` both completed successfully.
- No open repository issue currently blocks the chronological source-replay lane.
- A fresh exact-merge Core or Pages deployment run was not observed in this pass; do not infer those checks from the successful scheduled Maintenance/Source Report runs.

## Build / integration state

- Canonical source history remains through Aug. 28 afternoon at `2026-08-28T19:37:39Z`.
- PR #134 did not mutate canonical source history, registry freshness, raw evidence, opportunity/intelligence state, cases, tools, toolsets, or website HTML. It added `tests/test_aug29_source_readiness.py` only.
- The Aug. 29 morning raw snapshot `intelligence/feeds/2026-08-29-source-health.json` is now independently replay-ready under the canonical normalization contract. All five stored hashes recompute exactly and all five latest canonical predecessors are locked by regression coverage.
- Verified Aug. 29 fingerprints:
  - `challenge-gov`: `9e063815d1081f098c97ab5981f71b4c2e94d00edba6ca61198d1d9b2e762045`
  - `ctftime-upcoming`: `33b5c83409f9f2704f19483a69440ce82525b23c05a7f5ef2d401ac816c0f2ce`
  - `sherlock-bounties`: `6aaa4c2de88200e0be6144cb024734167d513c9c79a1b11d6f283958bbd2b19f`
  - `arxiv-cryptography`: `246032d40532baab6948400a0678b2421b6342024d13ae16258ac80583bb26c3`
  - `ethglobal-events`: `5b270d1af189b17c8508993b6c5ed10d6794acec5e254eee7dc77f2c2f84925c`
- The readiness regression allows either the current pre-replay state or exactly one correct canonical/idempotent Aug. 29 replay state; duplicate or mismatched records fail.
- The next build action is a separate bounded Aug. 29 morning canonical replay: exactly five `2026-08-29T07:38:35Z` history records and only the five matching registry `last_checked_at` advances.

## Current research / intelligence state

- Later research remains contributed/noncanonical evidence until chronology reaches it. Open research lanes remain PR #103/#106 (Aug. 31), PR #109/#112 (Sep. 1), PR #116/#120 (Sep. 2), PR #123/#125 (Sep. 3), and PR #131 (Sep. 4).
- `intelligence/feeds/2026-08-29-afternoon-source-health.json`, Aug. 30 morning/afternoon raw evidence, and the later open research PRs must remain blocked until Aug. 29 morning is canonically replayed and verified.
- Public bounty/program listings remain discovery evidence only and are not authorization to test any target.
- xTech|Search 10 remains non-actionable until authoritative Army/RFI/application evidence resolves the conflicting official date/state surfaces.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, payout, or puzzle solve.
- Root legacy/generated artifacts remain preservation debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Canonical tools, toolsets, cases, source health, repository data, and Agent Operations are expected to flow through registries/manifests/site-data builders rather than bespoke HTML.
- No user-facing canonical data changed in PR #134, so no site-data content delta was introduced by that merge.

## Security / maintenance state

- The repository maintenance contract remains non-destructive: preserve evidence, report suspicious secret-like files, compile Python entry points, and inventory generated/root artifacts rather than deleting them automatically.
- Previous bounded default-branch searches found no indexed `shell=True` or `os.system(` usage; this remains a targeted check, not a complete security audit.
- Workflow dependencies continue to use major-version action tags rather than immutable commit pins; action pinning/runtime migration and dependency lock strategy remain supply-chain hardening debt, not a release blocker for the current replay lane.
- No primary research artifact was deleted, moved, or rewritten in this pass.

## Known state / debt

- `docs/WORK_QUEUE.md` still describes the already-completed Aug. 28 afternoon replay as the next P2 step. It must be reconciled to make Aug. 29 morning canonical replay the active source-health task.
- `data/integration_queue.json` is also behind current chronology and should mark the Aug. 28 afternoon lane integrated, record PR #134 replay-readiness verification, and preserve later contributed-research items without replacing historical queue entries.
- `docs/AGENT_HANDOFF.md` remains append-only and materially behind current state. The available connector performs whole-file replacement rather than atomic append; do not reconstruct or truncate the journal from partial reads. Preserve the exact handoff in the coordination PR description until a byte-preserving append can be performed safely.
- Direct public Pages render verification and exact-merge Core/Pages checks remain separate release-health debt for this commit.

## Current operating priorities

1. Merge the bounded post-PR134 coordination reconciliation only after its exact-head CI is green.
2. Stage a separate Aug. 29 morning canonical replay using the verified raw snapshot, writing exactly five `2026-08-29T07:38:35Z` history records with the exact predecessor links locked by `tests/test_aug29_source_readiness.py`.
3. Advance only the five corresponding source-registry timestamps; preserve all raw research evidence unchanged.
4. Run source-history, source-registry, collection-report, intelligence, site-data/Agent Operations, Core, Intelligence Source Report, and Daily Maintenance validation on the replay head.
5. Only after the replay is independently verified may Aug. 29 afternoon advance, followed by Aug. 30 morning/afternoon and then the later research PRs in timestamp/source-overlap order.

## Coordination note

This integrity pass started from actual `main` `8992891ad511a508509161e4fa976f37030be6d8`, read the governing operating documents, current coordination surfaces, current Aug. 29 raw snapshot, recent commits, open PRs/issues, and current workflow state. PR #134 had already independently locked the five Aug. 29 hashes and predecessors without replaying them. The repository had no open issues, while `ops/CURRENT_STATE.md` and the shared work/integration queues lagged the merge. This reconciliation changes coordination truth only; it does not promote any solve, payout, opportunity, security finding, capability, tool maturity, or release/readiness claim beyond observed evidence.

## Next handoff

Repo Integrity / Build Integration should merge this coordination update only after fresh exact-head validation, then perform the separate bounded Aug. 29 morning canonical replay. Do not advance Aug. 29 afternoon or any later contributed research until the five-record morning replay and matching registry timestamps are independently verified green.
