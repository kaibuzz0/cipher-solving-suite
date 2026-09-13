# Current Repository State

Last reconciled: 2026-09-13 08:07 UTC
Default branch: `main`
Reconciled default-branch head: `359f9b9fd8996050533ee1d7a35e480d7377c4af`
Repository version: `v3.1.0` (README)

> This is a reconciliation snapshot. A branch/PR containing this file may have a newer commit by definition; compare material repository facts rather than treating that self-reference difference as drift.

## Verified health

- Current `main` is `359f9b9fd8996050533ee1d7a35e480d7377c4af`, the merge of PR #169 (`Ops: reconcile integration queue after PR #168`).
- Exact-main Core validation `34745388643` and Deploy operations dashboard / Pages `34745388618` succeeded on `359f9b9fd8996050533ee1d7a35e480d7377c4af`.
- Core covers direct-script regressions, Python compilation, source-registry/history/report validation, intelligence validation, artifact inventory, 310 migration/reproduction verification, site-data generation, maintenance diagnostics, repository-browser/tool/toolset discovery, and canonical tool visibility.
- Before this replay branch, source registry validated with 16 sources and source-check history with 77 checks. The branch-native replay validates at 16 sources and 78 checks.
- No standalone open GitHub issue currently blocks the chronological replay lane.
- Governance remains aligned that current repository state outranks agent memory, external AI output is contributed work rather than automatically trusted truth, primary evidence must be preserved, and normal tools/toolsets/cases/intelligence/evidence must flow through canonical registries/manifests/site-data builders.

## Canonical source / integration state

- On current `main`, canonical source history still ends at Aug. 29 morning, `2026-08-29T07:38:35Z`.
- PR #148 remains the last merged canonical replay on `main`: exactly five Aug. 29 morning records for `challenge-gov`, `ctftime-upcoming`, `sherlock-bounties`, `arxiv-cryptography`, and `ethglobal-events`, with only those five matching registry timestamp advances.
- Branch `build/aug29-afternoon-replay-20260913` now stages the next canonical replay through the repository-native `source-history` command. Native workflow run `34746769854` succeeded.
- The staged semantic change is exactly one `ethglobal-events` history record at `2026-08-29T19:40:52Z`, fingerprint `361c6c0ce2988ea281442a7b6b6ac8ca94574cda8074242b2d7966fed9037179`, predecessor `5b270d1af189b17c8508993b6c5ed10d6794acec5e254eee7dc77f2c2f84925c`, `change_state=changed`.
- The staged registry change advances only `ethglobal-events.last_checked_at` to `2026-08-29T19:40:52Z`; the other Aug. 29 morning source timestamps remain `2026-08-29T07:38:35Z`.
- The raw `intelligence/feeds/2026-08-29-afternoon-source-health.json` snapshot remains unchanged.
- `tests/test_aug29_afternoon_source_readiness.py` passed in the native replay workflow and continues to protect the exact hash, predecessor linkage, canonical uniqueness, and idempotence contract.
- `data/integration_queue.json` was reconciled on main by PR #169 and this replay branch updates the Aug. 29 item for the resulting integrated state while preserving prior queue history.
- This branch state is not canonical on `main` until independently reviewed, exact-head CI is green, and the replay PR is merged. Aug. 30 must not advance before then.

## Concurrent / stale contribution state

- PR #170 is a current-base Sep. 13 research-only contribution and does not overlap the Aug. 29 replay files or advance canonical source freshness.
- PR #168 is merged research evidence. Its xTech, ETHOnline, Code4rena, and PwnSec claims do not advance canonical source chronology.
- PR #161 and PR #163 remain open stale-base research contributions and require current-main reconciliation before merge.
- Other older open research PRs remain contributed evidence lanes and must be reconciled only when chronology/source-overlap order permits.

## Toolset / case / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental` maturity.
- Shared tool registration remains canonical in `data/tools.json`; `source-history` remains verified and the 310 solver/analyzer/reproduction tools remain explicitly `experimental`.
- Structured active cases remain `20260816-310-btc-challenge` and `20260906-pwnsec-ctf-2026`.
- The 310 case remains internal evidence only and does not establish an external puzzle solve, private key, payout, or provenance of `310_challenge.png`.
- PwnSec remains an authorization-bounded event case; repository evidence does not establish participant registration/team/faction state.
- User-facing repository state continues through generated site data; normal additions must not require bespoke `site/index.html` edits.

## Security / maintenance state

- Preserve all primary evidence, hashes, provenance, and research artifacts. Do not delete or relocate evidence silently.
- Current artifact inventory remains preservation-sensitive; cleanup must remain hash/provenance preserving.
- GitHub Actions still use major-version action tags (`actions/checkout@v4`, `actions/setup-python@v5`, `actions/upload-artifact@v4`) rather than immutable commit SHAs. Hosted runners currently warn that Node-20-targeting actions are being forced onto Node 24; immutable pinning/major-version refresh remains supply-chain hardening debt.
- CI installs broad dependency ranges rather than a lockfile, so dependency drift remains possible.
- `main` remains unprotected with required status-check enforcement disabled; release discipline depends on workflow verification and review practice.
- Legacy root truthfulness debt remains in `QUICK_START_REAL_MONEY.sh` and `TOOLS_AUDIT.md`; preserve history and reconcile those claims separately.

## Coordination drift requiring follow-up

- `docs/AGENT_HANDOFF.md` now has an append-only build entry for this staged native replay, but prior post-PR166/167/168 coordination coverage should remain preserved rather than rewritten.
- The replay branch still requires a PR, exact-head Core / Intelligence Source Report / Daily Maintenance validation, semantic diff review, and review-thread check before merge.
- After merge, exact-main Core and Pages must succeed before Aug. 30 chronology advances.
- Stale research PRs must be reconciled from current `main` and rerun through validation before merge.

## Current operating priorities

1. Open the bounded Aug. 29 afternoon replay PR from `build/aug29-afternoon-replay-20260913` and independently inspect its semantic diff.
2. Require exact-head Core matrix, Intelligence Source Report, Daily Maintenance, Agent Operations/site-data compatibility, and no unresolved review threads before merge.
3. Merge only if the net diff remains exactly one ETHGlobal history addition, one matching registry timestamp advance, history-preserving integration-queue reconciliation, current-state synchronization, and append-only handoff; raw snapshot must remain unchanged.
4. Require post-merge exact-main Core and Pages success.
5. Only after those checks, make Aug. 30 morning the next canonical replay gate and independently verify its fingerprints/predecessors before writing.
6. Reconcile later research PRs only after current-main conflict review and according to chronology/source overlap.

## Next handoff

Current `main` is `359f9b9fd8996050533ee1d7a35e480d7377c4af`, with exact-main Core `34745388643` and Pages `34745388618` green. Build branch `build/aug29-afternoon-replay-20260913` used the repository-native replay path in successful workflow run `34746769854`; the replay output commit is `2b3e4fbae115f8f3e3eba5ba14c889ad10c1abf0` before this state update. The branch validates 78 source-history checks and 16 registry sources and stages exactly one ETHGlobal record/timestamp advance while preserving the raw Aug. 29 afternoon snapshot. Open and validate the replay PR; merge only after independent semantic and CI review. If merged and post-merge Core/Pages remain green, Aug. 30 morning becomes the next chronology gate.
