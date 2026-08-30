# Current Repository State

Last reconciled: 2026-08-30 07:24 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `8d2b20ba678fd776b0a90a0e38b8a4e061386a13`, the independently reviewed merge of PR #93.
- PR #93 final head `5403df4d36ce3160db58e45c786b8ca5d2ed84e5` passed Core validation `33272701911` on Python 3.11/3.12/3.13, Intelligence Source Report `33272701915`, and Daily Repository Maintenance `33272701910`.
- The Python 3.12 Core job ran 75 tests and all passed, including Aug. 26 canonical/idempotence replay, direct-script non-mutation, Agent Operations parsing, dynamic repository/toolset discovery, command-site generation, and canonical tool-visibility tests. Compilation, source registry/history/report validation, intelligence validation, artifact inventory, both 310 verification stages, site-data generation, maintenance, and the final failure gate also passed across the matrix.
- Post-merge Core validation `33299042160` and Deploy operations dashboard `33299042070` both succeeded on the actual merge commit `8d2b20ba...`.
- Repo Integrity independently recomputed all five protected Aug. 26 SHA-256 values from `intelligence/feeds/2026-08-26-source-health.json` and matched the preserved snapshot exactly. Every predecessor also matched the latest canonical Aug. 24/Aug. 25 source-history record.
- PR #93 added exactly five `2026-08-26T07:39:05Z` history records and advanced exactly five matching `last_checked_at` values; no older history records or unrelated registry metadata were removed or changed.

## Build / integration state

- Source-health observations through Aug. 26 are now canonical.
- Aug. 26 PR #66 raw evidence remains preserved unchanged; PR #93 replayed it without moving primary evidence or manufacturing later freshness.
- `challenge-gov`, `sherlock-bounties`, `arxiv-cryptography`, `ctftime-upcoming`, and `ethglobal-events` now carry the exact Aug. 26 canonical observation timestamp where applicable.
- xTech|Search 10 remains non-actionable. Current official surfaces still conflict: USA.gov lists Sep. 10-Oct. 19, the Army xTech page displays Aug. 5-Sep. 30 while still saying `Coming Soon`, and SBIR.gov lists Aug. 26-Sep. 23 for the linked topic. Do not infer one authoritative entry deadline until the complete Army RFI/application portal resolves the conflict.
- Open PR #75 owns Aug. 27 raw research, PR #82 owns Aug. 28 morning/afternoon raw research, PR #85 owns Aug. 29 morning research, and PR #91 owns a later Aug. 29 ETHOnline prize observation. These later contributions remain raw research until processed chronologically.

## Current research / intelligence state

- Aug. 22 morning, Aug. 22 afternoon, Aug. 23, Aug. 24, Aug. 25, and Aug. 26 source-health observations are canonical.
- Aug. 27 PR #75 is the next chronological source lane. Its Education challenge evidence must be independently rechecked before any structured opportunity promotion, and its source hashes/predecessors must be verified against canonical Aug. 26 history before replay.
- NASA RASC-AL remains specialized research and should not be converted into generic actionable work without complete official competition guidelines.
- Public bounty/program listings remain discovery evidence only and are not authorization to test a target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonical at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established; external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Toolset / UI state

- `repo-factory` remains the sole catalogued reusable toolset at `experimental`.
- PR #93 changed no tool/toolset registration, case, opportunity, primary evidence, or bespoke website HTML.
- Generated site-data, Agent Operations inputs, repository-browser discovery, Command Site generation, and canonical tool visibility passed on PR #93's final head; the post-merge operations-dashboard deployment also succeeded.

## Known state / debt

- Process Aug. 27 PR #75 next, then Aug. 28 PR #82 snapshots in timestamp order, then Aug. 29 PR #85 and PR #91.
- Keep xTech|Search 10 non-actionable until authoritative RFI/application evidence resolves the date conflict.
- Daily maintenance still reports known generated root artifacts; artifact inventory reports duplicates/orphans requiring hash- and reference-preserving migration rather than destructive cleanup.
- External provenance/authenticity for `310_challenge.png` remains unresolved.
- Workflow dependencies currently use supported major action tags rather than immutable commit pins, and Python CI installs bounded version ranges rather than a repository lockfile; treat this as non-blocking supply-chain hardening debt, not a release failure.

## Current operating priorities

1. Reconcile and independently review Aug. 27 PR #75 on current `main`; verify its protected hashes and predecessors before canonical replay.
2. Recheck the official Careers in Your Community Challenge rules before any actionability promotion; preserve its specialized Perkins V school/team eligibility boundary.
3. Then process Aug. 28 and Aug. 29 raw research strictly chronologically.
4. Keep xTech|Search 10 non-actionable until authoritative RFI/application evidence resolves the date conflict.
5. Continue 310 external-provenance and hash-preserving root-artifact work without inflating experimental capability claims.

## Coordination note

PR #93 was based directly on synchronized post-PR92 `main` and did not touch the later Aug. 27/Aug. 28/Aug. 29 raw research files. Its initial Core failure exposed obsolete pre-canonical readiness assertions; those assertions were replaced with stronger exact-canonical/idempotence checks rather than bypassed. Repo Integrity independently verified the five hashes, five predecessors, five-record history diff, five registry timestamp changes, xTech non-actionability boundary, final green CI, and post-merge Core/Pages workflows before advancing the lane.

## Next handoff

Mark the Aug. 26 integration item integrated, then reconcile PR #75 against current `main`. Independently recompute every Aug. 27 raw observation hash and predecessor against the new Aug. 26 canonical history; re-open the official Careers in Your Community rules; replay only evidence-backed observations through the deterministic source-history workflow; rerun source registry/history/report, intelligence, site-data, Agent Operations, Core and Maintenance validation; and only then consider merge. Aug. 28 and Aug. 29 follow afterward in chronological order.
