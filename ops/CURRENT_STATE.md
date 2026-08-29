# Current Repository State

Last reconciled: 2026-08-29 20:05 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `d7dbaa3d48b32729403b7d8cdcf8beb00827dedd`, the merge of PR #92, which preserved the exact green post-PR89 coordination branch after the connector could not transition draft PR #90 to ready.
- PR #92 reused exact head `5c06755e20f2cbf9b454ab9b014f88f3e27ed3b8`, whose Core validation `33270858667` succeeded and had no review threads.
- Post-merge Core `33272291998` and Deploy operations dashboard `33272291991` both succeeded on `d7dbaa3d...`; Pages/data packaging is therefore green on current main.
- Repo Integrity independently recomputed all five protected Aug. 26 observation SHA-256 values from `intelligence/feeds/2026-08-26-source-health.json`; all matched the preserved snapshot exactly.
- The verified Aug. 26 predecessor chain is: `challenge-gov` -> `756f0ba6...`, `sherlock-bounties` -> `b50b89ec...`, `arxiv-cryptography` -> `68147c9a...`, `ctftime-upcoming` -> `26679909...`, and `ethglobal-events` -> `b20807c6...`.

## Build / integration state

- Source-health observations through Aug. 25 are canonical on `main`.
- Branch `build/replay-aug26-source-health-20260829` stages the bounded Aug. 26 canonical replay at exact timestamp `2026-08-26T07:39:05Z`.
- The staged replay adds exactly five canonical history records, all classified `changed`, and advances only the matching source `last_checked_at` timestamps. Registry-level `updated_at` remains the newer Aug. 27 value and is not rewound.
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
- The Aug. 26 replay changes no tool/toolset registration, case, opportunity, primary evidence, or bespoke website HTML.
- Canonical registry/site-data discovery remains data-driven; current-main Pages deployment `33272291991` is green.

## Known state / debt

- Complete CI/source-report/maintenance verification for the Aug. 26 replay branch before merge.
- Keep xTech|Search 10 non-actionable until the complete authoritative RFI/application window is independently verified.
- After Aug. 26 is canonical, process Aug. 27 PR #75, Aug. 28 PR #82 snapshots in timestamp order, then Aug. 29 PR #85 and later PR #91.
- Root legacy/generated artifacts still require hash- and reference-preserving migration.
- External provenance/authenticity for `310_challenge.png` remains unresolved.

## Current operating priorities

1. Independently verify and merge the exact five-record Aug. 26 replay if CI/source-history/registry/report/intelligence/site-data/Agent Operations checks remain green.
2. Reconcile integration-queue/work-queue state after merge.
3. Process Aug. 27, Aug. 28, and Aug. 29 raw research strictly chronologically.
4. Keep xTech|Search 10 non-actionable until authoritative RFI/application evidence resolves the date conflict.
5. Continue 310 external-provenance and hash-preserving root-artifact work without inflating experimental capability claims.

## Coordination note

PR #90 was closed unmerged only because the connected draft-to-ready mutation failed. PR #92 preserved the exact unchanged green branch/head and merged it without rewriting history. The Aug. 26 replay branch was then created from that synchronized main and deliberately avoids later raw-research files.

## Next handoff

Verify the Aug. 26 replay branch contains exactly five `2026-08-26T07:39:05Z` records with the protected fingerprints and expected Aug. 25 predecessors, advances only the five matching registry timestamps, leaves xTech actionability unresolved, and passes Core, source-report, maintenance, generated site-data and Agent Operations validation. Merge only if clean; then mark the Aug. 26 integration item integrated and move the chronological lane to Aug. 27 PR #75.
