# Current Repository State

Last reconciled: 2026-09-05 07:17 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `e3071cdb793b535ae615f498b7c8971f4bd2a056`, the merge of PR #135 (`Ops: reconcile repository truth after PR #134`).
- Exact-merge Core validation `33914235334` and Deploy operations dashboard `33914235286` both completed successfully on `e3071cdb793b535ae615f498b7c8971f4bd2a056`.
- PR #135 changed only `ops/CURRENT_STATE.md`; it did not mutate source history, registry freshness, raw evidence, opportunities, cases, tools, toolsets, or website HTML.
- No open repository issue currently blocks the chronological source-replay lane.
- Direct public Pages rendering could not be fetched from this runtime; release-health claims are limited to the successful exact-merge Pages workflow plus repository-side site-data validation in Core.

## Build / integration state

- Canonical source history remains through Aug. 28 afternoon at `2026-08-28T19:37:39Z`.
- PR #134 (`Build: verify Aug 29 morning source replay readiness`) added only `tests/test_aug29_source_readiness.py`; it did not replay Aug. 29.
- The Aug. 29 morning raw snapshot `intelligence/feeds/2026-08-29-source-health.json` remains independently replay-ready under the canonical normalization contract. All five stored hashes recompute exactly and all five latest canonical predecessors are locked by regression coverage.
- Verified Aug. 29 fingerprints:
  - `challenge-gov`: `9e063815d1081f098c97ab5981f71b4c2e94d00edba6ca61198d1d9b2e762045`
  - `ctftime-upcoming`: `33b5c83409f9f2704f19483a69440ce82525b23c05a7f5ef2d401ac816c0f2ce`
  - `sherlock-bounties`: `6aaa4c2de88200e0be6144cb024734167d513c9c79a1b11d6f283958bbd2b19f`
  - `arxiv-cryptography`: `246032d40532baab6948400a0678b2421b6342024d13ae16258ac80583bb26c3`
  - `ethglobal-events`: `5b270d1af189b17c8508993b6c5ed10d6794acec5e254eee7dc77f2c2f84925c`
- The next canonical write remains a separate bounded Aug. 29 morning replay: exactly five `2026-08-29T07:38:35Z` source-history records and only the five matching registry `last_checked_at` advances.

## Current research / intelligence state

- Later research remains contributed/noncanonical evidence until chronology reaches it.
- Open research lanes remain PR #103/#106 (Aug. 31), PR #109/#112 (Sep. 1), PR #116/#120 (Sep. 2), PR #123/#125 (Sep. 3), PR #131 (Sep. 4 morning), and PR #136 (Sep. 4 afternoon).
- PR #136 is a one-file research contribution at head `c67a2ff5a5292573ba42bdc627aa447c842c1bad`. It passed Core validation `33912437483`, but its base is the pre-PR135 commit `8992891ad511a508509161e4fa976f37030be6d8`. Its CTF-skills, NNS CTF, ETHOnline, prize, and event-status claims remain contributed evidence and must be independently re-opened when chronology reaches Sep. 4 afternoon.
- `intelligence/feeds/2026-08-29-afternoon-source-health.json`, Aug. 30 morning/afternoon raw evidence, and all later research PRs remain blocked until Aug. 29 morning is canonically replayed and verified.
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
- No user-facing canonical data changed in PR #135, so no site-data content delta was introduced by that merge.

## Security / maintenance state

- The repository maintenance contract remains non-destructive: preserve evidence, report suspicious secret-like files, compile Python entry points, and inventory generated/root artifacts rather than deleting them automatically.
- Previous bounded default-branch searches found no indexed `shell=True` or `os.system(` usage; this remains a targeted check, not a complete security audit.
- Workflow dependencies continue to use major-version action tags rather than immutable commit pins; action pinning/runtime migration and dependency lock strategy remain supply-chain hardening debt, not a release blocker for the current replay lane.
- No primary research artifact was deleted, moved, or rewritten in this pass.

## Known state / debt

- `docs/WORK_QUEUE.md` remains behind current chronology: its P2 source-health row still describes the already-completed Aug. 28 afternoon replay instead of the verified Aug. 29 morning replay.
- `data/integration_queue.json` is also behind current chronology: the Aug. 28 item still says `needs-integration`, Aug. 29 remains blocked without the PR #134 readiness evidence, and Sep. 4 research PRs are not yet represented. Preserve prior queue history when reconciling it.
- `docs/AGENT_HANDOFF.md` is append-only. This pass appends a new integrity entry without rewriting prior history.
- Direct public Pages render verification remains unavailable from this runtime even though the exact-merge deployment workflow is green.

## Current operating priorities

1. Reconcile the stale human-readable and machine-readable queues without replacing historical entries or changing canonical source freshness.
2. Stage a separate Aug. 29 morning canonical replay using the verified raw snapshot, writing exactly five `2026-08-29T07:38:35Z` history records with the exact predecessor links locked by `tests/test_aug29_source_readiness.py`.
3. Advance only the five corresponding source-registry timestamps; preserve all raw research evidence unchanged.
4. Run source-history, source-registry, collection-report, intelligence, site-data/Agent Operations, Core, Intelligence Source Report, and Daily Maintenance validation on the replay head.
5. Only after the replay is independently verified may Aug. 29 afternoon advance, followed by Aug. 30 morning/afternoon and then the later research PRs in timestamp/source-overlap order.

## Coordination note

This integrity pass started from actual `main` `e3071cdb793b535ae615f498b7c8971f4bd2a056`, re-read the governing operating documents and coordination surfaces, inspected recent commits, open PRs/issues, exact-main Actions, the toolset catalog, and the current research chronology. PR #135 had merged but `ops/CURRENT_STATE.md` still described the pre-merge commit. PR #136 was opened from the older pre-#135 base and passed Core on that contributed one-file research head; it was not treated as canonical truth. The repository has no open issues. This reconciliation changes coordination truth only; it does not promote any solve, payout, opportunity, security finding, capability, tool maturity, or source/release claim beyond observed evidence.

## Next handoff

Repo Integrity / Build Integration should merge this coordination update only after fresh exact-head validation is green, then reconcile `docs/WORK_QUEUE.md` and `data/integration_queue.json` without destroying history. The next source-health build remains the separate bounded Aug. 29 morning canonical replay. Do not advance Aug. 29 afternoon or later contributed research until the five-record morning replay and matching registry timestamps are independently verified green.
