# Current Repository State

Last reconciled: 2026-08-28 20:12 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current base `main` for this build pass is `c3276bcf27c5a2348e8ea74c7cea71650a6e30e2`, the merge of PR #81.
- PR #81 exact head `44213f4e2f1bd0010d9848b541766babaf89c42d` passed Core validation `33203624769` with no review threads before merge.
- Post-merge `c3276bcf...` passed Core validation `33206416336` and Deploy operations dashboard / Pages `33206416216`.
- PR #83 implementation head `451c4be41264d0bba6c5edf2af7d9256cc7f09fd` passed Core `33207099679` across Python 3.11/3.12/3.13, Intelligence Source Report `33207099686`, and Daily Repository Maintenance `33207099676`.
- The initial PR #83 head `5ecd8978...` failed Core `33206895140` because the repository-specific Aug. 25 regression still expected the snapshot to be replay-ready after the same records had become canonical. Source Report `33206895105` and Maintenance `33206895164` had already passed. The test was corrected to verify canonical hashes/predecessors/registry state plus idempotent non-mutation; no production validation was weakened.
- Open research PR #75 owns only the Aug. 27 raw research snapshot; PR #82 owns reconciled Aug. 28 raw research. This Aug. 25 replay branch does not touch either raw evidence file.

## Build / integration state

- PR #79's canonical `python scripts/source_check_history.py replay-snapshot <snapshot>` path remains the source replay contract.
- PR #83 / branch `build/replay-aug25-source-health-20260828` applies the next bounded chronological replay from `intelligence/feeds/2026-08-25-source-health.json`.
- Exactly four records are added at `2026-08-25T19:42:47Z`: `ctftime-upcoming` `26679909...`, `sherlock-bounties` `b50b89ec...`, `arxiv-cryptography` `68147c9a...`, and `ethglobal-events` `b20807c6...`.
- Their canonical predecessors are respectively `a96cc699...`, `13c29e51...`, `8fb2b945...`, and `a1954da1...`; all four therefore classify as `changed`.
- Only those four source `last_checked_at` fields advance to `2026-08-25T19:42:47Z`. The registry-level `updated_at` remains `2026-08-27T20:02:00Z` because it is already newer than the replay timestamp, matching the merged replay implementation.
- The updated repository-specific regression recomputes each preserved observation hash, verifies exactly one canonical same-time record with the expected predecessor/change state, checks registry timestamps have not regressed, and proves replaying the same protected snapshot is idempotent and non-mutating.
- `data/integration_queue.json` marks the Aug. 25 lane `needs-review`; it is not marked integrated before independent verification/merge.
- `docs/WORK_QUEUE.md` points the source-health lane at independent verification of this Aug. 25 replay, with Aug. 26 next only after merge.

## Current research / intelligence state

- Aug. 22 morning, Aug. 22 afternoon, Aug. 23, and Aug. 24 source-health observations are canonical on `main`.
- The Aug. 25 PR #62 snapshot is staged on PR #83 but is not canonical on `main` until independent review and merge.
- The NASA 2027 RASC-AL lead remains specialized research only. Complete official competition guidelines remain required before structured opportunity/case promotion.
- Aug. 26 PR #66 remains blocked behind Aug. 25. Aug. 27 PR #75 and Aug. 28 PR #82 remain later chronological raw research lanes.
- Public bounty/program listings remain discovery evidence only and are not authorization to test a target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonically registered at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established, but external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental`; no toolset manifest/catalog changes occur in this replay pass.
- `source-history` remains registered at `verified` maturity. No new tool ID/path/maturity is introduced.
- The green Core run on implementation head `451c4be4...` passed dashboard-data generation, source registry/history validation, intelligence validation, 310 migration/reproduction, maintenance, and the final failure gate. No bespoke `site/index.html` edit is required.

## Known state / debt

- This current-state documentation update follows the green implementation head, so the final PR head should also remain green before readiness is claimed.
- Independently verify all four replay entries and registry timestamps against the protected raw snapshot.
- Complete official RASC-AL eligibility, judging, submission, IP, travel/cost, and top-award rules remain a separate gate before actionability promotion.
- After Aug. 25 is canonical, process Aug. 26 PR #66 and resolve the xTech|Search 10 official deadline conflict before any actionability claim.
- Root legacy/generated artifacts still require hash- and reference-preserving migration.
- External provenance/authenticity for `310_challenge.png` remains unresolved.
- `docs/AGENT_HANDOFF.md` is append-only; the available connector path replaces entire files, so this pass preserves the exact intended handoff in PR #83 rather than risk truncating journal history.

## Current operating priorities

1. Independently verify PR #83 against `intelligence/feeds/2026-08-25-source-health.json` and its corrected canonical/idempotent regression.
2. Require green validation on the final PR head and preserve the `needs-review` state until independent integrity review.
3. Merge only if clean; then process Aug. 26 PR #66, followed by Aug. 27 and Aug. 28 in chronological order.
4. Continue the 310 external-provenance gate and hash-preserving root-artifact inventory without inflating experimental capability claims.

## Coordination note

PR #83 started from post-PR81 `main` and deliberately avoids the raw research paths owned by PR #75 and PR #82. It advances only the four preserved Aug. 25 source observations and matching registry timestamps, leaves RASC-AL as non-actionable specialized research, does not alter tools/toolsets/cases/opportunities, and does not hand-edit website HTML. The first Core run usefully exposed a stale transition-state test; the correction converts that test into a durable canonical/idempotence check rather than bypassing validation.

## Next handoff

Repo Integrity should compare the four replay records and predecessor links to the protected Aug. 25 snapshot, confirm only the matching registry timestamps changed, verify the corrected canonical/idempotent regression and final-head CI/site-data compatibility, and merge only if the chronology and claim boundaries remain clean. After merge, Aug. 26 becomes the next canonical replay lane.
