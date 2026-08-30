# Current Repository State

Last reconciled: 2026-08-29 20:08 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `d7dbaa3d48b32729403b7d8cdcf8beb00827dedd`, the merge of PR #92, which preserved the exact green post-PR89 coordination branch after the connector could not transition draft PR #90 to ready.
- PR #92 reused exact head `5c06755e20f2cbf9b454ab9b014f88f3e27ed3b8`, whose Core validation `33270858667` succeeded and had no review threads.
- Post-merge Core `33272291998` and Deploy operations dashboard `33272291991` both succeeded on `d7dbaa3d...`; Pages/data packaging is therefore green on current main.
- Repo Integrity independently recomputed all five protected Aug. 26 observation SHA-256 values from `intelligence/feeds/2026-08-26-source-health.json`; all matched the preserved snapshot exactly.
- The verified Aug. 26 predecessor chain is: `challenge-gov` -> `756f0ba6...`, `sherlock-bounties` -> `b50b89ec...`, `arxiv-cryptography` -> `68147c9a...`, `ctftime-upcoming` -> `26679909...`, and `ethglobal-events` -> `b20807c6...`.
- PR #93 corrected replay head `7fe8ad422e6bc884c41db7e40bb4be866c642eaf` passed Core `33272597884` across Python 3.11/3.12/3.13, Intelligence Source Report `33272597878`, and Daily Repository Maintenance `33272597879`.

## Build / integration state

- Source-health observations through Aug. 25 are canonical on `main`.
- PR #93 stages the bounded Aug. 26 canonical replay at exact timestamp `2026-08-26T07:39:05Z`.
- The staged replay adds exactly five canonical history records, all classified `changed`, and advances only the matching source `last_checked_at` timestamps. Registry-level `updated_at` remains the newer Aug. 27 value and is not rewound.
- Per-file diff inspection confirms no older source-history records were removed and no unrelated source-registry metadata changed.
- Initial Core run `33272541781` failed because the Aug. 26 readiness regression still asserted the pre-canonical state (`replayed == 5`). Source registry/history/report, intelligence, artifact inventory, 310 migration/reproduction, dashboard-data generation and maintenance all passed in that run. The test was converted to the stronger post-integration contract: exact protected hashes/predecessors, exactly one canonical record per source/timestamp, matching registry advancement, idempotent library/direct-script replay, and byte-for-byte non-mutation. The corrected head then passed all validation above.
- xTech|Search 10 remains non-actionable: source-health replay preserves the conflicting official date/RFI evidence but does not establish a definitive submission window or active case.
- Open PR #75 owns Aug. 27 raw research, PR #82 owns Aug. 28 raw research, PR #85 owns Aug. 29 morning research, and PR #91 owns a later Aug. 29 ETHOnline prize observation. None may overtake the Aug. 26 canonical replay.

## Current research / intelligence state

- Aug. 22 morning, Aug. 22 afternoon, Aug. 23, Aug. 24, and Aug. 25 source-health observations are canonical.
- Aug. 26 is staged for canonical replay using the protected merged PR #66 snapshot and independently verified hashes/predecessors.
- NASA RASC-AL remains specialized research and should not be converted into generic actionable work without complete official competition guidelines.
- xTech|Search 10 remains a high-value watch/reconciliation lead until the authoritative RFI/application portal resolves the official-source conflict.
- Public bounty/program listings remain discovery evidence only and are not authorization to test a target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonical at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental`.
- PR #93 changes no tool/toolset registration, case, opportunity, primary evidence, or bespoke website HTML.
- Corrected Core `33272597884` passed dashboard-data generation and Agent Operations/site-data tests across the Python matrix; current-main Pages deployment `33272291991` is green.

## Known state / debt

- Independently review and merge PR #93 only if the final coordination head remains green and the exact five-record/five-timestamp contract holds.
- Keep xTech|Search 10 non-actionable until the complete authoritative RFI/application window is independently verified.
- After Aug. 26 is canonical, process Aug. 27 PR #75, Aug. 28 PR #82 snapshots in timestamp order, then Aug. 29 PR #85 and later PR #91.
- Root legacy/generated artifacts still require hash- and reference-preserving migration.
- External provenance/authenticity for `310_challenge.png` remains unresolved.

## Current operating priorities

1. Repo Integrity should independently verify and merge PR #93 if its final head remains green and the five-record/five-timestamp replay contract is exact.
2. After merge, mark Aug. 26 integrated and move the chronological source lane to Aug. 27 PR #75.
3. Process Aug. 27, Aug. 28, and Aug. 29 raw research strictly chronologically.
4. Keep xTech|Search 10 non-actionable until authoritative RFI/application evidence resolves the date conflict.
5. Continue 310 external-provenance and hash-preserving root-artifact work without inflating experimental capability claims.

## Coordination note

PR #90 was closed unmerged only because the connected draft-to-ready mutation failed. PR #92 preserved the exact unchanged green branch/head and merged it without rewriting history. PR #93 was created from that synchronized main and deliberately avoids later raw-research files. CI exposed an obsolete readiness assertion after canonical replay; it was upgraded to canonical/idempotence verification rather than bypassed or weakened.

## Next handoff

Verify PR #93 contains exactly five `2026-08-26T07:39:05Z` records with the protected fingerprints and expected Aug. 25 predecessors, advances only the five matching registry timestamps, leaves xTech actionability unresolved, preserves the stronger canonical/idempotence regression, and remains green for Core/source-report/maintenance/generated site-data/Agent Operations. Merge only if clean; then mark the Aug. 26 integration item integrated and move the chronological lane to Aug. 27 PR #75.
