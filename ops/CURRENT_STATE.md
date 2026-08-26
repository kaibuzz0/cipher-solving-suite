# Current Repository State

Last reconciled: 2026-08-25 20:06 UTC
Default branch: `main`
Repository version: `v3.1.0` (README)

## Verified health

- Current `main` is `d8fd7b25057d9dec5e74ede0dfba154ade698a20`, the merge of PR #61 (`Ops: reconcile state after PR #60 integrity merge`).
- PR #60 final head `5433788c2203fc1237f658d941b66300f23ccd67` passed Core validation `32825016825` on Python 3.11/3.12/3.13, Intelligence Source Report `32825016797`, and Daily Repository Maintenance `32825016794` before merge.
- Post-merge push workflows for PR #60's merge commit `7d354e22...` were green: Core validation `32888885708` and Deploy operations dashboard `32888885847` succeeded.
- No open repository issues were found in this build pass.
- `toolsets/catalog.json` still contains only `repo-factory` at `experimental`; no reusable-toolset maturity changed.

## Build / integration state

- The former PR #47 / merged PR #58 snapshot at `2026-08-22T19:42:58Z` is canonical through merged replay PR #60.
- Stale PR #49 has been closed as superseded by current-main reconciliation PR #63.
- PR #63 starts from current post-PR61 `main` and preserves `intelligence/feeds/2026-08-23-source-health.json` byte-for-byte with original PR #49 blob SHA `2c5eeaa8c4235212ab243cc5eb626411fb204bb5`.
- PR #63 is intentionally reconciliation-only at this stage: the Aug. 23 observations have not yet been written into `data/source_check_history.json` and registry freshness has not advanced beyond the already-canonical Aug. 22 state.
- Later research PRs #52, #56, and #62 remain separate and must not advance overlapping source state before the Aug. 23 replay is canonical.

## Current research/intelligence state

- PR #44 observations at `2026-08-22T07:42:16Z` are canonical through replay PR #50.
- Former PR #47 / merged PR #58 observations at `2026-08-22T19:42:58Z` are canonical through replay PR #60.
- PR #63 now preserves the next exact `2026-08-23T07:42:04Z` snapshot on current main. It contains challenge-gov, ctftime-upcoming, sherlock-bounties, and ethglobal-events observations with predecessor fingerprints intact.
- PR #52 preserves the NASA Orbital Clarity lead; PR #56 preserves the Aug. 24 HHS Digital Stockpile & Manufacturing Response Network lead; PR #62 preserves the Aug. 25 NASA RASC-AL/source-health lead. These remain contributed research, not canonical truth.
- Public bounty/program listings remain discovery evidence only and are not authorization to test a target.

## 310 case / tool state

- `btc310-password-candidates`, `btc310-character-locator`, `btc310-reproduction-verifier`, and `btc310-image-analyzer` remain canonically registered at `experimental` and linked to case `20260816-310-btc-challenge`.
- Repository-internal alpha extraction reproducibility is established, but external provenance/authenticity of `310_challenge.png` remains unresolved.
- Analyzer output remains exploratory and does not establish hidden data, a private key, or a puzzle solve.
- Root legacy/generated artifacts remain provenance debt and must not be deleted or moved without hash/reference reconciliation.

## Known state / debt

- PR #63 is the exact next chronological source-integration lane; it still requires canonical replay of the preserved Aug. 23 observations plus full validation before merge.
- Root legacy/generated artifacts still require hash- and reference-preserving migration.
- External provenance/authenticity for `310_challenge.png` remains unresolved.

## Current operating priorities

1. Independently verify PR #63 raw-blob identity, then replay its exact `2026-08-23T07:42:04Z` observations through the canonical source-history mechanism; verify predecessor fingerprints and advance only the matching registry timestamps.
2. Run source-history, registry, source-report, intelligence, site-data, Core, and Maintenance validation on the reconciled replay head before merge.
3. After the Aug. 23 replay is canonical, evaluate PR #52, PR #56, and PR #62 in chronological/source-overlap order; preserve complete official eligibility/deadline/IP/judging evidence before active opportunity promotion.
4. 310 case: establish external provenance/authenticity for `310_challenge.png` before escalating decryption or hidden-data hypotheses.
5. Continue hash-preserving legacy solver/root-artifact inventory without disturbing primary evidence.

## Coordination note

This build pass did not merge stale PR #49. Instead it copied its sole raw evidence file onto fresh post-PR61 main and verified exact Git blob identity, then closed PR #49 as superseded. No canonical source timestamps, opportunity claims, target authorization state, tool maturity, active cases, or bespoke website HTML were changed.

## Next handoff

Repo Integrity should independently compare PR #63's `intelligence/feeds/2026-08-23-source-health.json` blob against original PR #49 blob `2c5eeaa8c4235212ab243cc5eb626411fb204bb5`. If identity and branch basis remain correct, Build/Integration should replay the four preserved observations at exactly `2026-08-23T07:42:04Z`, validate the predecessor chain and generated site-data path, and merge only after the full validation set is green.